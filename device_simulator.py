import json
import os
import threading
import time

import paho.mqtt.client as mqtt

MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))

COMMAND_TOPIC = "smart_home/commands"
STATUS_TOPIC = "smart_home/status"
STATE_FILE = "home_state.json"

ALLOWED_DEVICES = {
    "bedroom_light",
    "hall_light",
    "fan",
    "ac",
}

ALLOWED_ACTIONS = {"ON", "OFF"}

state_lock = threading.Lock()


def load_state():
    """Load saved device states, or initialize all devices as OFF."""
    default_state = {
        device: {"state": "OFF"}
        for device in ALLOWED_DEVICES
    }

    if not os.path.exists(STATE_FILE):
        return default_state

    try:
        with open(STATE_FILE, "r", encoding="utf-8") as file:
            saved_state = json.load(file)

        for device in ALLOWED_DEVICES:
            if device in saved_state:
                saved_value = saved_state[device].get("state", "OFF")

                if saved_value in ALLOWED_ACTIONS:
                    default_state[device] = {"state": saved_value}

        return default_state

    except (OSError, json.JSONDecodeError, AttributeError):
        return default_state


def save_state(state):
    """Save current virtual device states."""
    temp_file = STATE_FILE + ".tmp"

    with open(temp_file, "w", encoding="utf-8") as file:
        json.dump(state, file, indent=2)

    os.replace(temp_file, STATE_FILE)


device_state = load_state()


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Connected to MQTT broker successfully!")
        print(f"Listening for commands on: {COMMAND_TOPIC}")

        client.subscribe(COMMAND_TOPIC, qos=1)

        # Publish the initial virtual device status.
        with state_lock:
            client.publish(
                STATUS_TOPIC,
                json.dumps(device_state),
                qos=1,
                retain=True,
            )

        print("Virtual smart-home devices are ready.")

    else:
        print(f"MQTT connection failed: {reason_code}")


def on_message(client, userdata, message):
    global device_state

    try:
        command = json.loads(message.payload.decode("utf-8"))

        device = command.get("device")
        action = command.get("action")

        # Independently validate every incoming MQTT command.
        if device not in ALLOWED_DEVICES:
            print(f"Rejected unknown device: {device}")
            return

        if action not in ALLOWED_ACTIONS:
            print(f"Rejected invalid action: {action}")
            return

        with state_lock:
            device_state[device] = {"state": action}
            save_state(device_state)

            current_state = json.dumps(device_state)

        client.publish(
            STATUS_TOPIC,
            current_state,
            qos=1,
            retain=True,
        )

        print(f"VIRTUAL DEVICE: {device} -> {action}")
        print(f"Saved updated status in {STATE_FILE}")

    except (json.JSONDecodeError, UnicodeDecodeError, AttributeError) as error:
        print(f"Invalid MQTT message rejected: {error}")

    except OSError as error:
        print(f"Could not save device state: {error}")


def main():
    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2,
        client_id="smart_home_device_simulator",
    )

    client.on_connect = on_connect
    client.on_message = on_message

    print("Starting virtual smart-home device simulator...")
    print(f"MQTT broker: {MQTT_BROKER}:{MQTT_PORT}")

    try:
        client.connect(MQTT_BROKER, MQTT_PORT, keepalive=30)
        client.loop_forever()

    except KeyboardInterrupt:
        print("\nStopping device simulator...")

    except OSError as error:
        print(f"Could not connect to MQTT broker: {error}")
        print("Check that Mosquitto is still running.")

    finally:
        client.disconnect()

if __name__ == "__main__":
    main()
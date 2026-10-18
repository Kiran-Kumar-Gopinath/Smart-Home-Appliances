
import streamlit as st
import paho.mqtt.client as mqtt

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
COMMAND_TOPIC = "smart_home/kiran_home_7319/commands"

st.set_page_config(page_title="AI Smart Home", page_icon="🏠")
st.title("AI Smart Home Controller")
st.write("Control your virtual smart home using text commands.")
st.caption("Chatbot + MQTT + ESP32 + Wokwi")

def send_mqtt_command(command):
    client = mqtt.Client(
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2
    )
    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.loop_start()
        result = client.publish(COMMAND_TOPIC, command, qos=0)
        result.wait_for_publish(timeout=5)

        if result.rc != mqtt.MQTT_ERR_SUCCESS:
            raise RuntimeError("MQTT publish failed")
        if not result.is_published():
            raise RuntimeError("MQTT publish timed out")
    finally:
        client.loop_stop()
        client.disconnect()

def understand_command(message):
    text = message.lower().replace("-", " ")
    words = set(text.replace(".", "").replace(",", "").split())

    # Detect action
    off_words = {"off", "disable", "stop", "switch-off", "turn-off"}
    on_words = {"on", "enable", "start", "activate", "switch-on", "turn-on"}

    if "off" in words or "disable" in words or "stop" in words:
        action = "OFF"
    elif "on" in words or "enable" in words or "activate" in words:
        action = "ON"
    else:
        return None, "Please say turn on or turn off a device."

    # Detect all devices
    all_phrases = [
        "all", "everything", "every device",
        "all devices", "all things", "whole house"
    ]
    if any(phrase in text for phrase in all_phrases):
        return f"ALL {action}", f"Turning {action.lower()} all devices."

    # Detect individual devices
    if any(word in words for word in ["bedroom", "bed", "room"]):
        device, name = "BEDROOM", "bedroom light"
    elif any(word in words for word in ["hall", "hallway"]):
        device, name = "HALL", "hall light"
    elif any(word in words for word in ["fan", "hot"]):
        device, name = "FAN", "fan"
    elif any(word in words for word in ["ac", "airconditioner", "air"]):
        device, name = "AC", "AC"
    else:
        return None, "Please specify bedroom light, hall light, fan, AC, or all devices."

    return f"{device} {action}", f"Turning {action.lower()} the {name}."

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_message = st.chat_input("Example: Turn on the fan")

if user_message:
    st.session_state.messages.append(
        {"role": "user", "content": user_message}
    )
    with st.chat_message("user"):
        st.markdown(user_message)

    with st.chat_message("assistant"):
        try:
            command, reply = understand_command(user_message)

            if command:
                send_mqtt_command(command)
                reply += f"\n\n**MQTT command:** `{command}`"
                st.success(reply)
            else:
                st.info(reply)

        except Exception as error:
            reply = f"Command failed. Check MQTT and Wokwi. Details: {error}"
            st.error(reply)

        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )

st.divider()
st.subheader("Try these commands")
st.markdown("""
- Turn on the bedroom light
- Turn off the hall light
- I am feeling hot. Turn on the fan
- Turn on the AC
- Turn on all things
- Turn off all things
""")
st.caption(f"MQTT topic: {COMMAND_TOPIC}")
st.caption(f"MQTT broker: {MQTT_BROKER}:{MQTT_PORT}")

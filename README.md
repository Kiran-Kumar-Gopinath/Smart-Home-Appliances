# AIoT Smart Home Automation Using MQTT, ESP32 and Wokwi

## Overview

This project demonstrates a chatbot-controlled smart home simulation. Users enter text commands through a Streamlit web dashboard to control four simulated devices: a bedroom light, hall light, fan and air conditioner.

The application recognizes commands, publishes them through MQTT, and sends them to an ESP32 simulated in Wokwi. The ESP32 controls LEDs representing each device.

The current demonstration version uses rule-based command recognition, so it does not require an external AI API key.

## Features

- Interactive Streamlit chatbot dashboard
- MQTT communication using the HiveMQ public broker
- ESP32 simulation in Wokwi
- Individual ON/OFF control for four devices
- Group commands to turn all devices ON or OFF
- Visual LED feedback in the simulation
- No paid AI API required for the current demonstration version

## System Architecture

**User command → Streamlit dashboard → Command recognition → MQTT broker → ESP32 in Wokwi → LEDs**

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Web dashboard |
| Paho MQTT | MQTT communication from Python |
| HiveMQ public broker | MQTT message broker |
| ESP32 | Simulated IoT controller |
| Wokwi | ESP32 and LED simulation |
| PubSubClient | MQTT library for ESP32 |

## Supported Commands

| Device | Example |
|---|---|
| Bedroom light | `Turn on the bedroom light` |
| Hall light | `Turn off the hall light` |
| Fan | `Turn on the fan` |
| Air conditioner | `Turn on the AC` |
| All devices | `Turn on all things` |
| All devices | `Turn off all things` |

## Requirements

- Python
- Visual Studio Code or another Python editor
- A Wokwi account
- Internet connection

## Setup Instructions

### 1. Install Python dependencies

Open a terminal in the project folder and run:

```bash
python -m pip install streamlit paho-mqtt
```

### 2. Start the dashboard

Run:

```bash
python -m streamlit run app.py
```

Open the local URL shown in the terminal, usually `http://localhost:8501`.

### 3. Start the ESP32 simulation

1. Open the Wokwi project.
2. Confirm that the PubSubClient library is included.
3. Start the simulation.
4. Wait for Wi-Fi and MQTT connection confirmation in the Serial Monitor.

### 4. Verify MQTT settings

The Python application and ESP32 sketch must use the same MQTT broker and topic.

Broker: `broker.hivemq.com`

Port: `1883`

Topic: `smart_home/kiran_home_7319/commands`

## ESP32 Pin Mapping

| Device | GPIO |
|---|---:|
| Bedroom light | 16 |
| Hall light | 17 |
| Fan | 18 |
| AC | 19 |

The LEDs represent devices in a simulation and do not physically control household appliances.

## Project Structure

```text
AIoT-Smart-Home-Automation/
├── app.py
├── sketch.ino
├── libraries.txt
├── README.md
└── .gitignore
```

## Security Note

This project uses a public MQTT broker over unencrypted port 1883 for demonstration purposes. Do not transmit sensitive information. A production deployment should use authenticated and encrypted MQTT communication.

Do not upload API keys, passwords, or `.env` files containing secrets to GitHub.

## Future Enhancements

- Integration with an AI-powered natural-language model
- Voice-based device control
- Physical sensors and relay modules
- Device-state feedback and monitoring
- Secure MQTT authentication and encryption

## Conclusion

This project demonstrates an IoT smart home control workflow using a web dashboard, MQTT messaging, an ESP32 and a Wokwi simulation. It provides a simple platform for exploring connected-device control and can be extended with AI services and physical hardware.

**Project domain:** Artificial Intelligence of Things (AIoT)  
**Current demo:** Rule-based text commands with MQTT and ESP32 simulation

## Author

**Project Title:** Chatbot-Controlled Smart Home Dashboard

**Domain:** Artificial Intelligence of Things (AIoT)

**Technologies:** Python, Streamlit, MQTT, ESP32 and Wokwi

**Developed by:** Kiran Kumar Gopinath

**Project Purpose:** Academic project demonstrating text-based smart home automation using MQTT communication and ESP32 simulation.


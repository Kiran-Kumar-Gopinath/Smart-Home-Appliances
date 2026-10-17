# AIoT Smart Home Automation Using Gemini AI, MQTT and ESP32

## Overview

This project implements a chatbot-controlled smart home dashboard using Artificial Intelligence and the Internet of Things (AIoT). Users can control simulated home devices by entering natural-language commands into a chatbot powered by Google's Gemini AI.

The chatbot interprets the user's request and sends a command through the MQTT messaging protocol. An ESP32 simulated in Wokwi receives the command and controls LEDs representing smart home devices.

## Features

- **AI-powered chatbot:** Understands natural-language device control requests using Gemini.
- **MQTT communication:** Transfers commands from the Python dashboard to the ESP32 simulation.
- **ESP32 simulation:** Uses Wokwi to simulate device control without requiring physical hardware.
- **Individual device control:** Controls the bedroom light, hall light, fan and AC independently.
- **Group device control:** Turns all simulated devices ON or OFF with one command.
- **Interactive dashboard:** Built using Streamlit.
- **Real-time visual feedback:** LEDs indicate the simulated state of each device.

## System Architecture

User Text Command → Streamlit Dashboard → Gemini AI → MQTT Broker → ESP32 in Wokwi → LED Indicators

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Web-based chatbot dashboard |
| Google Gemini API | Natural-language command interpretation |
| MQTT / HiveMQ | Message communication |
| ESP32 | Simulated IoT controller |
| Wokwi | ESP32 and LED simulation |
| Paho MQTT | MQTT communication in Python |
| PubSubClient | MQTT communication on ESP32 |
| python-dotenv | Environment configuration |

## Devices Controlled

| Device | MQTT Command Examples |
|---|---|
| Bedroom light | `BEDROOM ON`, `BEDROOM OFF` |
| Hall light | `HALL ON`, `HALL OFF` |
| Fan | `FAN ON`, `FAN OFF` |
| Air conditioner | `AC ON`, `AC OFF` |
| All devices | `ALL ON`, `ALL OFF` |

## Example User Commands

- Turn on the bedroom light.
- Switch off the hall light.
- I am feeling hot. Turn on the fan.
- Turn on the AC.
- Turn on all things.
- Turn off all things.

## Project Setup

### 1. Requirements

Install Python and Visual Studio Code. You will also need:
- A Google Gemini API key
- A Wokwi account and ESP32 simulation
- An internet connection
- Access to an MQTT broker

### 2. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AIoT-Smart-Home-Automation.git
cd AIoT-Smart-Home-Automation
```

Replace `YOUR-USERNAME` with your GitHub username.

### 3. Install Python dependencies

```bash
python -m pip install streamlit paho-mqtt python-dotenv google-genai
```

### 4. Configure environment variables

Create a `.env` file in the project folder:

```text
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=your_supported_gemini_model
MQTT_BROKER=broker.hivemq.com
MQTT_PORT=1883
```

Replace the API key and model placeholder with your own valid values. Use a Gemini model currently available to your API key.

**Security:** Never upload your actual API key or `.env` file to GitHub.

### 5. Configure the MQTT topic

The Python dashboard and ESP32 sketch must use the exact same topic:

```text
smart_home/kiran_home_7319/commands
```

If you change this topic, update it in both `app.py` and `sketch.ino`.

### 6. Run the dashboard

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

### 7. Run the ESP32 simulation

1. Open the Wokwi ESP32 project.
2. Ensure the `PubSubClient` library is included.
3. Check that the LED pin assignments and MQTT topic match the Python application.
4. Start the simulation.
5. Verify that the Serial Monitor reports a successful Wi-Fi connection, MQTT connection and topic subscription.
6. Enter a command in the Streamlit dashboard and observe the LED response.

## ESP32 LED Pin Mapping

| Device | ESP32 GPIO |
|---|---:|
| Bedroom light | GPIO 16 |
| Hall light | GPIO 17 |
| Fan | GPIO 18 |
| AC | GPIO 19 |

These LEDs represent devices in a simulation; they do not physically operate a fan, air conditioner or household lights.

## Project Structure

```text
AIoT-Smart-Home-Automation/
├── app.py
├── sketch.ino
├── libraries.txt
├── .env                 # Local configuration; do not upload
├── .gitignore
└── README.md
```

Your repository may also include screenshots, a project report, a presentation or a demonstration video.

## Testing

The project can be tested by sending individual ON/OFF commands for each device and group commands for all devices. Successful operation is indicated by the appropriate LED changes in Wokwi and MQTT messages in the Serial Monitor.

## Advantages

- Simple natural-language interaction
- Low-cost simulation-based development
- Modular integration of AI, MQTT and IoT
- No physical appliances required for the demonstration
- Easy to extend with additional simulated devices

## Limitations and Future Enhancements

- The current project uses simulated LEDs rather than physical appliances.
- MQTT communication over public port 1883 is unencrypted and should be restricted to non-sensitive demonstration data.
- Future versions could add authenticated private MQTT infrastructure, physical sensors, relay modules, device-state feedback, voice control and a more detailed dashboard.

## Conclusion

This project demonstrates how Generative AI and IoT communication can work together to provide a natural-language smart home control interface. Gemini interprets user requests, MQTT transfers device commands, and a simulated ESP32 controls LEDs in Wokwi, providing a practical AIoT demonstration.

## Author

**Project:** Chatbot-Controlled Smart Home Dashboard  
**Domain:** Artificial Intelligence of Things (AIoT)  
**Platform:** Python, Streamlit, Gemini API, MQTT and Wokwi ESP32

# 🛡 Smart Personal Desk Guardian

## Overview

**Smart Personal Desk Guardian** is an IoT-based physical security
monitoring system designed to protect personal workspaces from
unauthorized access and physical disturbances. The system combines an
**ESP32**, **PIR Motion Sensor**, **SW-420 Vibration Sensor**, and a
**Python-based monitoring dashboard** to detect suspicious activity in
real time.

Whenever motion or vibration is detected, the ESP32 activates an audible
buzzer, updates the monitoring dashboard, and records the incident with
a timestamp for future forensic analysis.

------------------------------------------------------------------------

## Objectives

-   Detect unauthorized movement near a desk.
-   Detect physical vibration or tampering.
-   Generate an audible security alert.
-   Display live monitoring information.
-   Maintain timestamped incident logs.

------------------------------------------------------------------------

## Key Features

-   Real-time motion detection
-   Desk vibration monitoring
-   Audible buzzer alarm
-   Live Python dashboard
-   Automatic incident logging
-   Threat level classification
-   Serial communication between ESP32 and Python

------------------------------------------------------------------------

## Hardware Components

-   ESP32 Dev Module
-   PIR Motion Sensor (HC-SR501)
-   SW-420 Vibration Sensor
-   Active Buzzer
-   Breadboard
-   Jumper Wires
-   USB Type-C Cable

------------------------------------------------------------------------

## Software Requirements

-   Arduino IDE
-   Python 3.x
-   Visual Studio Code
-   CustomTkinter
-   PySerial

------------------------------------------------------------------------

## System Workflow

1.  ESP32 monitors the PIR and vibration sensors.
2.  Sensor readings are processed to identify events.
3.  If motion or vibration is detected, the buzzer is activated.
4.  The ESP32 sends the event to the Python dashboard through serial
    communication.
5.  The dashboard updates the system status in real time.
6.  Every event is stored as a timestamped incident log.

------------------------------------------------------------------------

## Project Structure

``` text
SMART DESK GUARDIAN
│
├── ARDUINO/
├── GUI/
│   ├── dashboard.py
│   ├── web_dashboard.py
│   └── requirements.txt
├── IMAGES/
├── REPORT/
├── SCREENSHOTS/
└── README.md
```

------------------------------------------------------------------------

## GPIO Connections

  ESP32 Pin   Component
  ----------- -------------------------
  GPIO 14     PIR Motion Sensor
  GPIO 27     SW-420 Vibration Sensor
  GPIO 26     Active Buzzer

------------------------------------------------------------------------

## Applications

-   Personal Workspace Security
-   Office Desk Monitoring
-   Laboratory Equipment Protection
-   Educational IoT Projects
-   Digital Forensics Demonstrations

------------------------------------------------------------------------

## Future Scope

-   ESP32-CAM integration
-   Cloud-based monitoring
-   Mobile notifications
-   AI-based threat detection
-   Encrypted log storage
-   RFID or fingerprint authentication

------------------------------------------------------------------------

## Author

**Atulya Seethal**\
**M.Sc. Digital Forensics & Information Security**

------------------------------------------------------------------------

## License

This project is developed for academic and educational purposes.

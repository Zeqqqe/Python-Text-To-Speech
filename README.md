# zeqqe's Text-to-Speech CLI

> An interactive command-line tool for text-to-speech (TTS) synthesis using both eSpeak and Piper TTS engines.

---

## Features

* **Dual Engine Support:** Switch seamlessly between the fast, robotic **eSpeak** engine and the realistic, neural **Piper TTS** engine.
* **Interactive CLI:** An easy-to-use command-line interface for controlling all features.
* **Advanced Speech Customization (eSpeak):** Adjust rate, pitch, amplitude, word gap, and select from various voice variants.
* **High-Quality Speech Synthesis (Piper):** Leverages a modern neural network model for natural, human-like speech.
* **Play & Save Functionality:** Speak text directly and simultaneously save the output to a timestamped `.wav` file with a single command.

## Dependencies & Setup

This script is designed to run in a **Linux or WSL (Windows Subsystem for Linux)** environment.

### 1. System Dependencies

Required for the speech engines and audio playback. Open your terminal and run the appropriate command:

* **For Fedora/CentOS:**
    ```bash
    sudo dnf install espeak-ng alsa-utils alsa-plugins-pulseaudio
    ```
* **For Debian/Ubuntu:**
    ```bash
    sudo apt-get install espeak-ng alsa-utils alsa-plugins-pulseaudio
    ```

### Python Install Tutorial:
[![Python Install Tutorial](https://i.ytimg.com/vi/ddGTXBhaGWA/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLBHgfdcWE4URTwe-kzMvYQ_gcqAYw)](https://www.youtube.com/watch?v=ddGTXBhaGWA)


### 2. Python & Libraries

Ensure you have Python 3.8+ installed, then install the required libraries:

```bash
pip install pyttsx3 piper-tts
```
###### (This entire project was made with AI)

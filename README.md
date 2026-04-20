# Object Detection System

This is a mini project using YOLOv8 for real-time object detection

## Features

- Voice-controlled start
- Audio introduction
- Real-time object detection using webcam
- Text-to-speech feedback

## Required python version

- Be sure u should have the Python 3.10.0
ultralytics
pyttsx3
speech_recognition

## Technologies Used
- Python
- YOLOv8 (Ultralytics)
- OpenCV
- SpeechRecognition
- pyttsx3
- pygame

## How to Run

1. Install requirements:
   pip install -r requirements.txt

2. Run program:
   python main.py

3. Say:
   "start object detection"







🎯 Object Detection System (YOLOv8 + Voice Control)

A real-time object detection system powered by YOLOv8 with voice command activation and audio feedback. This project combines computer vision and speech technologies to create an interactive and user-friendly experience.

🚀 Features
🎙️ Voice-controlled start
🔊 Audio introduction on launch
📷 Real-time object detection using webcam
🗣️ Text-to-speech feedback for detected objects
🛠️ Tech Stack
Python 3.10
YOLOv8 (Ultralytics)
OpenCV
SpeechRecognition
pyttsx3
pygame
📦 Requirements

Install dependencies using:

pip install -r requirements.txt

Or install manually:

pip install ultralytics pyttsx3 SpeechRecognition pygame opencv-python
▶️ How to Run
python main.py

Then say:

🎤 "start object detection"

📸 How It Works
The program starts with an intro audio
It listens continuously for a voice command
When "start" is detected, the webcam activates
YOLOv8 performs real-time object detection
Detected objects are:
Highlighted with bounding boxes
Announced using text-to-speech

# Object Detection System (YOLOv8 + Voice Control)

A real-time object detection system powered by YOLOv8 with voice command activation and audio feedback. This project combines computer vision and speech technologies to create an interactive and user-friendly experience.

## Features
- Voice-controlled start
- Audio introduction on launch
- Real-time object detection using webcam
- Text-to-speech feedback for detected objects

## Tech Stack
- Python 3.10
- YOLOv8 (Ultralytics)
- OpenCV
- SpeechRecognition
- pyttsx3
- pygame

## Requirements

- Install dependencies using:

-pip install -r requirements.txt
it installs all the libraries in requirements.txt file

# How to Run
## python main.py

Then say:

"start object detection"

## How It Works
- The program starts with an intro audio
- It listens continuously for a voice command
- When "start" is detected, the webcam activates
- YOLOv8 performs real-time object detection
- Highlighted with bounding boxes
- Announced using text-to-speech

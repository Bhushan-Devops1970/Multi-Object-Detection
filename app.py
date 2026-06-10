import streamlit as st
import cv2
from ultralytics import YOLO
import time

# Load YOLO model
model = YOLO("yolov8n.pt")

# Streamlit UI
st.set_page_config(page_title="Object Detection App", layout="wide")
st.title("🎯 Real-Time Object Detection")

st.markdown("Click the button below to start webcam-based object detection.")

# Start/Stop buttons
start = st.button("▶ Start Detection")
stop = st.button("⏹ Stop Detection")

# Placeholder for video frames
frame_placeholder = st.empty()

# Session state to control loop
if "run" not in st.session_state:
    st.session_state.run = False

if start:
    st.session_state.run = True

if stop:
    st.session_state.run = False

# Open webcam
cap = cv2.VideoCapture(0)

last_spoken = ""
last_time = time.time()

# Main loop
while st.session_state.run:
    ret, frame = cap.read()
    
    if not ret:
        st.error("❌ Unable to access camera")
        break

    # Run YOLO detection
    results = model(frame, verbose=False)

    detected_objects = []

    for result in results:
        if result.boxes is not None:
            for box in result.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                label = model.names[cls]

                if conf > 0.6:
                    detected_objects.append(label)

                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    # Draw box
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                    # Label text
                    cv2.putText(
                        frame,
                        f"{label} {conf:.2f}",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 255, 0),
                        2,
                    )

                    # Simulated "speech" (text output instead)
                    if label != last_spoken and time.time() - last_time > 3:
                        st.toast(f"{label} detected")
                        last_spoken = label
                        last_time = time.time()

    # Display detected objects list
    if detected_objects:
        st.write("### Detected Objects:")
        st.write(", ".join(set(detected_objects)))

    # Show frame in Streamlit
    frame_placeholder.image(frame, channels="BGR")

# Release camera
cap.release()
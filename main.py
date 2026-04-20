import pygame                       # this librarie make program able to run the audio file  
import speech_recognition as sr     # convert voice input into text 
import pyttsx3                      # convert text into voice output
import cv2                          # OpenCV used for camera and image processing
from ultralytics import YOLO        # deep learing model which is use for object detection model  
import time                         # used for delays and timing
"""use of time library there is a while loop it runs continuously so we use time to make a 1 second gap"""


pygame.init()               # initialize all pygame modules (Starts audio system)
pygame.mixer.init()         # initialize audio mixer (for playing sound) 

engine = pyttsx3.init()     # Starts text-to-speech engine

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   # select voice (voices[1].id  M=0,F=1)
engine.setProperty('volume', 1.0)           # set volume (1.0 = max)

# function to convert text into speech (person detected)
def speak(text):
    engine.say(text)
    engine.runAndWait()

# in this block of function our intro audio file get triggerd
def play_intro():
    pygame.mixer.music.load("intro.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():    # waits until music finishes
        time.sleep(1)       # here exactly we have used time library to counter frequency of while loop

# CONTINUOUS VOICE LISTEN 
def listen_until_start():
    r = sr.Recognizer()
    # we r implimenting loop for taking disered voice input as command  
    while True:
        with sr.Microphone() as source:   # use microphone as input
            print("Listening... Say 'start object detection'")
            r.adjust_for_ambient_noise(source, duration=1)  # adjust for background noise
            audio = r.listen(source)

        try:
            # convert speech to text using Google API
            command = r.recognize_google(audio).lower()
            print("You said:", command)
            # check if user said "start"
            if "start" in command:
                speak("Starting object detection")    # give voice feedback
                return True                         # exit function and continue program

            else:
                print("Waiting for correct command...")

        except:
            # if speech is not recognized
            print("Didn't catch that, try again...")

# OBJECT DETECTION 
def start_detection():
    model = YOLO("yolov8n.pt")     # load YOLO object detection model
    cap = cv2.VideoCapture(0)    # open webcam (0 = default camera)

    # check if camera opened successfully
    if not cap.isOpened():  #If camera fails show error
        print("Camera error")
        speak("Camera not accessible")
        return

    print("Press Ctrl+c to quit")

    last_spoken = ""             # stores last spoken object
    last_time = time.time()      # stores last time speech was made


    # continuous loop for real-time detection
    while True:
        ret, frame = cap.read()   # capture frame from camera
        if not ret:               # If camera fails stop program
            break

        results = model(frame, verbose=False)  # run YOLO detection on frame try to find object 

        # loop through detection results
        for result in results:
            if result.boxes is not None:   # check if objects are detected
                for box in result.boxes:     # loop through each detected object
                    cls = int(box.cls[0])    # get class ID
                    conf = float(box.conf[0])  # get confidence score
                    label = model.names[cls]   # get object name


                    # only consider objects with confidence > 60%
                    if conf > 0.6:
                        
                        # get bounding box coordinates
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        
                        # draw rectangle around object
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        
                        # display object label and confidence ex... person 0.87
                        cv2.putText(frame, f"{label} {conf:.2f}",
                                    (x1, y1 - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    0.6, (0, 255, 0), 2)

                        # Speak with delay

                        #Only speak if the object is new AND at least 3 seconds have passed
                        if label != last_spoken and time.time() - last_time > 3:
                            speak(f"{label} detected")   
                            last_spoken = label    
                            last_time = time.time()
        # show output window with detection
        cv2.imshow("Object Detection", frame)

        # press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()                # release camera
    cv2.destroyAllWindows()      # close all OpenCV windows

def main():
    play_intro()                 # play intro music first

    if listen_until_start():     # wait for voice command
        start_detection()        # start object detection

if __name__ == "__main__":
    main()

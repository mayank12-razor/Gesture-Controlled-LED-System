import cv2
import mediapipe as mp
import serial
import time

# Initialize serial communication with Arduino
arduino = serial.Serial(port='COM7', baudrate=9600, timeout=1)
time.sleep(2)  # Wait for connection to establish

# Initialize Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

def detect_fingers(image, hand_landmarks):
    finger_tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky
    thumb_tip = 4
    finger_states = [0, 0, 0, 0, 0]  # Thumb, Index, Middle, Ring, Pinky

    # Check thumb
    if hand_landmarks.landmark[thumb_tip].x < hand_landmarks.landmark[thumb_tip - 1].x:
        finger_states[0] = 1

    # Check the other fingers
    for idx, tip in enumerate(finger_tips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            finger_states[idx + 1] = 1

    return finger_states

# Start capturing video
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers_state = detect_fingers(image, hand_landmarks)
            
            # Ensure only 0 or 1 values are sent
            byte_data = bytearray([min(1, max(0, x)) for x in fingers_state])
            arduino.write(byte_data)
            arduino.flush()  # Ensure data is sent
            print(f"Fingers State: {list(byte_data)}")

    cv2.imshow('Hand Tracking', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

    time.sleep(0.01)  # Small delay to avoid overwhelming the Arduino

cap.release()
cv2.destroyAllWindows()
arduino.close()

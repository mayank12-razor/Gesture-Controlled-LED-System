# Gesture-Controlled-LED-System
Title:
Gesture-Controlled LED System Using Hand Tracking and Arduino for Mining Applications
________________________________________
Objective:
To develop a real-time gesture-based LED control system using computer vision (Mediapipe) and Arduino, aiming to provide a hands-free and intuitive communication or signaling solution for underground mining environments where traditional controls are impractical or unsafe.
________________________________________
Components Required:
Hardware:
•	Arduino Uno (or compatible board)
•	LEDs (x5)
•	220Ω Resistors (x5)
•	Breadboard & jumper wires
•	USB cable for Arduino
•	Laptop or PC with camera
Software:
•	Python (with cv2, mediapipe, and pyserial libraries)
•	Arduino IDE
•	Serial Communication between Python and Arduino
________________________________________
Introduction:
Underground mining operations often face challenges related to visibility, communication, and manual equipment handling in confined spaces. Traditional control interfaces can be difficult to use when wearing protective gear or when operators’ hands are engaged in other tasks.
This project proposes a gesture-controlled LED system where hand gestures (finger positions) are tracked using a webcam and interpreted via Python's Mediapipe library. These gestures are then transmitted to an Arduino via serial communication to control multiple LEDs. The system can be used as a prototype for contactless signaling mechanisms or control interfaces in mining environments where hygiene, hands-free interaction, or remote signaling is critical.
________________________________________
Theory:
Hand Tracking using Mediapipe:
Google’s Mediapipe is a cross-platform library that provides machine learning solutions for live hand and body tracking. It detects 21 landmark points on each hand using a webcam feed. By analyzing the relative positions of landmarks, we determine whether each finger is extended (1) or folded (0).
Serial Communication:
Once the state of each finger (thumb to pinky) is determined, a 5-byte signal representing the finger positions is sent to the Arduino over a serial interface (USB). Each byte corresponds to a HIGH or LOW state of an LED.
Arduino LED Control:
The Arduino receives the byte array and maps each value to a digital pin (2 to 6). If a finger is up (value 1), the corresponding LED is turned ON; otherwise, it remains OFF.
This mimics a gesture-to-light conversion, enabling a physical response to digital gestures.
________________________________________
Application in Mining:
•	Hands-Free Signaling: Miners can use gestures to trigger visual signals when voice communication is difficult due to noise or protective gear.
•	Hazard Alerts: Different finger combinations can be mapped to predefined warning lights (e.g., gas leak, collapse risk, request for assistance).
•	Gesture-Based Controls: The system can be extended to operate relays, fans, or emergency systems via gesture input, reducing the need for physical contact.
•	Training and Simulation: Used in safety drills to simulate gesture-based emergency signals or operation of virtual machinery.


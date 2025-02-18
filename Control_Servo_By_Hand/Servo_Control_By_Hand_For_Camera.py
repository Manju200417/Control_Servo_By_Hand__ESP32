#  Note: This code is used to control the camera angle by hand using the servo motor.
#  The servo motor is connected to the ESP32 and the ESP32 is connected to the computer via Wi-Fi.
#  ensure that the ESP32 is connected to the same Wi-Fi network as the computer. 
#  this code uses to calculate the angle between the thumb and the index finger and send it to the ESP32 to control the servo motor.

import cv2
import mediapipe as mp
import requests
import math

ESP32_IP = "http://192.168.154.206"    # Replace with your ESP32 IP address 'you get from the serial monitor after uploading the code to the ESP32'

cap = cv2.VideoCapture(0) # 0 for default camera(Laptop camera)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.9, min_tracking_confidence=0.8) 
mp_draw = mp.solutions.drawing_utils

frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_center_x = frame_width / 2

scaling_factor = 0.5

previous_angle = 90

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            finger_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            finger_x = int(finger_tip.x * frame.shape[1])
            finger_y = int(finger_tip.y * frame.shape[0])
            thumb_x = int(thumb_tip.x * frame.shape[1])
            thumb_y = int(thumb_tip.y * frame.shape[0])

            distance = math.sqrt((thumb_x - finger_x) ** 2 + (thumb_y - finger_y) ** 2)

            raw_angle = int(distance * scaling_factor)

            raw_angle = max(0, min(raw_angle, 180))

            angle = raw_angle

            requests.get(f"{ESP32_IP}?angle={angle}")

            mp_draw.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            cv2.circle(frame, (finger_x, finger_y), 10, (0, 255, 0), -1)
            cv2.circle(frame, (thumb_x, thumb_y), 10, (255, 0, 0), -1)

            cv2.line(frame, (finger_x, finger_y), (thumb_x, thumb_y), (255, 255, 0), 2)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"): #press q to exit
        break

cap.release()
cv2.destroyAllWindows()

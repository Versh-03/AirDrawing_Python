import mediapipe as mp
import cv2
import math
import numpy as np

drawing= np.zeros((480, 640, 3), dtype=np.uint8)
hands = mp.solutions.hands.Hands(
    min_detection_confidence=0.4,
    min_tracking_confidence=0.4
)
cap= cv2.VideoCapture(0)

prev_point = None
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results=hands.process(rgb_frame)
    if results.multi_hand_landmarks:
        hand=results.multi_hand_landmarks[0]
        x = int(hand.landmark[8].x * 640)
        y = int(hand.landmark[8].y * 480)
        
        if(prev_point is not None):
            if(hand.landmark[8].y<hand.landmark[6].y and hand.landmark[12].y<hand.landmark[10].y):
                distance = math.sqrt((x - prev_point[0])**2 + (y - prev_point[1])**2)
                if(distance > 1):
                    cv2.line(drawing, prev_point, (x, y), (0, 0, 255), 3)
                    prev_point = (x, y)
            else:
                prev_point = None
        else:
            prev_point = (x, y)
    combined = cv2.addWeighted(frame, 0.5, drawing, 0.5, 0)
    cv2.imshow("Air Draw", combined)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        drawing = np.zeros((480, 640, 3), dtype=np.uint8)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
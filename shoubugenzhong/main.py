import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, max_num_hands=4, 
                        model_complexity=1, min_detection_confidence=0.5, 
                        min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils
handLmsStyle = mpDraw.DrawingSpec(color=(0, 0, 255), thickness=1)
handConStyle = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=2)

pTime = 0
cTime = 0

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    if ret:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)

        imgHeight, imgWidth = img.shape[:2]

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, 
                                       mpHands.HAND_CONNECTIONS, 
                                       handLmsStyle, handConStyle)

                for lm in handLms.landmark:
                    xPos, yPos = int(lm.x * imgWidth), int(lm.y * imgHeight)
                    cv2.circle(img, (xPos, yPos), 5, (92, 65, 214), cv2.FILLED)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f"FPS : {int(fps)}", (30, 50), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        
        cv2.namedWindow('img',cv2.WINDOW_GUI_NORMAL)
        cv2.imshow('img', img)
        if cv2.waitKey(1) == ord(' '):
            break
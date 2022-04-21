from sre_constants import IN_IGNORE, SUCCESS
import cv2
import os
from cvzone.HandTrackingModule import HandDetector

# Variables
width, height = 1280, 720 # camera size adjust
folderPath = "Presentation"

#camera setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Get the list of presentation images
pathImages = sorted(os.listdir(folderPath), key = len)
# print(pathImages)

# Variables
imgNumber = 0 # change the value of imgNumber to show 
#the differente images
hs, ws = int(120*1), int(213*1)
gestureThreshold = 400
buttonPressed = False
buttonCounter = 0
buttonDelay = 30

# Hand Detector
detector =HandDetector(detectionCon = 0.8, maxHands = 1)
 
while True:
    # import images

    success, img = cap.read()
    # flip the hand detector horizontally
    img = cv2.flip(img, 1) # 0 -> vetically flip
    pathfullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathfullImage)

    hands, img = detector.findHands(img)

    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 1)

    if hands and buttonPressed is False:
        hand = hands[0] #for single hand detection
        fingers = detector.fingersUp(hand)
        #add condition for hand up and down detection
        cx, cy = hand['center']
        lmList = hand['lmList'] # land mark list 
        indexFinger = lmList[8][0], lmList[8][1]
        

        if cy <=gestureThreshold: # if hand is at the height of the face
            # gesture 1 -Left
            if fingers == [1, 0, 0, 0, 0]:
                print("Left")
                
                if imgNumber > 0:
                    buttonPressed = True
                    imgNumber -= 1
              # gesture 2 -Right
            if fingers == [0, 0, 0, 0, 1]:
                print("Right")
                
                if imgNumber < len(pathImages)-1:
                    buttonPressed = True
                    imgNumber += 1
        # Gesture 3 - Show Pointer
        if fingers == [0, 1, 1, 0, 0]:
            cv2.circle(imgCurrent, indexFinger, 6, (0, 0, 255), cv2.FILLED)
    # Button pressed iteration
    if buttonPressed:
        buttonCounter += 1
        if buttonCounter > buttonDelay:
            buttonCounter = 0
            buttonPressed = False
    # Adding webcam images on the slides
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w - ws:w] = imgSmall

    cv2.imshow("image", img)
    cv2.imshow("slides", imgCurrent)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
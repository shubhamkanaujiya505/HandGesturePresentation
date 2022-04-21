from sre_constants import SUCCESS
import cv2
import os
from cvzone.HandTrackingModule import HandDetector

# Variables
width, height = 50, 20 # camera size adjust
folderPath = "Presentation"

#camera setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Get the list of presentation images
pathImages = sorted(os.listdir(folderPath), key = len)
print(pathImages)

# Variables
imgNumber = 0 # change the value of imgNumber to show 
#the differente images
hs, ws = int(120*1), int(213*1)

# Hand Detector
detector =HandDetector(detectionCon = 0.8, maxHands = 1)
 
while True:
    # import images

    success, img = cap.read()
    # flip the hand detector horizontally
    img = cv2.flip(img, 1) # 0 -> vetically flip
    pathfullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathfullImage)

    hands, img = detector.findHands(img, flipType = False)

    # Adding webcam images on the slides
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w - ws:w] = imgSmall

    cv2.imshow("image", img)
    cv2.imshow("slides", imgCurrent)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
from sre_constants import SUCCESS
import cv2
import os

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

while True:
    # import images

    success, img = cap.read()
    cv2.imshow("image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
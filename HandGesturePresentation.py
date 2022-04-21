from sre_constants import SUCCESS
import cv2

# Variables
width, height = 50, 20 # camera size adjust

#camera setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

while True:
    success, img = cap.read()
    cv2.imshow("image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
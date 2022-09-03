import cv2
import numpy as np

img = cv2.imread("Resources/lambo.png")

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

cv2.imshow("Hor Image", imgHor)
cv2.imshow("Ver Image", imgVer)
cv2.waitKey(0)
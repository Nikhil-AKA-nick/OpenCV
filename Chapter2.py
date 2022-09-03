#Basic Functions

import cv2
import numpy as np


#RGB to Gray image

img = cv2.imread("Resources/naruto.jpg")

imggray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image", imggray)
cv2.waitKey(0)

#BLUR Image

imgblur = cv2.GaussianBlur(imggray, (9,9), 0)

cv2.imshow("Gray Image", imgblur)
cv2.waitKey(0)

#EDGE Detection

imgcanny = cv2.Canny(img, 100,100)
cv2.imshow("Canny Image", imgcanny)
cv2.waitKey(0)

#Dilaiton

kernal =np.ones((5,5), np.uint8)

imgdilation = cv2.dilate(imgcanny, kernal, iterations=1)
cv2.imshow("Dilated Image", imgdilation)
cv2.waitKey(0)

#Erosion

imgeroded = cv2.erode(imgdilation,kernal,iterations=1)
cv2.imshow("Eroded Image",imgeroded)
cv2.waitKey(0)
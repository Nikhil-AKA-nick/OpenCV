import cv2
import numpy as np

#IMG RESIZE

img = cv2.imread("Resources/lambo.png")
print(img.shape)

imgResize = cv2.resize(img,(560,400))
print(imgResize.shape)

cv2.imshow("Image", img)
# cv2.imshow("Image Resize", imgResize)
# cv2.waitKey(0)

#CROPPING IMAGE

imgcropped = img[0:240,0:400]
cv2.imshow("Cropped Image", imgcropped)
cv2.waitKey(0)
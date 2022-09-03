import cv2
import numpy as np

#SHAPES AND TEXT

img = np.zeros((512,512,3),np.uint8)
print(img.shape)

# print(img)
# img[:] = 255,0,0

# cv2.line(img,(0,0),(300,300),(0,255,0),1)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),1)

cv2.rectangle(img,(0,0),(300,350),(0,255,0),1)
# cv2.rectangle(img,(0,0),(300,350),(0,255,0),cv2.FILLED)

cv2.circle(img,(300,150),100,(255,255,0),2)

cv2.putText(img,"NIKHIL",(100,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
cv2.imshow("Image",img)
cv2.waitKey(0)
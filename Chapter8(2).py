import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 50 :
            cv2.drawContours(imgContour, cnt, -1,(255,0,0),2) #-1 because we want all cnt to print 2 is thickness
            peri = cv2.arcLength(cnt, True)     # True because it is close
            # print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)  #finds no of coutour/vertex
            print(len(approx))
            objCorner = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            if objCorner == 3:
                objectType = "Tri"
            else:
                objectType = "None"

            cv2.rectangle(imgContour, (x,y),(x+w, y+h),(0,0,255),1)
            cv2.putText(imgContour, objectType, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 2)

path = "X:\OpenCV\OpenCVpython\Resources 1\shapes.png"
img = cv2.imread(path)
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur, 50, 50)

cv2.imshow("Original", img)
cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny", imgCanny)

getContours(imgCanny)
cv2.imshow("Contour", imgContour)

cv2.waitKey(0)
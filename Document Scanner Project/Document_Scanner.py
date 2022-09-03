import cv2
import numpy as np

################################
widthImg = 400
heightImg = 300
#################################

cap = cv2.VideoCapture(0)
cap.set(3,widthImg)
cap.set(4,heightImg)
cap.set(10,150)

def preProcessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernel = np.ones((5,5,))
    imgDila = cv2.dilate(imgCanny,kernel,iterations=2)
    imgTresh = cv2.erode(imgDila,kernel,iterations=1)
    cv2.imshow("Gray",imgGray)
    cv2.imshow("Blur",imgBlur)
    cv2.imshow("Canny",imgCanny)
    cv2.imshow("Dila",imgDila)
    return imgTresh


while True:
    success, img = cap.read()
    img = cv2.resize(img,(widthImg,heightImg))
    imgTresh = preProcessing(img)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
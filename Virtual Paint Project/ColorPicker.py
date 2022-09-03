import cv2
import numpy as np

framewidth = 400
frameheight = 300

cap = cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(10,150)

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",480,240)
cv2.createTrackbar("Hue Min","HSV",173,179,empty)
cv2.createTrackbar("Sat Min","HSV",66,255,empty)
cv2.createTrackbar("Val Min","HSV",62,255,empty)
cv2.createTrackbar("Hue Max","HSV",179,179,empty)
cv2.createTrackbar("Sat Max","HSV",255,255,empty)
cv2.createTrackbar("Val Max","HSV",255,255,empty)

while True:
    _,img = cap.read()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min","HSV")
    h_max = cv2.getTrackbarPos("Hue Max","HSV")
    s_min = cv2.getTrackbarPos("Sat Min","HSV")
    s_max = cv2.getTrackbarPos("Sat Max","HSV")
    v_min = cv2.getTrackbarPos("Val Min","HSV")
    v_max = cv2.getTrackbarPos("Val Max","HSV")
    print(h_min)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    # cv2.imshow("Original",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",result)

    if cv2.waitKey(1) and 0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
import cv2
framewidth = 640
frameheight = 480
platecascade = cv2.CascadeClassifier("Cascade/haarcascade_russian_plate_number.xml")

cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10,150)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberplates = platecascade.detectMultiScale(imgGray, 1.1, 4)
    for (x,y,w,h) in numberplates:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
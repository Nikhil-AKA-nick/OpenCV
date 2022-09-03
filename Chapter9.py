import cv2

facecascade = cv2.CascadeClassifier("Resources 1/haarcascade_frontalface_default.xml")
img = cv2.imread("Resources 1/lena.png")

# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Videos", img)
#     if cv2.waitKey(10) & 0xFF == ord("q"):
#         break


imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = facecascade.detectMultiScale(imgGray,1.1,4)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Image",img)
cv2.waitKey(0)

import cv2

GREEN = (0,255,0)

faces = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
image = cv2.imread("físicos.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
detections = faces.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=6)

for (x, y, w, h) in detections:
    cv2.rectangle(image, (x,y), (x+w,y+h), GREEN, 2)

cv2.imshow("output", image)
cv2.waitKey(0)
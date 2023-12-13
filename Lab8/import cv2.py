import cv2
# de pe imagine

face_cascade = cv2.CascadeClassifier(r'C:\Users\Bianca\Downloads\haarcascade_frontalface_default (3).xml')

img = cv2.imread(r'C:\Users\Bianca\Desktop\OIP.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (225,0,0),2)

#display the output
cv2.imshow('img', img)
cv2.waitKey()
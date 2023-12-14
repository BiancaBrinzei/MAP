#de pe web
import cv2
import keyboard

face_cascade = cv2.CascadeClassifier(r'C:\Users\Bianca\Downloads\haarcascade_frontalface_default (3).xml')

cap=cv2.VideoCapture(0)

#cap = cv2.VideoCapture('C:\Users\X-IT\Desktop\')

while not keyboard.is_pressed('esc'):
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+y, y+h), (225,0,0),2)

        cv2.imshow('img', img)

        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
cap.release()
import cv2
import numpy as np


'''
This part is just to see how to capture video from 
Webcam and show it to you
cap = cv2.VideoCapture(0)

cap.set(3,640)  #width
cap.set(4,480)  #height
cap.set(10,100) #brightness

while True:
    success, img = cap.read()
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''

img = cv2.imread("D:\Github\python\emilia_small.jpg")
kernal = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,150,100)
imgDilation = cv2.dilate(imgCanny,kernal,iterations=1)
imgEroded = cv2.erode(imgDilation,kernal,iterations=1)

##resizing and cropping
height, length, channels = img.shape
imgResize = cv2.resize(img,(600,400))
#cv2.imshow('resized',imgResize)
imgCropped = imgResize[:int(height/2),:int(length/2)]
cv2.imshow('cropped',imgCropped)

#cv2.imshow("gray",imgGray)
#cv2.imshow("Blur",imgBlur)
#cv2.imshow("Canny",imgCanny)
#cv2.imshow("dilation",imgDilation)
#cv2.imshow("Erode",imgEroded)
cv2.waitKey(0)

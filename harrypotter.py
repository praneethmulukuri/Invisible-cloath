#Importing necessary libraries

import numpy as np
import cv2
import time

#Creating video cature object
cap=cv2.VideoCapture(0)

time.sleep(2)
background=0

#Capturing the background image
for i in range(30):
    ret,background=cap.read()
    cv2.namedWindow ('background', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty ('background', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('background',background)
cv2.destroyAllWindows()

while(cap.isOpened()):
    
    ret,image=cap.read()

    if not ret:
        break
    
    # Converting  BGR to HSV

    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)


    #HSV values
    lower_red=np.array([0,120,70])
    upper_red=np.array([10,255,255])

    mask1=cv2.inRange(hsv,lower_red,upper_red) #Seperating the cloath part

    lower_red=np.array([170,120,70])
    upper_red=np.array([180,255,255])
    mask2=cv2.inRange(hsv,lower_red,upper_red)

    mask1=mask1+mask2

    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)

    mask1=cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8),iterations=1)

    mask2=cv2.bitwise_not(mask1)

    res1=cv2.bitwise_and(background,background,mask=mask1)
    res2=cv2.bitwise_and(image,image,mask=mask2)
    final_output=cv2.addWeighted(res1,1,res2,1,0)


    cv2.namedWindow ('harry', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty ('harry', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('harry',final_output)

    k=cv2.waitKey(5)
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()

import cv2
import numpy as np


import time

cap=cv2.VideoCapture(0)

time.sleep(2)
background = 0

#Capturing the Background .........
for i in range(30):
    ret,background=cap.read()

#While program session begins capturing......
while(cap.isOpened()):
    ret,img=cap.read()

    if not ret:
        break

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)  #Loading the Colour to HSV format......
    

    lower_red=np.array([0,120,70])  #RED COLOUR CODE FROM LEFT 
    upper_red=np.array([10,255,255])

    mask1=cv2.inRange(hsv,lower_red,upper_red) #INPUT AS HSV 

    lower_red=np.array([170,120,70]) #RED COLOR CODE FROM RIGHT 
    upper_red=np.array([180,255,255])


    mask2=cv2.inRange(hsv,lower_red,upper_red) #LOADING


    mask1 = mask1 + mask2 # 1 or anything is = 1 (Bitwise OR)

    
    
    mask1 =cv2.morphologyEx(mask1,cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2) #NOISE REMOVAL FROM IMAGE (CREATE A 3*3 MAtRIX) .
    mask1 =cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8),iterations=1) # SMOOTHNESS OF IMAGE .

    


    
    mask2=cv2.bitwise_not(mask1)
    result1=cv2.bitwise_and(background,background,mask=mask1) # Segmentation on colour from rest background
    result2=cv2.bitwise_and(img,img,mask=mask2)  # Used to substitute of invisiblity part.

    
    
    final_output=cv2.addWeighted(result1,1,result2,1,0)  #linearly adding or super-imposing 2 images.
    cv2.imshow('INVISIBLE MAN  !',final_output)
    k=cv2.waitKey(10)
    if(k==27):  #Escape key 
        break
    




cap.release() #Destroy the object cap.
cv2.destroyAllWindows() #Destroy all windows
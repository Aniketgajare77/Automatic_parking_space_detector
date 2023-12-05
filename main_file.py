
import cv2
import pickle
import cvzone
import numpy as np

cap=cv2.VideoCapture(r'C:\AL_DL\Automatic space detector\large parking space.mp4')

width ,height = 35 , 16

with open('CarParkPos1','rb')as f:
            posList=pickle.load(f)


def checkParkingSpace(imgpro):
       spaceCounter=0
       for pos in posList:
            
            x,y=pos
            imgCrop= imgpro[y:y+height , x:x+width]
            #cv2.imshow(str(x*y),imgCrop)
            count=cv2.countNonZero(imgCrop)
            cvzone.putTextRect(img,str(count),(x,y+height-3),scale=0.3,thickness=1,offset=0)

            if count <150:
                color=(0,255,0)
                thickness=1
                spaceCounter+=1
            else:
                color=(0,0,255)
                thickness=1
            cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),color,thickness)

       cvzone.putTextRect(img,f'FREE : {spaceCounter}/{len(posList)}',(100,50),scale=2,thickness=3,offset=10,colorR=(0,255,0))
         
       
    
while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES)== cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    
    sucess ,img=cap.read()
    img=cv2.resize(img,(1000,600))
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.GaussianBlur(imgGray,(3,3),1)
    imgThreshold=cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY_INV,25,16)
    imgMedian=cv2.medianBlur(imgThreshold,5)
    kernal=np.ones((3,3), np.int8)
    imgDilate=cv2.dilate(imgMedian,kernal,iterations=1)
    checkParkingSpace(imgDilate)

    
          
          


    cv2.imshow('img',img)
    #cv2.imshow('imgthersh',imgDilate)

    if cv2.waitKey(1) == 27:
        break
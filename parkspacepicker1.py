import cv2
import pickle

width ,height = 35 , 16

try:

    with open('CarParkPos1','rb')as f:
            posList=pickle.load(f)
except:

    posList=[]

def mouseClick(events,x,y,flags,param):
    if events==cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    elif events==cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
            x1,y1=pos
            if x1< x <x1+width and y1 < y < y1+height:
                posList.pop(i)
    with open('CarParkPos1','wb')as f:
        pickle.dump(posList,f)



while True:
    
    img = cv2.imread(r'C:\AL_DL\Automatic space detector\large parkin space.png')
    img=cv2.resize(img,(1000,600))
    #cv2.rectangle(img,(44,250),(81,269),(255,0,255),2)
    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)

    cv2.imshow('img', img)
    cv2.setMouseCallback("img", mouseClick)
    if cv2.waitKey(1) == 27:  # Press 'Esc' key to exit the loop
        break

cv2.destroyAllWindows()

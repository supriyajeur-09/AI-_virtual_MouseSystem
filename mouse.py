import cv2
import numpy as np
import time
import HandTracking as ht
import autopy
import pyautogui
####################
width=648
height=480
smoothening= 7
frameR=100 #frame Reduction

pTime=0
plocx,plocy=0,0
clocx,clocy=0,0

Wscr,hscr=autopy.screen.size()
print(Wscr,hscr)

cap=cv2.VideoCapture(0)

cap.set(3,width)
cap.set(4,height)

detector=ht.handDetector(maxHands=1)

while True:
    fingers=[0,0,0,0,0]
    success, img=cap.read()
    img=detector.findHands(img)
    lmList,bbox=detector.findPosition(img)

    if len(lmList)!=0:
        x1,y1=lmList[8][1:]
        x2,y2=lmList[12][1:]
        #print(x1,y1,x2,y2)

        fingers=detector.fingersUp()
        #print(fingers)

        #convert coordinator
        cv2.rectangle(img, (frameR,frameR), (width - frameR, height - frameR), (255,0,255),2)
        
        #only index up
        if fingers[1]==1 and fingers[2]==0:
               
            x3=np.interp(x1,(frameR,width-frameR),(0,Wscr))
            y3=np.interp(y1,(frameR,height-frameR),(0,hscr))
            
            #smoothen the value
            clocx=plocx+(x3-plocx)/smoothening
            clocy=plocy+(y3-plocy)/smoothening

            #mouse move
            autopy.mouse.move(Wscr-clocx,clocy)
            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
            plocx,plocy=clocx,clocy
        
        

        
        #both fingers are up 
        if fingers[1]==1 and fingers[2]==1:

            length,img,lineInfo =detector.findDistance(8,12,img)
            # print(length)

            if length<20:
                cv2.circle(img,(lineInfo[4],lineInfo[5]),15,(0,255,0),cv2.FILLED)

                # pyautogui.click()
                autopy.mouse.click()
                #pyautogui.click(button='right')
        
        
        #three fingers are up for right click
        if fingers[1]==1 and fingers[2]==1 and fingers[3]==1 and fingers[4]== 0:
            
            cv2.circle(img,(x1,y1),15,(215,25,240),cv2.FILLED)
            pyautogui.click(button='right')
            
        
        #four fingers are up for scroll
        if fingers[1]==1 and fingers[2]==1 and fingers[3]==1 and fingers[4]==1 :
            lexy,img,lineInfo =detector.findDistance(8,12,img)
            
            if lexy<40:
              cv2.circle(img,(x1,y1),15,(22,25,24),cv2.FILLED)
              pyautogui.scroll(-50)
            
            else:
              cv2.circle(img,(x1,y1),15,(22,25,24),cv2.FILLED)
              pyautogui.scroll(50)
            
        
            
          
        
    #frame rate
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img, str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0),3)
    
    
    cv2.imshow("Image", img)
    cv2.waitKey(1) 

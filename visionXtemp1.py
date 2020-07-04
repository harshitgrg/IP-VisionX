import cv2
import numpy as np


cap=cv2.VideoCapture('arena.mp4')

while True:
    ret,frame=cap.read()
    if ret == True:
        #frame=cv2.resize(frame,(512,512)) 
        frame = cv2.transpose(frame)
        frame = cv2.flip(frame,1)
        cv2.imshow('initial',frame)
        #print(frame.shape)
        pts1 = np.float32([[39,104],[352,104],[0,640],[352,640]])

        pts2= np.float32([[0,0],[352,0],[0,640],[352,640]])
        per_trans=cv2.getPerspectiveTransform(pts1,pts2)

        frame = cv2.warpPerspective(frame,per_trans,(352,640))
        #cv2.imshow('perspective transformed',frame)
        blur = cv2.GaussianBlur(frame,(3,3),0)
        l_b = np.array([110,150,110])
        u_b = np.array([255,255,255])

        mask = cv2.inRange(frame, l_b, u_b)
        kernal=np.ones((1,1),np.uint8)

        mask=cv2.dilate(mask,kernal,iterations=1)
        res = cv2.bitwise_and(frame, frame, mask=mask)

        #cv2.imshow('mask', mask)
        circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 120, param1=120, param2=9, minRadius=20, maxRadius=110)
        #print(len(circles))
        if circles.all != None:
            #circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                # Draw outer circle
                cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
                # Draw inner circle
                cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
                thiselem = i
                if len(circles[0,:])==0:
                    cv2.putText(frame,'no circles',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                elif len(circles[0,:])==1:
                    cv2.putText(frame,'only one circle',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                if len(circles[0,:])>1:
                    cv2.putText(frame,'more than one',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                    temp=circles[0,:].copy() 
                    #print(len(circles[0,:]))
                    print(temp)
                    print(i)
                    #print((i)+1)


                    #nextelem = temp[temp.index(i)-len(li)+1]
                    #theta=np.arctan((thiselem[1]-nextelem[1])/(thiselem[0]-nextelem[0]))
                    #frame=cv2.putText(frame,str(theta),(nextelem[0],nextelem[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0))
                    

        
        cv2.imshow('result',frame)
        if cv2.waitKey(150) & 0xFF==ord('q'):
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()
import cv2 
import numpy as np 
import imutils 
from PIL import Image
import time

import subprocess
import serial
global frame
flagard=0

ser=serial.Serial('COM6',9600)


def disconnect():
    ser.close()
    
def up():
    
    data = 'w'
    print(data)
    ser.write(b'w')

def down():
    print('s')
    ser.write(b's')
def left():
    print('a')
    ser.write(b'a')
def right():
    print('d')
    ser.write(b'd')
def stop():
    print('q')
    ser.write(b'q')
def clock():
    print('c')
    ser.write(b'c')
def counterclock():
    print('v')
    ser.write(b'v')
def stepsdata(steps):
    print(steps)
    ser.write(steps)





def perspective_bird(frame):
    pts1 = np.float32([[190,0],[430,0],[0,285],[640,285]])

    pts2= np.float32([[0,0],[639,0],[0,477],[639,477]])

    per_trans=cv2.getPerspectiveTransform(pts1,pts2)

    perspective = cv2.warpPerspective(frame,per_trans,(639,477))
    #cv2.imshow('perspective',perspective)
    perspective=cv2.resize(perspective,(305,665))
    #cv2.imshow('reshape',perspective)
    return perspective



def hought(frame):
    
    #global i
    frame = cv2.medianBlur(frame,5)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("check",frame)
    #cv2.waitKey(0)
    global circles
###
#HughCircles Detection TEST  
    try:
        circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,100,
                            param1=45,param2=20,minRadius=70,maxRadius=230) 
        circles = np.uint16(np.around(circles))
        ret,thresh = cv2.threshold(gray,127,255,0)
    
    

 
# calculate moments of binary image
        M = cv2.moments(thresh)
    
    # calculate x,y coordinate of center
        if(M["m00"]!=0):
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        if circles.all != None:
            for i in circles[0,:]:
            # draw the outer circle
                cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
                cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
            #print(i[0])
    except:
        pass
def line_angle(thresh,frame):
    global ar
    ar=[]
    #frame = cv2.medianBlur(frame,5)
    global theta2
    #print(frame.shape)
    y,x,_=frame.shape
    x=int(x/2)
    
    theta2=0
    
    #M = cv2.moments(thresh)
 
# calculate x,y coordinate of center

    try:
        if circles.all != None:
            for i in circles[0,:]:
            # draw the outer circle
                cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
                cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
                
                #cv2.line(frame,(i[0],i[1]),(cX,cY),(0,0,0),2)
                ar.append(i[1])
                #ar[0].sort()
                ar.sort()
                
                l=str(len(ar))
                print(ar)
                
                
                cv2.line(frame,(x,y),(x,int(y/2)),(0,0,0),2)
               
            for i in circles[0,:]:
                if i[1]==ar[len(ar)-1]:
                    cv2.line(frame,(i[0],i[1]),(x,y),(0,255,0),2)
                    theta1=np.arctan((i[0]-x)/(i[1]-y))*180/np.pi
                    steps=abs(theta/1.8)
                    
                    if theta1>10:
                        
                        #dist=(theta1*11.5/2)
                        steps=theta1*3200/360
                        steps=int(steps)
                        steps=str(steps)
                        #steps=str(100)
                        frame=cv2.putText(frame,'Turn Left',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                        # counterclock()
                        print(steps)
                        stepssignal(steps)
                        #time.sleep(0.5)
                        cv2.waitKey(1)
                        return 1
                    
                
                    elif theta1<-10:
                        steps=theta1*3200/360
                        steps=int(steps)
                        steps=str(steps)
                        frame=cv2.putText(frame,'Turn Right',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                        # clock()
                        print(steps)
                        stepssignal(steps)
                        #time.sleep(0.5)
                        cv2.waitKey(1)

                        return 1
                    else:
                        frame=cv2.putText(frame,'Go Straight',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                        #up()
                        distance=math.sqrt((x-i[0])**2+(y-i[1])**2)
                        factor=15/665
                        distancecm=distance*factor
                        #print(distancecm)
                        cameraFactor=41.5/15
                        realDistance=distancecm*cameraFactor
                        #print(realDistance)
                        wheelRadius=2.5
                        angletoturn=(360*realDistance*7)/(2*3*22)
                        #print(angletoturn)
                        steps=angletoturn*16/1.8
                        steps=int(steps)
                        steps=str(steps)
                        #steps=""+steps1
                        
                        print(steps)
                        frame=cv2.putText(frame,'Go Straight',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                        #up()
                        stepssignal(steps)
                        #time.sleep(3)
                        cv2.waitKey(1)
                        #up()
                        return 1

                    
             
    except:
        pass        
    

def shape(frame):
    y,x,_=frame.shape
    x=int(x/2)
    top_left_x=0
    top_left_y=240
    bottom_right_x=700
    bottom_right_y=800
    
    lt=np.array([0,0,0])

    ut=np.array([75,75,75])
    mask=cv2.inRange(frame,lt,ut)
    kernel=np.ones((3,3),np.uint8)

    mask=cv2.erode(mask,kernel)
    contours, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    try:
        
        for cnt in contours:
            M = cv2.moments(cnt)

            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            area=cv2.contourArea(cnt)
            approx=cv2.approxPolyDP(cnt,0.05*cv2.arcLength(cnt,True),True)

            #if area>10:
            cv2.drawContours(frame,[approx],-1,(0,150,150),2)
            cv2.circle(frame,(cx,cy),2,(0,0,255),-1)

            if(cx>47 and cx<313 and cy>132 and cy< 522):
                cv2.line(frame,(x,y),(cx,cy),(0,0,0),2)
            

                if len(approx) == 3:
                    cv2.putText(frame, "Triangle", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (150, 100, 200))
                    return 3

                elif len(approx) == 4:
                    x1 ,y1, w, h = cv2.boundingRect(approx)
                    aspectRatio = float(w)/h
                    print("This is Aspect Ratio"+str(aspectRatio))
                    if aspectRatio >= 0.85 and aspectRatio <= 1.3:
                    
                        cv2.putText(frame, "Square", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (150, 100, 200))
                        return 4
                    else:
                        cv2.putText(frame, "Triangle", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (150, 100, 200))
                        return 3
                else:
                    return 0
                    
                   
    except:
        pass
    cv2.imshow('mask',mask)  

def ROI(frame):
    top_left_x=0
    top_left_y=240
    bottom_right_x=700
    bottom_right_y=800
    cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), 255, 3)

def bluemask(frame):
    lt=np.array([130,145,130])
    ut=np.array([155,165,160])
    mask=cv2.inRange(frame,lt,ut)
    kernel=np.ones((3,3),np.uint8)

    mask=cv2.erode(mask,kernel)
    return mask

    




#cap=cv2.VideoCapture("opencv/visionX/r1_toptrack.mp4")
cap=cv2.VideoCapture(0)

#frame=cv2.imread("opencv/visionX/r1_track_p1.png")
#ret=True
while(True):
    shapeflag=0

    #flagard=0
    ret,frame=cap.read()
    #frame=cv2.transpose(frame)
    #frame=cv2.flip(frame,+1)
    #signal=ord(getch())
    #ROI(frame)
    ser1=ser.readline()
    print(str(ser1)+"arduino")
    

    if ret==True:
        flagard=0
        frame=perspective_bird(frame)
        #frame,flag=houghc()
        #shape()
        mask=bluemask(frame)
        
        flag=shape(frame)
        hought(frame)
        #houghc(mask)
        #ROI(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(gray,127,255,0)
        if(flag == 4 or flag == 3):
            print("Shape Detected")
            if flag == 4:
                cv2.putText(frame,"TURN RIGHT",(10,20), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,50,255),2)
                clock()
            else:
                cv2.putText(frame,"TURN LEFT",(10,20), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,50,255),2)
                counterclock()
            shapeflag=1
        else:
            flagard= line_angle(thresh,frame)
            
        
            
        #print('flag='+str(flagard))
        cv2.imshow("Video",frame)
        if flagard==0 and shapeflag==0:
            
            stepssignal(-800)
            
            

        key=cv2.waitKey(50)

        if key== 27:
            disconnect()
            break

cap.release()
cv2.destroyAllWindows()
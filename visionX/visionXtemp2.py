import cv2 
import numpy as np 
import imutils 
from PIL import Image
#import pyfirmata
#import serial
import bluetooth
from msvcrt import getch
import subprocess
global frame
global flagard
flagard=0


print ("Searching for devices...")
print ("")

nearby_devices = bluetooth.discover_devices()

num = 0
print ("Select your device by entering its coresponding number...")
for i in nearby_devices:
	num+=1
	print (num , ": " , bluetooth.lookup_name( i ))

selection = int(input("> ")) - 1
print ("You have selected "+bluetooth.lookup_name(nearby_devices[selection]))
addr = nearby_devices[selection]
print(addr)
name=bluetooth.lookup_name(nearby_devices[selection])

passkey = "1234" # passkey of the device you want to connect

try:
    port=1
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socket.connect((addr,port))
except bluetooth.btcommon.BluetoothError as err:
    # Error handler
    pass
def disconnect():
    #Close socket connection to device
    socket.close()
    
def up():
    
    data = 'w'
    print(data)
    socket.send(data)

def down():
   
    data = 's'
    socket.send(data)
def left():
  
    data = 'a'
    socket.send(data)
def right():
   
    data = 'd'
    socket.send(data)
def stop():
    data='q'
    socket.send(data)



#port='port name'
#bluetooth=serial.Serial(port, 9600)
#bluetooth.flushInput()


def perspective_bird(frame):
    pts1 = np.float32([[140,125],[530,125],[0,470],[639,477]])

    pts2= np.float32([[0,0],[639,0],[0,477],[639,477]])

    per_trans=cv2.getPerspectiveTransform(pts1,pts2)

    perspective = cv2.warpPerspective(frame,per_trans,(639,477))
    #cv2.imshow('perspective',perspective)
    perspective=cv2.resize(perspective,(375,700))
    #cv2.imshow('reshape',perspective)
    return perspective

def houghc():
    global circles
    flag = 1
    l_b = np.array([30,50,30])
    u_b = np.array([190,200,190])

    mask = cv2.inRange(frame, l_b, u_b)
    kernal=np.ones((1,1),np.uint8)

    mask=cv2.dilate(mask,kernal,iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('mask', mask)
    #cv2.imshow('result',res)

    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 200, param1=100, param2=5, minRadius=56, maxRadius=65)
    # Draw detected circles
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Draw outer circle
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Draw inner circle
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
    #if len(circles[0,:])==0:
    #    flag = 0

    return frame,flag

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
        circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,30,
                            param1=40,param2=25,minRadius=30,maxRadius=70) 
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
                
                #cv2.line(frame,(i[0],i[1]),(cX,cY),(0,0,0),2)
                ar.append(i[1])
                #ar[0].sort()
                ar.sort()
                
                l=str(len(ar))
                print(ar)
                
                #cv2.putText(frame,l,(50,50),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),4)
                cv2.line(frame,(x,y),(x,int(y/2)),(0,0,0),2)
                #if ar[0]==i[1]:
                    #cv2.line(frame,(i[0],i[1]),(x,y),(0,255,0),2)
            
                    


            

                
                #theta1 = np.arctan((thiselem[1]-cY)/(thiselem[0]-cX))
                #theta1*=180/np.pi

                
                #print(theta1)
                #frame=cv2.putText(frame,str(theta1),(thiselem[0],thiselem[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                #if theta1>0:
                #    frame=cv2.putText(frame,'Turn Left',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                    
                
                #else:
                    
                #    frame=cv2.putText(frame,'Turn Right',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
            #print(ar)
            for i in circles[0,:]:
                if i[1]==ar[len(ar)-1]:
                    cv2.line(frame,(i[0],i[1]),(x,y),(0,255,0),2)
                    theta1=np.arctan((i[0]-x)/(i[1]-y))*180/np.pi
                    if theta1>10:
                        frame=cv2.putText(frame,'Turn Left',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                        left()
                        flagard=1
                    
                
                    elif theta1<-10:
                        frame=cv2.putText(frame,'Turn Right',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                        right()
                        flagard=1
                    else:
                        frame=cv2.putText(frame,'Go Straight',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                        up()
                        flagard=1

                    
                #if len(circles)>1:
                #    nextelem = circles[circles.index(i)-len(li)+1]
                #    theta2=np.arctan((cY-nextelem[1])/(cX-nextelem[0]))
                #    theta2=theta2*180/np.pi
                #    print(theta2) 
                #    frame=cv2.putText(frame,str(theta2),(nextelem[0],nextelem[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0))
            
    except:
        pass        
    
    def barcode(): 
        img=cv.imread("opencv/barcode/bcode.jpg")
        height,width,_=img.shape
        im=Image.open('opencv/barcode/bcode.jpg')
        ppi=im.info['dpi']
        print(ppi[0])


        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        #s=cv.Sobel(gray,cv.CV_64f,1,0)
        #cv.imshow("sobel",s)

        a=0
        d=[]
        #can=cv.Canny(gray,100,200)
        edges = cv.Canny(gray,50,150,apertureSize = 3)
        minLineLength = 100
        maxLineGap = 70
        lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)

        for x1,y1,x2,y2 in lines[:,0]:
            
            d.append(x1)
            cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)

        d.sort()
        l=len(d)
        ba=[]
        for i in range(0,l-1):
            if(i%2==0):
                ba.append(d[i+1]-d[i])
        print(ba)

        #   for i in range(0,len(ba)):
        #      ba[i]=(ba[i]/ppi[0])*25.4
        #  print(ba)
        bav=0
        for i in range(0,len(ba)):
            bav=bav+ba[i]
            bav=bav/4
            print(bav)

        s=""
        for i in range(0,len(ba)):
            if ba[i]<=bav:
                ba[i]=0
            if bav< ba[i]:
                ba[i]=1
            s=s+str(ba[i])
        print(s) 






            


        #cv.imwrite('opencv/barcode/houghlines5.jpg',img)
        #i1=cv.imread('opencv/barcode/houghlines5.jpg')
        cv.putText(frame,s,(int(width/2),int(height/2)),cv.FONT_HERSHEY_PLAIN,3,(255,0,0),2)
        #cv.imshow("Edges",i1)



        #cv.imshow("canny",can)



def shape(frame):
    y,x,_=frame.shape
    x=int(x/2)
    top_left_x=47
    top_left_y=132
    bottom_right_x=313
    bottom_right_y=522
    
    lt=np.array([0,0,0])
    ut=np.array([50,50,50])
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
            #x=approx.ravel()[0]
            #y=approx.ravel()[1]
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
                    #print("This is Aspect Ratio"+str(aspectRatio))
                    if aspectRatio >= 0.85 and aspectRatio <= 1.15:
                    
                        cv2.putText(frame, "Square", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (150, 100, 200))
                        return 4
                    else:
                        cv2.putText(frame, "Triangle", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (150, 100, 200))
                        return 3
                else:
                    return 0
                    
                    #else : cv2.putText(frame, "Circle", (200,200), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255))
                #print (len(approx))
            
    except:
        pass
    cv2.imshow('mask',mask)  

def ROI(frame):
    top_left_x=47
    top_left_y=132
    bottom_right_x=313
    bottom_right_y=522
    cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), 255, 3)

    




#cap=cv2.VideoCapture("opencv/visionX/r1_toptrack.mp4")
cap=cv2.VideoCapture("testTrack0.mp4")

#frame=cv2.imread("opencv/visionX/r1_track_p1.png")
#ret=True
while(True):

    flagard=0
    ret,frame=cap.read()
    frame=cv2.transpose(frame)
    frame=cv2.flip(frame,+1)
    #signal=ord(getch())
    

    if ret==True:
        frame=perspective_bird()
        #frame,flag=houghc()
        #shape()
        
        flag=shape(frame)
        hought(frame)
        #ROI(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(gray,127,255,0)
        if(flag == 4 or flag == 3):
            print("Shape Detected")
            if flag == 4:
                cv2.putText(frame,"TURN RIGHT",(10,20), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,50,255),2)
            else:
                cv2.putText(frame,"TURN LEFT",(10,20), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,50,255),2)

        else:
            line_angle(thresh,frame)
            
        
            
        
        cv2.imshow("Video",frame)
        if flagard==0:
            stop()
       

        key=cv2.waitKey(1)

        if key== 27:
            disconnect()
            break

cap.release()
cv2.destroyAllWindows()
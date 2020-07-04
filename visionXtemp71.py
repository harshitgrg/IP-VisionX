
import cv2 
import numpy as np 
import bluetooth

import math
import subprocess
import serial
global frame
import time
flagard=0



global oldtime
# oldtime=0
oldtime=time.time()
print(oldtime)

global newtime
newtime=0
ser=serial.Serial('COM6',9600)

# print ("Searching for devices...")
# print ("")

# nearby_devices = bluetooth.discover_devices()

# num = 0
# print ("Select your device by entering its coresponding number...")
# for i in nearby_devices:
# 	num+=1
# 	print (num , ": " , bluetooth.lookup_name( i ))

# selection = int(input("> ")) - 1
# print ("You have selected "+bluetooth.lookup_name(nearby_devices[selection]))
# addr = nearby_devices[selection]
# print(addr)
# name=bluetooth.lookup_name(nearby_devices[selection])

# passkey = "1234" # passkey of the device you want to connect

# try:
#     port=1
#     socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#     socket.connect((addr,port))
# except bluetooth.btcommon.BluetoothError as err:
#     # Error handler
#     pass

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






def angle_encoder(steps):
    if steps>0:
        if steps>0 and steps<=100:
            data='a'
        elif steps>100 and steps<=200:
            data='b'
        elif steps>200 and steps<=300:
            data='c'
        elif steps>300 and steps<=400:
            data='d'
        elif steps>400 and steps<=500:
            data='e'
        elif steps>500 and steps<=600:
            data='f'
        elif steps>600 and steps<700:
            data='g'
        elif steps>700 and steps<=800:
            data='h'
        elif steps>800 and steps<=900:
            data='i'
    if steps<0:
        if steps<0 and steps>=-100:
            data='z'
        elif steps<-100 and steps>=-200:
            data='y'
        elif steps<-200 and steps>=-300:
            data='x'
        elif steps<-300 and steps>=-400:
            data='w'
        elif steps<-400 and steps>=-500:
            data='v'
        elif steps<-500 and steps>=-600:
            data='u'
        elif steps<-600 and steps>=-700:
            data='t'
        elif steps<-700 and steps>=-800:
            data='s'
        elif steps<-800 and steps>=-900:
            data='r'
    print(data)
    return data

def encode_straight(steps):
    if steps>=0 and steps<=250:
        data='A'
    elif steps>250 and steps<=500:
        data='B'
    elif steps>500 and steps<=750:
        data='C'
    elif steps>750 and steps<=1000:
        data='D'
    elif steps>1000 and steps<=1250:
        data='E'
    elif steps>1250 and steps<=1500:
        data='F'
    elif steps>1500 and steps<=1750:
        data='G'
    elif steps>1750 and steps<=2000:
        data='H'
    elif steps>2000 and steps<=2250:
        data='I'
    elif steps>2250 and steps<=2500:
        data='J'
    elif steps>2500 and steps<=2750:
        data='K'
    elif steps>2750 and steps<=3000:
        data='L'
    elif steps>3000 and steps<=3250:
        data='M'
    elif steps>3250 and steps<=3500:
        data='N'
    elif steps>3500 and steps<=3750:
        data='O'
    elif steps>3750 and steps<=4000:
        data='P'
    elif steps>4000 and steps<=4250:
        data='Q'
    elif steps>4250 and steps<=4500:
        data='R'
    elif steps>4500 and steps<=5000:
        data='S'
    elif steps>5000 and steps<=5250:
        data='T'
    elif steps>5250 and steps<=5500:
        data='U'
    elif steps>5750 and steps<=6000:
        data='V'
    elif steps>6000 and steps<=6250:
        data='W'
    elif steps>6250 and steps<=6500:
        data='X'
    elif steps>6500 and steps<=7000:
        data='Y'
    elif steps>7000 and steps<=7250:
        data='Z'
    elif steps>7250 and steps<=7500:
        data='.'
    elif steps>7500 and steps<=7750:
        data='_'
    elif steps>7750 and steps<=8000:
        data='-'
    elif steps>8000 and steps<=8250:
        data='@'
    elif steps>8250 and steps<=8500:
        data='~'
    elif steps>8500 and steps<=8750:
        data='!'
    elif steps>8750 and steps<=9000:
        data='#'
    

    return data
def arduino(sig):
    print('sig')
    sig=sig.encode()
    # socket.send(sig)
    ser.write(sig)



    


#port='port name'
#bluetooth=serial.Serial(port, 9600)
#bluetooth.flushInput()


def perspective_bird(frame):
    
   
    pts1 = np.float32([[205,14],[475,14],[20,390],[640,390]])

    pts2= np.float32([[0,0],[639,0],[0,477],[639,477]])


    per_trans=cv2.getPerspectiveTransform(pts1,pts2)

    perspective = cv2.warpPerspective(frame,per_trans,(639,477))

    
    perspective=cv2.resize(perspective,(400,800))
    return perspective

def houghc(frame):
 #global i
    frame = cv2.medianBlur(frame,5)
    gray= frame
    #cv2.imshow("check",frame)
    #cv2.waitKey(0)
    global circles
###
#HughCircles Detection TEST  
    try:
        circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,4,30,
                            param1=40,param2=25,minRadius=30,maxRadius=150) 
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
                cv2.circle(frame,(i[0],i[1]),2,(0,255,0),2)
            # draw the center of the circle
                cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
            #print(i[0])
    except:
        pass
    cv2.imshow('bluecircles',frame)

def contour_circles(frame):
    def nothing(x):
        pass

    cv2.namedWindow("Trackbars")
    cv2.createTrackbar("L-H","Trackbars",54,180,nothing)
    cv2.createTrackbar("L-S","Trackbars",26,255,nothing)
    cv2.createTrackbar("L-V","Trackbars",51,255,nothing)
    cv2.createTrackbar("U-H","Trackbars",99,180,nothing)
    cv2.createTrackbar("U-S","Trackbars",126,255,nothing)
    cv2.createTrackbar("U-V","Trackbars",255,255,nothing)


    font=cv2.FONT_HERSHEY_COMPLEX


    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_h=cv2.getTrackbarPos("L-H","Trackbars")
    l_s=cv2.getTrackbarPos("L-S","Trackbars")
    l_v=cv2.getTrackbarPos("L-V","Trackbars")
    u_h=cv2.getTrackbarPos("U-H","Trackbars")
    u_s=cv2.getTrackbarPos("U-S","Trackbars")
    u_v=cv2.getTrackbarPos("U-V","Trackbars")


    lower_green=np.array([l_h,l_s,l_v])
    upper_green=np.array([u_h,u_s,u_v]) 

    mask=cv2.inRange(hsv,lower_green,upper_green)
    kernel=np.ones((3,3),np.uint8)
    mask=cv2.erode(mask,kernel)
    cv2.imshow('maskcontours',mask)
    contours,hierarchy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    y,x,_=frame.shape
    x=int(x/2)
    centers=[]
    try:
        for cnt in contours:
            M=cv2.moments(cnt)
            
            cx=int(M["m10"])/(M["m00"])
            cy=int(M["m01"])/(M["m00"])
        
            centers.append([cx,cy])
            cv2.circle(frame,(int(cx),int(cy)),7,(0,0,255),-1)
            
            area=cv2.contourArea(cnt)
            approx=cv2.approxPolyDP(cnt,0.001*cv2.arcLength(cnt,True),True)
            
            if area>100:
                if(len(approx)>8 and len(approx)<10000):
                    cv2.drawContours(frame,[approx],0,(0,0,0),3)
                if(len(approx<8) and area<400 ):
                    cv2.drawContours(frame,[approx],0,(0,0,0),3)


                
                if len(approx)<10000 and len(approx)>8:
                    cv2.putText(frame,"Circle",(x,y),font,1,(0,0,0))
                    ar=[]
                    for i in centers: 
                        ar.append(i[0])
                        ar.sort()
                        cv2.line(frame,(int(x),int(y)),(x,int(y/2)),(0,0,0),2)
                    for i in centers:
                        if i[0]==ar[len(ar)-1]:
                            cv2.line(frame,(int(i[0]),int(i[1])),(int(x),int(y)),(0,255,0),2)
                            theta1=-np.arctan((i[0]-x)/(i[1]-y))*180/np.pi
                            print(theta1)
                            if theta1>5:
                                #dist=(theta1*11.5/2)
                                steps=theta1*3200/360
                                steps=int(steps)
                                #steps=str(steps)
                                #steps=str(100)
                                frame=cv2.putText(frame,'Turn Right by '+str(steps),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                                # counterclock()
                                print(str(steps),'right turn')
                                # print(oldtime)
                                newtime=time.time()
                                # if newtime-oldtime>=2:
                                
                                signal=angle_encoder(steps)
                                arduino(signal)
                                #cv2.waitKey(1)
                                # time.sleep(2)
                                # _,frame=cap.read()

                                return 1
                            

                            elif theta1<-5:
                                steps=theta1*3200/360
                                steps=int(steps)
                                #steps=str(steps)
                                frame=cv2.putText(frame,'Turn Left by '+str(steps),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                                # clock()w  
                                print(steps)
                                #stepssignal(steps)
                                newtime=time.time()
                                signal=angle_encoder(steps)
                                print(signal)
                                if newtime-oldtime>=2:
                                
                                   
                                    arduino(signal)
                                    
                                    # oldtime=time.time()
                                # time.sleep(2)
                                # _,frame=cap.read()

                                return 1
                            else :
                                frame=cv2.putText(frame,'Go Straight',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                                #up()
                                distance=math.sqrt((x-i[0])**2+(y-i[1])**2)
                                camerac=29/750
                                anglec=360/(2*3.14*5)
                                stepsc=16/1.8
                                
                                steps=distance*camerac*anglec*stepsc

                                steps+1300
                                print(steps)
                                frame=cv2.putText(frame,'Go Straight',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                                signal=encode_straight(steps)
                                print(signal)
                                # print(oldtime)
                                #stepssignal(steps)
                                newtime=time.time()
                                if(newtime-oldtime>=2):
                                    arduino(signal)
                                    
                                    # oldtime=time.time()

                                
                                return 1

    except ZeroDivisionError:
        pass                         
            
                




   
    return 0



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
        circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,70,param1=20,param2=20,minRadius=140,maxRadius=200) 
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

    # try:
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
            #print(ar)
            
            #cv2.putText(frame,l,(50,50),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),4)
            cv2.line(frame,(x,y),(x,int(y/2)),(0,0,0),2)

        for i in circles[0,:]:
            if i[1]==ar[len(ar)-1]:
                cv2.line(frame,(i[0],i[1]),(x,y),(0,255,0),2)
                theta1=np.arctan((i[0]-x)/(i[1]-y))*180/np.pi
                if theta1>5:
                    #dist=(theta1*11.5/2)
                    steps=theta1*3200/360
                    steps=int(steps)
                    #steps=str(steps)
                    #steps=str(100)
                    frame=cv2.putText(frame,'Turn Right by '+steps,(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                    # counterclock()
                    print(steps)
                    newtime=time.time()
                    if newtime-oldtime>=2:
                       
                        signal=angle_encoder(steps)
                        arduino(signal)
                        oldtime=time.time()
                        #cv2.waitKey(1)
                    # time.sleep(2)
                    # _,frame=cap.read()
                    

                    return 1
                
            
                elif theta1<-5:
                    steps=theta1*3200/360
                    steps=int(steps)
                    #steps=str(steps)
                    frame=cv2.putText(frame,"turn left",(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                    # clock()w  
                    print(steps)
                    #stepssignal(steps)
                    newtime=time.time()
                    if newtime-oldtime>=2:
                        # oldtime=time.time()
                        signal=angle_encoder(steps)
                        arduino(signal)
                    # time.sleep(2)
                    # _,frame=cap.read()

                    return 1
                else :
                    frame=cv2.putText(frame,'Go Straight',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                    #up()
                    distance=math.sqrt((x-i[0])**2+(y-i[1])**2)
                    camerac=29/750
                    anglec=360/(2*3.14*5)
                    stepsc=16/1.8
                    #steps=str(steps)
                    #steps=""+steps1
                    steps=distance*camerac*anglec*stepsc

                    steps+1300
                    print(steps)
                    frame=cv2.putText(frame,'Go Straight',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                    signal=encode_straight(steps)
                    #stepssignal(steps)
                    newtime=time.time()
                    if(newtime-oldtime>=2):
                        arduino(signal)
                        # oldtime=time.time()

                    # time.sleep(2)
                    # 0_,frame=cap.read()
                    #cv2.waitKey(3000)
                    return 1

                
            #if len(circle.s)>1:
            #    nextelem = circles[circles.index(i)-len(li)+1]
            #    theta2=np.arctan((cY-nextelem[1])/(cX-nextelem[0]))
            #    theta2=theta2*180/np.pi
            #    print(theta2) 
            #    frame=cv2.putText(frame,str(theta2),(nextelem[0],nextelem[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0))
        
    # except:
    #     pass        
    
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
    top_left_x=10
    top_left_y=200
    bottom_right_x=300
    bottom_right_y=800
    
    lt=np.array([0,0,0])

    ut=np.array([75,75,75])
    mask=cv2.inRange(frame,lt,ut)
    kernel=np.ones((3,3),np.uint8)

    mask=cv2.erode(mask,kernel)
    contours, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    try:
        theta=0
        
        for cnt in contours:
            M = cv2.moments(cnt)

            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            area=cv2.contourArea(cnt)
            approx=cv2.approxPolyDP(cnt,0.02*cv2.arcLength(cnt,True),True)
            #x=approx.ravel()[0]
            #y=approx.ravel()[1]
            if area>400:
                cv2.drawContours(frame,[approx],-1,(0,150,150),2)
                cv2.circle(frame,(cx,cy),2,(0,0,255),-1)

                if(cx>10 and cx<300 and cy>200 and cy<800 ):
                    cv2.line(frame,(x,y),(cx,cy),(0,0,0),2)
                    cv2.line(frame,(cx,cy),(x,int(y/2)),(0,0,255),-1)
                    theta=np.arctan((cx-x)/(cy-y))*180/np.pi
                    print(theta)
                

                    if len(approx) == 3 and area<410:
                        cv2.putText(frame, "Triangle", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (150, 100, 200))
                        return 3,theta

                    elif len(approx) == 4 and area<410:
                        x1 ,y1, w, h = cv2.boundingRect(approx)
                        aspectRatio = float(w)/h
                        print("This is Aspect Ratio"+str(aspectRatio))
                    
                        
                        cv2.putText(frame, "Square", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (150, 100, 200))
                        return 4,theta
                        
                    else:
                        return 0,theta
                        
                        #else : cv2.putText(frame, "Circle", (200,200), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255))
                    #print (len(approx))
                
    except (TypeError,ZeroDivisionError):
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
cap=cv2.VideoCapture(1)

#frame=cv2.imread("opencv/visionX/r1_track_p1.png")
#ret=True
while(True):

    
    shapeflag=0

    flagard=0
    ret,frame=cap.read()

    #frame=cv2.transpose(frame)
    #frame=cv2.flip(frame,+1)
    #signal=ord(getch())
    #ROI(frame)
    

    if ret==True:
        #frame=cv2.flip(frame,0)
        #print(ser.readline())

        frame=perspective_bird(frame)
        #frame,flag=houghc()
        #shape()
        # mask=bluemask(frame)
        # circle_contour(frame)
        try:
            flag,theta=shape(frame)
        except:
            flag=0
            theta=0
        # flag=contour_circles(frame)
        #hought(frame)
        #houghc(mask)
        #ROI(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # ret,thresh = cv2.threshold(gray,127,255,0)
        if(flag == 4 or flag == 3):
            print("Shape Detected")
            if flag == 4:
                cv2.putText(frame,"TURN RIGHT",(10,20), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,50,255),2)
                if theta>5:
                    
                    steps=theta*(11.5/2)*(360/(2*np.pi*3))*16/1.8
                    
                    newtime=time.time()
                # if newtime-oldtime>=2:
                    oldtime=time.time()
                    signal=angle_encoder(steps)
                    arduino(signal)
                        
                elif theta<-5:
                    steps=theta*(11.5/2)*(360/(2*np.pi*3))*16/1.8
                    # if newtime-oldtime>=2:
                    oldtime=time.time()
                    signal=angle_encoder(steps)
                    arduino(signal)
            else:
                cv2.putText(frame,"TURN LEFT",(10,20), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,50,255),2)
                if theta>5:

                    steps=theta*(11.5/2)*(360/(2*np.pi*3))*16/1.8
                    newtime=time.time()
                    if newtime-oldtime>=2:
                        oldtime=time.time()
                        signal=angle_encoder(steps)
                        arduino(signal)
                elif theta<-5:
                    steps=theta*(11.5/2)*(360/(2*np.pi*3))*16/1.8
                    newtime=time.time()
                    if newtime-oldtime>=2:
                        oldtime=time.time()
                        signal=angle_encoder(steps)
                        arduino(signal)
            shapeflag=1
        else:
            # flagard= line_angle(thresh,frame)
            flagard=contour_circles(frame)
            
        
            
        #print('flag='+str(flagard))
        cv2.imshow("Video",frame)
        print (flagard)
        print(shapeflag)
        if flagard==None and shapeflag==0:
            newtime=time.time()
         
            arduino('D')
            # time.sleep(0.5)
            # ret,frame=cap.read()
        newtime=time.time()   
        #time.sleep(2)
        key=cv2.waitKey(1)
        print('oldtime',str(oldtime))
        print('newtime',str(newtime))

        if key== 27:
            disconnect()
            break

cap.release()
cv2.destroyAllWindows()
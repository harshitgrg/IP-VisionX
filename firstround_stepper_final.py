import cv2
import numpy as np
import bluetooth
import math
import subprocess
import serial
import time
flagard=0
# global frame
global circles
global frame
global oldtime
oldtime=time.time()
global newtime
newtime=time.time()
# newtime=0

################################################################################
# connection
ser=serial.Serial('/dev/ttyUSB0',9600)
# print ("Searching for devices...")
# print ("")

# nearby_devices = bluetooth.discover_devices()



# addr ="FC:A8:9B:00:0F:18"
# print(addr)
# name=bluetooth.lookup_name(addr)

# passkey = "1234" # passkey of HC-05

# try:
#      port=1
#      socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#      socket.connect((addr,port))
# except bluetooth.btcommon.BluetoothError as err:
#     pass

def disconnect():
    #Close socket connection to device
    # socket.close()
    ser.close()

###############################################################################
# encoding approximate steps

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
    print(data,'angular steps')
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
    else:
        data='*'
    
    print(data,'straight steps')
    return data


#################################################################################
# sending signal
def arduino(sig):
    print('sig ',sig)
    # sig=sig.encode()
    # socket.send(sig)
    print('sig ',sig)
    ser.write(sig)




###################################################################################


def perspective_bird(frame):
    
   
    pts1 = np.float32([[205,14],[475,14],[20,390],[640,390]])

    pts2= np.float32([[0,0],[639,0],[0,477],[639,477]])


    per_trans=cv2.getPerspectiveTransform(pts1,pts2)

    perspective = cv2.warpPerspective(frame,per_trans,(639,477))

    
    perspective=cv2.resize(perspective,(400,800))
    return perspective
#########################################################################################
# for circle detecton and contour detection using contours
def nothing(x):
    pass
def contour_circles(frame):
    # frame=cv2.medianBlur(frame,1)
    cv2.imshow('frame2',frame)
    cv2.namedWindow("Trackbars")
    cv2.createTrackbar("L-H","Trackbars",38,180,nothing)
    cv2.createTrackbar("L-S","Trackbars",60 ,255,nothing)
    cv2.createTrackbar("L-V","Trackbars",83,255,nothing)
    cv2.createTrackbar("U-H","Trackbars",152,180,nothing)
    cv2.createTrackbar("U-S","Trackbars",255,255,nothing)
    cv2.createTrackbar("U-V","Trackbars",243,255,nothing)





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
    mask=cv2.erode(mask,kernel,iterations=3)
    mask=cv2.dilate(mask,kernel,iterations=1)
    cv2.imshow('mask_contours',mask)

    contours,hierarchy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    y,x,_=frame.shape
    x=int(x/2)
    centers=[]

    try:
         for cnt in contours:
            M=cv2.moments(cnt)
            
            cx=int(M["m10"])/(M["m00"])
            cy=int(M["m01"])/(M["m00"])

            if cx<400: # for clearance
                centers.append([cx,cy])
            cv2.circle(frame,(int(cx),int(cy)),7,(0,0,255),-1)
            
            area=cv2.contourArea(cnt)
            approx=cv2.approxPolyDP(cnt,0.001*cv2.arcLength(cnt,True),True)

            if area>1000:
                if len(approx)>8:
                    cv2.putText(frame,"Circle",(x,y),font,1,(0,0,0))
                    ar=[]
                    for i in centers: 
                        ar.append(i[0])
                        ar.sort()
                    cv2.line(frame,(int(x),int(y)),(x,int(y/2)),(0,0,0),2)
                    for i in centers:
                        if i[0]==ar[len(ar)-1]:
                            cv2.line(frame,(int(i[0]),int(i[1])),(int(x),int(y)),(0,255,0),2)
                            theta1=np.arctan((i[0]-x)/(y-i[1]))*180/np.pi
                            print(theta1,' theta1')


                            if theta1>5:
                                steps=theta1*3200/360
                                # steps=int(steps)
                                print(steps, 'right turn')
                                # newtime=time.time()
                                signal=angle_encoder(steps)
                                print('newtime set for theta gt 5',newtime)
                                # if time.time()-oldtime>=2:
                                arduino(signal)
                                frame=cv2.putText(frame,"Turn Right",(10,20),cv2.FONT_HERSHEY_COMPLEX,1,(0,50,255),1)
                                
                                
                            

                            elif theta1<-5:
                                steps=theta1*3200/360
                                # steps=int(steps)

                                print(steps,'left turn')
                                # newtime=time.time()
                                print('newtime set for th lt -5 ',newtime)
                                signal=angle_encoder(steps)
                                # if time.time()-oldtime>=2:
                                arduino(signal)
                                frame=cv2.putText(frame,"Turn Left",(10,20),cv2.FONT_HERSHEY_COMPLEX,1,(0,50,255),1)
                            else:
                                distance=math.sqrt((x-i[0])**2+(y-i[1])**2)
                                anglec=360/(2*3.14*5)
                                stepsc=16/1.8
                                
                                distancecm=66.8731-(0.4701*distance)-(0.0041*((distance)**2))+(5.022*(10**-5)*(distance)**3)-(1.2055*(10**-7)*(distance**4))

                                steps=distancecm*anglec*stepsc
                                steps=steps+1000
                                frame=cv2.putText(frame,'Go Straight',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                                signal=encode_straight(steps)
                                # newtime=time.time()
                                print('newtime for straight ',newtime)
                                # if time.time()-oldtime>=2:
                                arduino(signal)
                            return 1,time.time(),contours
                        return 0,oldtime,contours
            cv2.imshow('frame',frame)

    except ZeroDivisionError:
        pass


######################################################################################
# hough circle detection


def hought(frame):
    
    
    frame = cv2.medianBlur(frame,5)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    global circles

    try:
        circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,70,param1=20,param2=20,minRadius=140,maxRadius=200) 
        circles = np.uint16(np.around(circles))
        ret,thresh = cv2.threshold(gray,127,255,0)
    
    

 

       
        if circles.all != None:
            for i in circles[0,:]:
            # draw the outer circle
                cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
                cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
            
    except:
        pass


###################################################################################
# angle detection after hough circle detection

def line_angle(frame):
    ar=[]
    y,x,_=frame.shape
    x=int(x/2)
    if circles.all != None:
        for i in circles[0,:]:
        # draw the outer circle
            cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
            cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
            
            #cv2.line(frame,(i[0],i[1]),(cX,cY),(0,0,0),2)
            ar.append(i[1])
            #ar[0].sort()
            ar.sort()
            
            # l=str(len(ar))
            #print(ar)
            
            #cv2.putText(frame,l,(50,50),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),4)
            cv2.line(frame,(x,y),(x,int(y/2)),(0,0,0),2)

        for i in circles[0,:]:
            if i[1]==ar[len(ar)-1]:
                cv2.line(frame,(i[0],i[1]),(x,y),(0,255,0),2)
                theta1=np.arctan((i[0]-x)/(y-i[1]))*180/np.pi
                if theta1>5:
                    steps=theta1*3200/360
                    # steps=int(steps)
                    print(steps, 'right turn')
                    newtime=time.time()
                    signal=angle_encoder(steps)
                    if time.time()-oldtime>=2:
                            arduino(signal)
                    frame=cv2.putText(frame,"Turn Right",(10,20),cv2.FONT_HERSHEY_COMPLEX,1,(0,50,255),1)
                    
                    
                

                elif theta1<-5:
                    steps=theta1*3200/360
                    # steps=int(steps)

                    print(steps,'left turn')
                    newtime=time.time()
                    signal=angle_encoder(steps)
                    if newtime-oldtime>=2:
                            arduino(signal)
                    frame=cv2.putText(frame,"Turn Left",(10,20),cv2.FONT_HERSHEY_COMPLEX,1,(0,50,255),1)
                
                
                else:
                    distance=math.sqrt((x-i[0])**2+(y-i[1])**2)
                    anglec=360/(2*3.14*5)
                    stepsc=16/1.8
                    
                    distancecm=66.8731-(0.4701*distance)-(0.0041*((distance)**2))+(5.022*(10**-5)*(distance)**3)-(1.2055*(10**-7)*(distance**4))

                    steps=distancecm*anglec*stepsc
                    steps=steps+1000
                    frame=cv2.putText(frame,'Go Straight',(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,50,255),2)
                    signal=encode_straight(steps)
                    if time.time()-oldtime>=2:
                            arduino(signal)
                return 1,time.time()
            return 0,oldtime


def ROIShape():
    top_left_x=0
    top_left_y=240
    bottom_right_x=700
    bottom_right_y=800
    #cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), 255, 3)
    return top_left_x,top_left_y,bottom_right_x,bottom_right_y


def shape():
    y,x,_=frame.shape
    x=int(x/2)
    x1,y1,x2,y2=ROIShape()
    lt=np.array([255,255,255])

    ut=np.array([255,255,255])
    mask=cv2.inRange(frame,lt,ut)
    kernel=np.ones((3,3),np.uint8)

    mask=cv2.erode(mask,kernel)
    # mask using hsv
    # def nothing():
    #     pass
    # cv2.namedWindow("Trackbars")
    # cv2.createTrackbar("L-H","Trackbars",60,180,nothing)
    # cv2.createTrackbar("L-S","Trackbars",77,255,nothing)
    # cv2.createTrackbar("L-V","Trackbars",63,255,nothing)
    # cv2.createTrackbar("U-H","Trackbars",101,180,nothing)
    # cv2.createTrackbar("U-S","Trackbars",206,255,nothing)
    # cv2.createTrackbar("U-V","Trackbars",255,255,nothing)


    # font=cv2.FONT_HERSHEY_COMPLEX


    # hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # l_h=cv2.getTrackbarPos("L-H","Trackbars")
    # l_s=cv2.getTrackbarPos("L-S","Trackbars")
    # l_v=cv2.getTrackbarPos("L-V","Trackbars")
    # u_h=cv2.getTrackbarPos("U-H","Trackbars")
    # u_s=cv2.getTrackbarPos("U-S","Trackbars")
    # u_v=cv2.getTrackbarPos("U-V","Trackbars")


    # lower_green=np.array([l_h,l_s,l_v])
    # upper_green=np.array([u_h,u_s,u_v]) 

    # mask=cv2.inRange(hsv,lower_green,upper_green)
    # kernel=np.ones((3,3),np.uint8)
    # mask=cv2.erode(mask,kernel)
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

                if(cx>x1 and cx<x2 and cy>y1 and cy<y2 ):
                    cv2.line(frame,(x,y),(cx,cy),(0,0,0),2)
                    cv2.line(frame,(cx,cy),(x,int(y/2)),(0,0,255),-1)
                    theta=np.arctan((cx-x)/(y-cy))*180/np.pi
                    print(theta)
                

                    if len(approx) == 3:
                        cv2.putText(frame, "Triangle", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (150, 100, 200))
                        return 3,theta,contours

                    elif len(approx) == 4:
                        x1 ,y1, w, h = cv2.boundingRect(approx)
                        aspectRatio = float(w)/h
                        print("This is Aspect Ratio"+str(aspectRatio))
                    
                        
                        cv2.putText(frame, "Square", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (150, 100, 200))
                        return 4,theta,contours
                        
                    else:
                        return 0,theta,contours
                        
                        #else : cv2.putText(frame, "Circle", (200,200), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255))
                    #print (len(approx))
                
    except (TypeError,ZeroDivisionError):
        pass
        
    cv2.imshow('shapemask',mask)  



cap=cv2.VideoCapture(2)


##########################################################################
# main loop

while True:

    shapeflag=0
    flagard=0

    ret,frame=cap.read()
    

    if ret == True:
        print('oldtime',str(oldtime))
        cv2.imshow('init',frame)
        frame=cv2.medianBlur(frame,7)
        # frame=perspective_bird(frame) #changing perspective
        try:
            flag,theta,contourshapes=shape(frame) # flag value for shape
        except TypeError:
            flag=0
            contourshapes=0
            print('noframe')
        if flag==3 or flag==4:
            print("shape Detected")
            if flag==4:
                cv2.putText(frame,"TURN RIGHT",(10,20), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,50,255),2)
                if theta>5:
                    
                    steps=theta*(11.5/2)*(360/(2*np.pi*3))*16/1.8
                    
                    newtime=time.time()
                    if time.time()-oldtime>=2:
                        oldtime=time.time()
                        signal=angle_encoder(steps)
                        arduino(signal)
                            
                elif theta<-5:
                    steps=theta*(11.5/2)*(360/(2*np.pi*3))*16/1.8
                    if time.time()-oldtime>=2:
                        oldtime=time.time()
                        signal=angle_encoder(steps)
                        arduino(signal)
                else:
                    arduino('I')
                    while len(contourcircle)==0:
                        newtime=time.time()
                        if time.time()-oldtime>=1: ###time interval can be changed as per requirement
                            arduino('y')
                            oldtime=time.time()
                arduino('4')
            else:
                cv2.putText(frame,"TURN LEFT",(10,20), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,50,255),2)
                if theta>5:

                    steps=theta*(11.5/2)*(360/(2*np.pi*3))*16/1.8
                    newtime=time.time()
                    if time.time()-oldtime>=2:
                        oldtime=time.time()
                        signal=angle_encoder(steps)
                        arduino(signal)
                elif theta<-5:
                    steps=theta*(11.5/2)*(360/(2*np.pi*3))*16/1.8
                    newtime=time.time()
                    if time.time()-oldtime>=2:
                        oldtime=time.time()
                        signal=angle_encoder(steps)
                        arduino(signal)
                else:
                    arduino('I')
                    while len(contourcircle)==0:
                        newtime=time.time()
                        if time.time()-oldtime>=1: ###time interval can be changed as per requirement
                            arduino('b')
                            oldtime=time.time()

                        
                arduino('3')
            #############step calculation and shooting remmaining######################
            

            shapeflag=1
        else:
            
            try:
                flagard,oldtime,contourcircle=contour_circles(frame)
            except TypeError:

                flagard=0
                contourcircle=0
                print('abcd')
        # # hought(frame)
            # flagard,oldtime=line_angle(frame)

        cv2.imshow("Video",frame)
        print (flagard,'flagard')
        print(shapeflag,'shapeflag')
        while flagard==None and shapeflag==0:
            newtime=time.time()
         #to be updated ############
            for i in range(1,4):
                if time.time-oldtime>=2:        
                    arduino('y')
                    oldtime=time.time()
                    if(len(contourcircle)==0 and len(contourshapes)==0):
                        continue
                    else:
                        break

            for i in range(1,8):
                if time.time()-oldtime>=2:
                    arduino('b')
                    oldtime=time.time()
                    if (len(contourcircle)==0 and len(contourshapes)==0):
                        continue
                    else:
                        break
            if time.time()-oldtime>=2:
                arduino('G')
                oldtime=time.time()
                
            # time.sleep(0.5)
            # ret,frame=cap.read()
         
        #time.sleep(2)
        key=cv2.waitKey(1)
        
        print('newtime',str(newtime))

        if key== 27:
            disconnect()
            break

cap.release()
cv2.destroyAllWindows()

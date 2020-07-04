im
cap=cv2.VideoCapture(1)

#frame=cv2.imread("opencv/visionX/r1_track_p1.png")
#ret=True
while(True):
    shapeflag=0

    #flagard=0
    ret,frame=cap.read()
    pts1 = np.float32([[190,0],[430,0],[0,285],[640,285]])

    pts2= np.float32([[0,0],[639,0],[0,477],[639,477]])

    per_trans=cv2.getPerspectiveTransform(pts1,pts2)

    perspective = cv2.warpPerspective(frame,per_trans,(639,477))
    #cv2.imshow('perspective',perspective)
    frame=cv2.resize(perspective,(305,665))
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
    #frame=cv2.transpose(frame)
    #frame=cv2.flip(frame,+1)
    #signal=ord(getch())
    #ROI(frame)
    if ret==True:
        flagard=0
        #frame=perspective_bird(frame)
        #frame,flag=houghc()
        #shape()
        mask=bluemask(frame)
        
        flag=shape(frame)
        hought(frame)

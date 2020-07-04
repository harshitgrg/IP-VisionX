import numpy as np 
import cv2

cap=cv2.VideoCapture(1)

#cap = cv2.VideoCapture(0)

while(True):
    try:
        ret, frame = cap.read()
        frame = cv2.medianBlur(frame,5)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("check",frame)
        #cv2.waitKey(0)

    ###
    #HughCircles Detection TEST  
        circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,30,
                            param1=30,param2=40,minRadius=35,maxRadius=300) 
        #circles = np.uint16(np.around(circles))
        ret,thresh = cv2.threshold(gray,127,255,0)

    
    # calculate moments of binary image
        M = cv2.moments(thresh)
    
    # calculate x,y coordinate of center
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        try:
            for i in circles[0,:]:
            # draw the outer circle
                cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
                cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
                cv2.line(frame,(i[0],i[1]),(cX,cY),(0,0,0),2)
        except:
            pass
    #    
    ###
    
    # Display the resulting frame
        
        cv2.imshow('live_hough_circlesq',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except:
        pass
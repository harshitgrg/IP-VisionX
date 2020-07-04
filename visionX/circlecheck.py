import cv2
import numpy as np
cap=cv2.VideoCapture(2)
while True:
    ret,frame=cap.read()
    output=frame.copy()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    try:    
        circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,2,300,minRadius=20,maxRadius=180) 
        circles = np.uint16(np.around(circles))
            # ret,thresh = cv2.threshold(gray,127,255,0)
            
        
        

    
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
            return frame
    except:
        pass
    cv2.imshow('frame',frame)
    key=cv2.waitKey(1)
    if key==27:
        break


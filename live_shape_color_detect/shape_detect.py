import cv2
import numpy as np

def nothing(x):
    pass
cap=cv2.VideoCapture(0)
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H","Trackbars",60,180,nothing)
cv2.createTrackbar("L-S","Trackbars",77,255,nothing)
cv2.createTrackbar("L-V","Trackbars",63,255,nothing)
cv2.createTrackbar("U-H","Trackbars",101,180,nothing)
cv2.createTrackbar("U-S","Trackbars",206,255,nothing)
cv2.createTrackbar("U-V","Trackbars",255,255,nothing)


font=cv2.FONT_HERSHEY_COMPLEX
while True:
    _, frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_h=cv2.getTrackbarPos("L-H","Trackbars")
    l_s=cv2.getTrackbarPos("L-S","Trackbars")
    l_v=cv2.getTrackbarPos("L-V","Trackbars")
    u_h=cv2.getTrackbarPos("U-H","Trackbars")
    u_s=cv2.getTrackbarPos("U-S","Trackbars")
    u_v=cv2.getTrackbarPos("U-V","Trackbars")


    lower_red=np.array([l_h,l_s,l_v])
    upper_red=np.array([u_h,u_s,u_v]) 

    mask=cv2.inRange(hsv,lower_red,upper_red)
    kernel=np.ones((5,5),np.uint8)
    mask=cv2.erode(mask,kernel)

    contours,hierarchy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area=cv2.contourArea(cnt)
        approx=cv2.approxPolyDP(cnt,0.001*cv2.arcLength(cnt,True),True)
        x=approx.ravel()[0]
        y=approx.ravel()[1]
        if area>800:
            cv2.drawContours(frame,[approx],0,(0,0,0),3)
            if len(approx)==3:
                cv2.putText(frame,"Triangle",(x,y),font,1,(0,0,0))
            elif len(approx)==4 :
                cv2.putText(frame,"Rectangle",(x,y),font,1,(0,0,0))
            elif len(approx)==5 :
                cv2.putText(frame,"Pentagon",(x,y),font,1,(0,0,0))
            elif 10<len(approx)<5000:
                cv2.putText(frame,"Circle",(x,y),font,1,(0,0,0))

            
    

    cv2.imshow("Frame",frame)
    frame=cv2.resize(frame,(550,640))
    cv2.imshow("Mask",mask)
    cv2.imshow("Kernel",kernel)

    key=cv2.waitKey(1)
    if key== 27:
        break

cap.release()
cv2.destroyAllWindows()
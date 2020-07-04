import cv2
import numpy as np
def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        #cv2.circle(img,(x,y),100,(255,0,0),-1)
        mouseX,mouseY = x,y
        print(mouseX)
        print(mouseY)

cap=cv2.VideoCapture(1)
def main():
    while True:
        ret,frame=cap.read()
        
        if ret == True:
            #frame=cv2.transpose(frame)
            #frame=cv2.flip(frame,0)
            cv2.imshow('initial',frame)
            cv2.setMouseCallback('initial',draw_circle)
        
            pts1 = np.float32([[213,100],[362,106],[26,456],[522,452]])

            pts2= np.float32([[0,0],[522,0],[0,456],[522,456]])

            per_trans=cv2.getPerspectiveTransform(pts1,pts2)

            perspective = cv2.warpPerspective(frame,per_trans,(522,456))
            #perspective = cv2.imread('wiki.jpg',0)
            cv2.imshow('perspective',perspective)
            #equ = cv2.equalizeHist(perspective)
            #res = np.hstack((perspective,equ)) #stacking images side-by-side
            #cv2.imshow('res.png',res)
            #gray = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
            #cv2.imshow("gray",gray)
            perspective=cv2.resize(perspective,(310,700))
            cv2.imshow('reshape',perspective)
            key= cv2.waitKey(1)
            if(key==27):
                break
main()



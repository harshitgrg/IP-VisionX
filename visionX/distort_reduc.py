import cv2 as cv
import numpy as np 
def cordi(event,x,y,flags,param):
    if(event==cv.EVENT_LBUTTONDBLCLK):
        mouseX,mouseY=x,y
        print(mouseX)
        print(mouseY)



def main():
    cap=cv.VideoCapture("git_workspace/opencv/visionX/visionX/live_feed.mp4")
    while(True):
        ret,frame=cap.read()
        if ret==True:
            frame=cv.resize(frame,(600,600))
            
            cv.imshow("Video",frame)
            cv.setMouseCallback('Video',cordi)
            key=cv.waitKey(1000)
            if(key==27):
                break
main()
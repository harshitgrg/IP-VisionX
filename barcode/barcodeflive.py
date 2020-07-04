import cv2 as cv 
import numpy as np
from PIL import Image
cap=cv.VideoCapture(1)

while(1):
    ret,img=cap.read()
    if ret!=None:
        _,img=cap.read()
        height,width,_=img.shape
        #print(img.shape)
        


        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #s=cv.Sobel(gray,cv.CV_64f,1,0)
    #cv.imshow("sobel",s)

        a=0
        d=[]
    #can=cv.Canny(gray,100,200)
        edges = cv.Canny(gray,50,150,apertureSize = 3)
        minLineLength = 100
        maxLineGap = 70
        lines = cv.HoughLinesP(edges,1,np.pi/180,150)
        
        i=0
        for x1,y1,x2,y2 in lines[:,0]:
            if lines[:,0].all()==None :
                break
            else :
                d.append(x1)
                cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)
            i=i+1


        
        
            

        d.sort()
        l=len(d)
        print(l)
        ba=[]
        for i in range(0,l-1):
            if(i%2==0):
                ba.append(d[i+1]-d[i])
        print(ba)
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






        


        cv.imwrite('opencv/barcode/houghlines5.jpg',img)
        i1=cv.imread('opencv/barcode/houghlines5.jpg')
        cv.putText(i1,s,(int(width/2),int(height/2)),cv.FONT_HERSHEY_PLAIN,3,(255,0,0),2)
        cv.imshow("Edges",i1)


        #cv.imshow("canny",can)
        cv.waitKey(0)
    else : break

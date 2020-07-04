import cv2
import numpy as np


cap=cv2.VideoCapture("barcode.mp4")

def rectangle(frame):
    lb=np.array([0,0,0])
    ub=np.array([65,65,65])
    mask=cv2.inRange(frame,lb,ub)

    kernel=np.ones([3,3],np.uint8)
    mask=cv2.erode(mask,kernel)
    #cv2.imshow('mask',mask)

    res=cv2.bitwise_and(frame,frame,mask=mask)

    (contour, _)= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    try:

        for cnt in contour:
            area=cv2.contourArea(cnt)
            approx=cv2.approxPolyDP(cnt,0.05*cv2.arcLength(cnt,True),True)
            x=approx.ravel()[0]
            y=approx.ravel()[1]
            if area>9000:
                cv2.drawContours(res,[approx],0,(60,120,45))
                if len(approx)==4:
                    x,y,w,h=cv2.boundingRect(cnt)
                    cv2.putText(res,"Rectangle",(x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (12, 20, 100))
                    cv2.rectangle(res,(x,y),(x+w,y+h),(40,45,45))
                    corners=np.array([x,y,w,h])
        return res,corners
    except:
        pass

def contour(cr):

    lb=np.array([0,0,0])
    ub=np.array([65,65,65])
    mask=cv2.inRange(cr,lb,ub)

    kernel=np.ones([3,3],np.uint8)
    mask=cv2.erode(mask,kernel)

    res=cv2.bitwise_and(cr,cr,mask=mask)
    gray=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    thresh= cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    (contours,heirarchy)=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    ar=[]

    #cv2.drawContours(cr, contours, -1, (0,255,0), 2)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        
        approx=cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
        if area>100 and area <10000:
             if len(approx)>0:
                    
                    x,y,w,h=cv2.boundingRect(cnt)
                    #cv2.putText(cr,"Rectangle",(x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (12, 20, 100))
                    cv2.rectangle(cr,(x,y),(x+w,y+h),(200,100,200),2)
                    ar.append([x,y,w,h])
                    
   
    return cr,ar


def barcode(ar):
    l=len(ar)
    arav=0
    #print(ar)

    for i in range(0,l-1):
        arav=arav+ar[i]
    arav=arav/l

    bar=""
    for i in range(0,l):
        if ar[i]<arav:
            bar=bar+"0"
        if ar[i]>arav:
            bar=bar+"1"
    print(bar)
    return bar

def sorting(ar):
    x=[]
    for i in ar:
        x.append(i[0])
    
    x.sort()
    l=len(x)
    #print(x)
    area=[]
    for j in x:
        for i in ar:
        
            if j==i[0]:
                area.append(i[3]*i[2])

    return area
    



def crop(frame,corner):
    #print(corners)
    
    
    x=corner[0]
    y=corner[1]
    w=corner[2]
    h=corner[3]
    cr = frame[y+10:y+h-10,x+10:x+w-10]
    #cv2.imshow('cr',cr)
    return cr




while True:
    ret, frame=cap.read()
    frame=cv2.resize(frame,(640,360))

    cv2.imshow('init',frame)

    try:
        res,corner=rectangle(frame)
        cr=crop(frame,corner)
        #cv2.imshow('res',res)
    except:
        pass

    #try:
    #    cv2.imshow('crop',cr)
    #except:
    #    pass

    boxes,ar=contour(cr)
    cv2.imshow('boxes',boxes)
    
    #print(ar)
    area=sorting(ar)
    bar=barcode(area)
    cv2.putText(frame,bar,(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(200,50,150))
    cv2.imshow('after barcode',frame)

    cv2.waitKey(100)




cv2.destroyAllWindows()
cap.release()
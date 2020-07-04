import cv2
import numpy as np
cap=cv2.VideoCapture('rectangle2.mp4')

def perspective_bird(frame):
    pts1 = np.float32([[50,57],[450,57],[0,200],[512,200]])

    pts2= np.float32([[0,0],[512,0],[0,512],[512,512]])

    per_trans=cv2.getPerspectiveTransform(pts1,pts2)

    perspective = cv2.warpPerspective(frame,per_trans,(512,512))
    #cv2.imshow('perspective',perspective)
    #perspective=cv2.resize(perspective,(350,660))
    #cv2.imshow('reshape',perspective)
    return perspective

def blur(img):
    blu = cv2.GaussianBlur(img,(3,3),0)
    return blu

def blackmask(img):
    lt=np.array([140,115,140])
    ut=np.array([200,160,230])


    mask=cv2.inRange(img,lt,ut)
    kernel=np.ones((3,3),np.uint8)
    mask=cv2.dilate(mask,kernel,iterations=3)
    mask=cv2.erode(mask,kernel,iterations=4)
    return mask

def shape(img,mask):
    y,x,_=img.shape
    x=int(x/2)
    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    try:
        for cnt in contours:
            M=cv2.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            area=cv2.contourArea(cnt)
            approx=cv2.approxPolyDP(cnt,0.05*cv2.arcLength(cnt,True),True)
            cv2.drawContours(img,[approx],-1,(0,150,150),2)
            cv2.circle(img,(cx,cy),2,(0,0,255),-1)
            cv2.line(img,(x,y),(cx,cy),(0,0,0),1)
            if len(approx) == 3:
                cv2.putText(img, "Triangle", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (150, 100, 200))
                return 3

            elif len(approx) == 4:
                x1 ,y1, w, h = cv2.boundingRect(approx)
                aspectRatio = float(w)/h
                print("This is Aspect Ratio"+str(aspectRatio))
                cv2.putText(img, "Square", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (150, 100, 200))
                return 4
                #if aspectRatio >= 0.85 and aspectRatio <= 1.3:
                
                #    cv2.putText(img, "Square", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (150, 100, 200))
                #    return 4
                #else:
                #    cv2.putText(img, "Triangle", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (150, 100, 200))
                #    return 3
            else:
                return 0
        cv2.imshow('contours',img)                
    except:
        print('No Contours')
    
    


while True:
    ret,frame=cap.read()

    if ret==True:
        frame=cv2.resize(frame,(512,512))
        frame=cv2.transpose(frame)
        frame=cv2.flip(frame,+1)
        cv2.imshow('init',frame)
        #persp=perspective_bird(frame)
        #blu=blur(persp)
        blu=blur(frame)
        mask=blackmask(blu)
        cv2.imshow('mask',mask)
        blu=shape(blu,mask)
        cv2.imshow('blu',blu)
        


        key=cv2.waitKey(250)
        if key==27:
            break
    else:
        print('No Source')
        break

cap.release()
cv2.destroyAllWindows()
import numpy as np
import cv2

image=cv2.imread('opencv/barcode/rect.jpg',0)
edges = cv2.Canny(image,50,150,apertureSize = 3)
cv2.imshow("C",edges)
lines = cv2.HoughLines(edges,1,np.pi/180,250) # used to be 200
for rho,theta in lines[:,0]:  
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(image,(x1,y1),(x2,y2),(255,0,255),1)


cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
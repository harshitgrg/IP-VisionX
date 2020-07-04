import cv2
import numpy as np




img = cv2.imread('opencv/hough/circles.jpg', cv2.IMREAD_COLOR)
# Convert to gray-scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 150,param1=100, param2=5, minRadius=0, maxRadius=80)
ret,thresh = cv2.threshold(gray,127,255,0)
 
# calculate moments of binary image
M = cv2.moments(thresh)
 
# calculate x,y coordinate of center
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])
if circles is not None:
    circles = np.uint16(np.around(circles))
    #print(np.dtype(circles))
    for i in circles[0, :]:
        
        cv2.circle(img,(i[0], i[1]), i[2], (0,0,0), 2)
        #circles = cv2.HoughCircles(lur, cv2.HOUGH_GRADIENT, 1, 150, param1=100, param2=5, minRadius=0, maxRadius=0)
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
        cv2.line(img,(i[0],i[1]),(cX,cY),(0,0,0),2)


cv2.imshow('Circles',img)
cv2.waitKey(0)



cv2.destroyAllWindows()
cap.release()
out.release()
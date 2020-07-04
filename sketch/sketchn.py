import numpy as np 
import cv2 as cv

img="opencv/sketch//sketch.jpeg"
def grayscale(gr):
    #return np.dot(rgb[...,:3],[0.299,0.587,0.114])

    return cv.cvtColor(gr,cv.COLOR_BGR2GRAY)

#def dodge(front,back):
    result=front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')


     


s=cv.imread(img)
g=grayscale(s)
g=cv.medianBlur(g,ksize=9)


cv.imwrite('opencv//sketch//sketchf1.jpg',g)
img1=cv.imread("opencv//sketch//sketchf1.jpg")
cv.imshow("Sketch",img1)
cv.waitKey(0)
key=cv.waitKey(1) & 0xFF
if key==ord("q"):
    cv.destroyAllWindows()

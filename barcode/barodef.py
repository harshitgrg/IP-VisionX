import cv2 as cv 
import numpy as np
from PIL import Image


img=cv.imread("opencv/barcode/bcode.jpg")
height,width,_=img.shape
im=Image.open('opencv/barcode/bcode.jpg')
ppi=im.info['dpi']
print(ppi[0])


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#s=cv.Sobel(gray,cv.CV_64f,1,0)
#cv.imshow("sobel",s)

a=0
d=[]
#can=cv.Canny(gray,100,200)
edges = cv.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 70
lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)

for x1,y1,x2,y2 in lines[:,0]:
    
    d.append(x1)
    cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)

d.sort()
l=len(d)
ba=[]
for i in range(0,l-1):
    if(i%2==0):
        ba.append(d[i+1]-d[i])
print(ba)

 #   for i in range(0,len(ba)):
  #      ba[i]=(ba[i]/ppi[0])*25.4
  #  print(ba)
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
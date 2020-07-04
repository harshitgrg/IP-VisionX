from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
#import pygame


ap=argparse.ArgumentParser()
ap.add_argument("-o","--output",type=str,default="result.csv",help="path to csv file")
args=vars(ap.parse_args())

print('[INFO]starting video streaming')
vs=VideoStream(src=1).start()
time.sleep(2.0)

csv=open(args["output"],"w")
found=set()
while True:
    frame=vs.read()
    frame=imutils.resize(frame,width=400)

    barcodes=pyzbar.decode(frame)

    for barcode in barcodes:
        (x,y,w,h)=barcode.rect
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),2)
        barcode_data=barcode.data.decode("utf-8")
        barcode_type=barcode.type

        text="{}".format(barcode_data)
        cv2.putText(frame,text,(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)

        if barcode_data not in found:
            #pygame.mixer.init()
            csv.write("{}\n".format(barcode_data))
            csv.flush()
            found.clear()
            found.add(barcode_data)
    cv2.imshow("BARCODE SCANNER",frame)
    key=cv2.waitKey(1) & 0xFF

    if key==ord("q"):
        break


    

print("[INFO]Closing")
csv.close()
vs.stop()



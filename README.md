# VisionX
This project is created to solve PS of computer vision event in IIT Kharagpur tech-fest.
Team Members: [Pavnesh Chaturvedi](https://github.com/pc-beast), [Harshit Garg](https://github.com/harshitgrg), [Rushil Makkar](https://github.com/rajrushilmakkar)
# Problem Statement
To build a robot that uses an onboard camera to detect a path formed by circles and traverses on it autonomously and is capable of shape detection and barcode reading.

# Algorithm
1. Finding Circle in the video feed.
2. Finding Nearest Circle in case of more than one circle.
3. Aligning of bot in the direction of nearest circle.
4. Calculating steps for the nearest circle.
5. Shooting to the nearest circle.

# Perspective Transform
First thing was to transform perspective to get birds view.
functions used-cv2.getPerspectiveTransform()
               cv2.warpPerspective()

# Circle detection
For circle detection we used two methods-
1.houghcircles() function on colormasked image.
2.Drawing contours over the feed after colormasking.
We tested both the methods on main arena to find which works better.

# Nearest Circle
Indexing of detected circles were creating problem. So to find the nearest circle we stored y-coordinate of all the detected circles in an array the sorted it. After that we compared last element of that array to every element for finding nearest circle.

# Aligning
For aligning in the direction of the nearest circle angle was calculated using basic trigonometery.
After angle was then mapped according to dimensions od bot for calculating exact steps.
These approximate steps were then sent to arduino after encoding them.

# Getting the nearest circle
After aligning in the direction of nearest circle. Distance to the nearest circle is calculated using simple distance formula.
This calclulated distance is then mapped according to the real distance using function calulated function according to the dimensions of the bot. Approximate steps are then calculated and sent to arduino for shooting.

# Shape Detection for turning right or left
Shape Detection is done by using colormasking and drawing contours over color masked image.
If length of the contours list is 3 then it is a triangle and if it is 4 then shape is rectangle.

# Searching Algorithm
If there is no circle in the view then searching algorithm starts working.
Bot turn left in steps till 90 degree and then right 90 dgree and then straight.
This is repeated until circle, shape or stopping point is found.

# Stopping
Another color mask for yellow color is created and if that is detected then bot stops.

# Major Problems and their solutions
### Initial Hardware
Initially we used a dc motor based bor completing the ps.
* 2 DC Motors and wheels
* Arduino Nano
* HC-05 for communication
* Webcam
* Motordriver(L293D IC)
##### Problem 1- Camera View
Since we used houghcircles method for circle detection. Getting birds view is must for that algorithm. Also we needed to restict the perspective so that unnecessary circle which are outside the line can be avoided.
###### Solution
We used perspective transformation to get appropirate view as we wanted.
* Functions used-
```
cv2.getPerspectiveTransform()
cv2.warpPerspective()
```
##### Problem 2- Unnecessary Circles and no Circles
Problem can be caused because of two reasons-
* Incorrect Thresholds of Hough Circles
* Inaccurate Color Mask
###### Solution
* Only solution is to set correct thresholds by trying different ones.
* For color masks, we can try masking in different color spaces to find out which one works better in that lighing conditions. In our case we tried BGR and HSV. HSV worked better. 
### Final Hardware
Main components used-
* Stepper Motor and drivers
* HC-05
* FPV Camera
##### Problem 3- Using Stepper Motors in coordination
Moving both stepper motors was a problem initially. For our first test we used it like DC motor which is against its purpose of moving in steps. it was very slow as it was moving step-by-step as signals passed by python.
###### Solution
Main libraries and functions used-
```
AccelStepper.h
MultiStepper.h
moveTo()
runSpeedToPosition()
```
##### Problem 4- Blocking of Motors
After we found how to use both motors in coordination. Next problem was **blocking** action of *runSpeedToPosition()*.
###### Solution
We passed fakepins in declarations of stepper pins and then mannnually made derection pins high and then reset steps(moving opposite steps using fakepins).
#### Problem 5- Garbage Value in Serial Buffer
Initially we were passing exact steps as a string and receiving as integer by Serial.parseInt(). This was creating a problem of receiving of garbage values sometimes.
###### Solution
We encoded a range of steps to a ascii code and sent to arduino serially. Encoded letter was decoded in arduino and functions were called acoordingly.
#### Problem 6- Overshooting
Continuous calculations for every frame caused overshooting of bot. So it was necessary to stop calculations. We were not able to find out any way for flushing the input buffer in arduino.
So we used three methods for adding delay-
* time.sleep()
* cv2.waitKey()
* empty loops
All three are essentially same things and were freezing the frame for a few moments.
Working to find a more reliable way to flushsh data.
## Workflow & Timeline
# (7-21 Dec):
Learning about OpenCV, detecting shapes and Colours, masking and comparing images. All was smooth on preset images, some problems arised on live video feed, but that was sorted using smoothing functions and different noise reducing functions.
visionXtemp1.py is the corresponding python file regarding this. <br />

There was a lot of time given to software part initially. 

# (21-23 Dec):
Now, motion test using prerecorded video of coins and circle for angle check was done. Simple code(opencv only) for it was written for the video coins.mp4 printing 'Turn Left' or 'Turn Right' using the angle determined as explained above.
# Problems:
Major error occurred was TypeError because of None frame passed. It was resolved using simple Try and Except statements.
At this stage perspective correction was not done as the video shot was in the top view itself. <br /> 
Corresponding code: visionx.py (Major functions: line_angle,hought and shape. Upto here, thresholding was done using altering values.
# (24 Dec-26 Dec):
Hardware testing without any camera was done. Simple ardiono code for L293D motor driver and serial communication (wired) was setup. <br />
For the video source, camera being used was an android phone. 
# Problems faced:
Even when trying to hold the camera still by hands, it would cause problems because it wasnt mounted and thus wasnt a robust method to do so. The actual communication also faced problems because of the mismatch of fps rate of phone's camera and Python's Code.
# Solution:
The fps problem was solved using delays in python, and setting a stable rate in phone's camera itself. <br />
A logitech camera was given on 25 december, which solved the feed problem. Now perepective correction could be easily applied.
# (26-29 Dec):
# Software part: 
The code was updated according to the camera, images were smoothened and arduino code was written (visionxard(1-7).ino) and visionxtemp(1-6).py <br />
Now we were testing on actual arena, however because of the conditions, it was missing some circles, and sometimes detecting some incorrect shapes. We were using houghcircles until then. <br />
The algoritm was same, with two circles in one frame. <br />
Now the final integrated code with above mentioned fucntionalities was in testing mode.<br /> 

# Hardware Part:
Because of connection issues, we were facing problems in motor driver, but it was sorted by using a soldered pcb. Also the speed was slow becuase we were driving the motors using the 5V. <br />

# (30 Dec-3 Jan)
We were thinking a possible solution for barcode problem. There were some must changes we needed in the PS to complete it, and it was mentioned to Robotix Team of IIT Kgp. PS was changed accordingly.<br /> 
During this period, we also modified our basic DC Motors fitted hardware, and tested it. Problems are mentioned above and the solution specified. <br />
A solution to barcode problem was made. (In the barcode folder of this repo) <br />
# (3-5 Jan)
The making of final hardware was started. 2 PCB's of the final hardware were soldered in this period. <br />
We also viewed basic stepper code for motion as mentioned above. The problems faced are already mentioned.<br />
# (5-9 Jan)
Testing of code, integration. We were also facing issues in signal sending and receiving. The motion was jittery and non-continuous.
Using AccelStepper library solved  and gave some problems. <br />
# (10 Jan-13 Jan)
FPV Camera was given. Trying everything again of camera raised some problems. Including fish-eye problem. <br />
Ultimately final mapping for step calculation was done on 13 evening. Arduino code for stepper was modified during this period. <br /> 
Serial buffer problem and signal problem was solved upto some extent. Rest was done in Kharagpur itself.



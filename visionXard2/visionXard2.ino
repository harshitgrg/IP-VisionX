#include<Stepper.h>
#define steppr 200
#define rstep 2
#define rdir 3
#define rms1 4
#define rms2 5
#define renb 6
#define lstep 7
#define ldir 8
#define lms1 9
#define lms2 10
#define lenb 11
#define led 12
#define Speed 60
char sig;
int steps;

Stepper rstepper(steppr,rstep,rdir,rms1,rms2);
Stepper lstepper(steppr,lstep,ldir,lms1,lms2);

#define posD 1
#define negD -1


void setup() {
  // put your setup code here, to run once:
  pinMode(renb,OUTPUT);
  pinMode(lenb,OUTPUT);
  digitalWrite(renb,HIGH);
  digitalWrite(lenb,HIGH);

  Serial.begin(115200);
  Serial.println("Starting");

}



void loop() {
  // put your main code here, to run repeatedly:
  rstepper.setSpeed(Speed);
  lstepper.setSpeed(Speed);
  while(Serial.available()!=0)
  {
    sig=Serial.read();
    if(sig=='w')
    {
      forward();
    }
    else if(sig=='s')
    {
      backward();
      
    }
    else if(sig == 'a')
    {
      left();
      
    }
    else if(sig=='d')
    {
      right();
      
    }
    else if(sig=='c')
    {
      clockwise();
      
    }
    else if (sig == 'v')
    {
      anticlockwise();
    }
    else
    {
      stopping();
    }


    
  }
  

}
void forward()
{
  Serial.println("Moving Forward");
  rstepper.step(posD);
  lstepper.step(negD);
  
}
void backward()
{
  Serial.println("Moving Backward");
  rstepper.step(negD);
  lstepper.step(posD);
}
void right()
{
 Serial.println("Turning Right");
 lstepper.step(negD); 
}
void left()
{
  Serial.println("Turning Left");
  rstepper.step(posD);
  
}
void clockwise()
{
  Serial.println("Clockwise");
  delay(500);
  steps=Serial.read();
  rstepper.step(steps);
  lstepper.step(steps);
  
}
void anticlockwise()
{
  Serial.println("Counter Clockwise");
  delay(500);
  steps=Serial.read();
  
  rstepper.step(steps);
  lstepper.step(steps);
}
void stopping()
{
  Serial.println("Stopping");
}

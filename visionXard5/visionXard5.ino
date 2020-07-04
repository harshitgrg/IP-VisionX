#include <AccelStepper.h>
#include <MultiStepper.h>

#define rstep 6
#define lstep 10
#define rdir 5
#define ldir 11
//String steps1;
//int steps;
char sig;
int dist;
String steps1;
int steps;
long positions[2];
#define rfake 7
#define lfake 8
AccelStepper rstepper(AccelStepper::FULL2WIRE,rstep,rfake);
AccelStepper lstepper(AccelStepper::FULL2WIRE,lstep,lfake);
MultiStepper steppers;
void setup() {
  // put your setup code here, to run once:
  pinMode(rstep,OUTPUT);
  pinMode(rdir,OUTPUT);
  pinMode(lstep,OUTPUT);
  pinMode(ldir,OUTPUT);
  Serial.begin(9600);
  Serial.println("Started");
  steppers.addStepper(rstepper);
  steppers.addStepper(lstepper);
  rstepper.setMaxSpeed(10000);
  lstepper.setMaxSpeed(10000);
  Serial.println("Starting");
}
void loop()
{
   Serial.println("Starting");
   while(Serial.available()!=0)
  {
      
    steps1=Serial.readStringUntil('\n');
    //steps1=steps1.decode("utf-16");
    
    steps=steps1.toInt();
    Serial.println(steps);
    if(steps>=1000 && steps<=1000)
    {
    forward();
    break;
    }
    else if(steps>0 && steps<1000)
    {
      Serial.println("left");
      clockwise();
      break;
      
    }
    else if (steps<0 && steps>-1000)
    {
      Serial.println("right");
      anticlockwise();
      break;
    }
    else if (steps<-10000)
    {
      
    }
  }
}
void forward()
{
  Serial.println(rstepper.currentPosition());
  digitalWrite(rdir,LOW);
  digitalWrite(ldir,HIGH);
  positions[0] = steps;
  positions[1] = steps;
  steppers.moveTo(positions);
  steppers.runSpeedToPosition(); // Blocks until all are in position
  
  delay(10);
  resetsteps();

  
  
}
void clockwise()
{
  Serial.println(rstepper.currentPosition());
  digitalWrite(rdir,HIGH);
  digitalWrite(ldir,HIGH);
  positions[0] = steps;
  positions[1] = steps;
  steppers.moveTo(positions);
  steppers.runSpeedToPosition();
}
void anticlockwise()
{
  Serial.println(rstepper.currentPosition());
  digitalWrite(rdir,LOW);
  digitalWrite(ldir,LOW);
  positions[0] = steps;
  positions[1] = steps;
  steppers.moveTo(positions);
  steppers.runSpeedToPosition();
}
void resetsteps()
{
  positions[0] = 0;
  positions[1] = 0;
  steppers.moveTo(positions);
  steppers.runSpeedToPosition(); // Blocks until all are in position
  delay(10);
}

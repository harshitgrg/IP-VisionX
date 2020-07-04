#include <AccelStepper.h>
#include <MultiStepper.h>

#define rstep 6
#define lstep 10
#define rdir 5
#define ldir 11
char sig;
int dist;
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
  rstepper.setMaxSpeed(7000);
  lstepper.setMaxSpeed(7000);
  Serial.println("Starting");
}
void loop()
{
  while(Serial.available()!=0)
  {
    sig=Serial.read();
    if (sig=='w')
    {
      forward();
    }
    else if(sig=='s')
    {
      backward();
      
    }
    else if(sig=='c')
    {
      clockwise();
    }
    else if(sig=='v')
    {
      anticlockwise();
    }
    else if (sig=='a')
    {
      right();
      
    }
    else if (sig=='d')
    {
      left();
    }
    else
    {
      stopping();
    }
    
  }
}
void forward()
{
  Serial.println(rstepper.currentPosition());
  digitalWrite(rdir,LOW);
  digitalWrite(ldir,HIGH);
  positions[0] = 50;
  positions[1] = 50;
  steppers.moveTo(positions);
  steppers.runSpeedToPosition(); // Blocks until all are in position
  
  delay(10);
  resetsteps();

  
  
}
void left()
{
  Serial.println(rstepper.currentPosition());
  digitalWrite(rdir,LOW);
  
  positions[0] = 20;
  positions[1] = 20;
  steppers.moveTo(positions);
  steppers.runSpeedToPosition(); // Blocks until all are in position
  delay(10);
  resetsteps();

  
  Serial.println(rstepper.currentPosition());
}
void right()
{
  Serial.println(rstepper.currentPosition());
  digitalWrite(ldir,HIGH);
  
  positions[0] = 20;
  positions[1] = 20;
  steppers.moveTo(positions);
  steppers.runSpeedToPosition(); // Blocks until all are in position
  delay(10);
  resetsteps();

  
  Serial.println(rstepper.currentPosition());
}
void clockwise()
{
  Serial.println(rstepper.currentPosition());
  digitalWrite(rdir,HIGH);
  digitalWrite(ldir,HIGH);
  positions[0] = 10;
  positions[1] = 10;
  steppers.moveTo(positions);
  steppers.runSpeedToPosition(); // Blocks until all are in position
  
  delay(10);
  resetsteps();
}
void anticlockwise()
{
   Serial.println(rstepper.currentPosition());
  digitalWrite(rdir,LOW);
  digitalWrite(ldir,LOW);
  positions[0] = 10;
  positions[1] = 10;
  steppers.moveTo(positions);
  steppers.runSpeedToPosition(); // Blocks until all are in position
  
  delay(10);
  resetsteps();
}
void resetsteps()
{
  positions[0] = 0;
  positions[1] = 0;
  steppers.moveTo(positions);
  steppers.runSpeedToPosition(); // Blocks until all are in position
  delay(10);
}
void backward()
{
    Serial.println(rstepper.currentPosition());
  digitalWrite(rdir,HIGH);
  digitalWrite(ldir,LOW);
  positions[0] = 10;
  positions[1] = 10;
  steppers.moveTo(positions);
  steppers.runSpeedToPosition(); // Blocks until all are in position
  delay(10);
  resetsteps();

 
  Serial.println(rstepper.currentPosition());
}
void moving()
{
  Serial.println(rstepper.currentPosition());
  digitalWrite(rdir,LOW);
  digitalWrite(ldir,HIGH);
  positions[0] = -100;
  positions[1] = -100;
  steppers.moveTo(positions);
  steppers.runSpeedToPosition(); // Blocks until all are in position
  delay(50);
  resetsteps();
}
void stopping()
{
  digitalWrite(lstep,LOW);
  digitalWrite(rstep,LOW);
}

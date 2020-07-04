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
int i=0,j=0,k=0;



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

}

void loop() {
  // put your main code here, to run repeatedly:
  
  while(Serial.available()!=0)
  {
    Serial.println("I'm Up.");
    if(j==0)
    {
    sig=Serial.read();
    Serial.println(sig);
    processSteps(sig);
    }
    
    
  }
  Serial.println("No Signal");

}
void processSteps(char sig)
{
  if( sig>='a' && sig<='z')
  {
    if(sig=='a')
    {
      int steps=50;
      clockwise(steps);
      
    }
    if(sig=='b')
    {
      int steps=150;
      clockwise(steps);
    }
    if(sig=='c')
    {
      int steps=250;
      clockwise(steps);
    }
    if(sig=='d')
    {
      int steps=350;
      clockwise(steps);
    }
    if(sig=='e')
    {
      int steps=450;
      clockwise(steps);
    }
    if(sig=='f')
    {
      int steps=550;
      clockwise(steps);
    }
    if(sig=='g')
    {
      int steps=650;
      clockwise(50);
    }
    if(sig=='h')
    {
      int steps=750;
      clockwise(steps);
    }
    if(sig=='i')
    {
      int steps=850;
      clockwise(steps);
    }
    if(sig=='z')
    {
      int steps=-50;
      anticlockwise(steps);
    }
    if(sig=='y')
    {
      int steps=-150;
      anticlockwise(steps);
    }
    if(sig=='w')
    {
      int steps=-250;
      anticlockwise(steps);
    }
    if(sig=='v')
    {
      int steps=-350;
      anticlockwise(steps);
    }
    if(sig=='u')
    {
      int steps=-450;
      anticlockwise(steps);
    }
    if(sig=='t')
    {
      int steps=-550;
      anticlockwise(steps);
    }
    if(sig=='s')
    {
      int steps=-650;
      anticlockwise(steps);
    }
    if(sig=='r')
    {
      int steps=-750;
      anticlockwise(steps);
    }

    }
  
  else if (sig>='A' && sig <='Z'|| sig=='.' || sig =='~' || sig =='@' ||sig =='_'||sig =='!'||sig =='-'||sig=='#')
  
  {
    if (sig=='A')
    {
      int steps=85;
      straight(steps);
    }
    
    if (sig=='B')
    {
      int steps=85*2;
      straight(steps);
    }
    
    if (sig=='C')
    {
      int steps=85*3;
      straight(steps);
    }
    
    if (sig=='D')
    {
      int steps=85*4;
      straight(steps);
    }
    
    if (sig=='E')
    {
      int steps=85*5;
      straight(steps);
    }
    
    if (sig=='F')
    {
      int steps=85*6;
      straight(steps);
    }
    
    if (sig=='G')
    {
      int steps=85*7;
      straight(steps);
    }
    
    if (sig=='H')
    {
      int steps=85*8;
      straight(steps);
    }
    
    if (sig=='I')
    {
      int steps=85*9;
      straight(steps);
    }
    
    if (sig=='J')
    {
      int steps=85*10;
      straight(steps);
    }
    
    if (sig=='K')
    {
      int steps=85*11;
      straight(steps);
    }
    
    if (sig=='L')
    {
      int steps=85*12;
      straight(steps);
    }
    
    if (sig=='M')
    {
      int steps=85*13;
      straight(steps);
    }
    
    if (sig=='N')
    {
      int steps=85*14;
      straight(steps);
    }
    
    if (sig=='O')
    {
      int steps=85*15;
      straight(steps);
    }
    
    if (sig=='P')
    {
      int steps=85*16;
      straight(steps);
    }
    
    if (sig=='Q')
    {
      int steps=85*17;
      straight(steps);
    }
    
    if (sig=='R')
    {
      int steps=85*18;
      straight(steps);
    }
    
    if (sig=='S')
    {
      int steps=85*19;
      straight(steps);
    }
    
    if (sig=='T')
    {
      int steps=85*20;
      straight(steps);
    }
    
    if (sig=='U')
    {
      int steps=85*21;
      straight(steps);
    }
    
    if (sig=='V')
    {
      int steps=85*22;
      straight(steps);
    }
    
    if (sig=='W')
    {
      int steps=85*23;
      straight(steps);
    }
    
    if (sig=='X')
    {
      int steps=85*24;
      straight(steps);
    }
    
    if (sig=='Y')
    {
      int steps=85*25;
      straight(steps);
    }
    
    if (sig=='Z')
    {
      int steps=85*26;
      straight(steps);
    }
    
    if (sig=='.')
    {
      int steps=85*27;
      straight(steps);
    }
    
    if (sig=='_')
    {
      int steps=85*28;
      straight(steps);
    }
    
    if (sig=='-')
    {
      int steps=85*29;
      straight(steps);
    }
    
    if (sig=='@')
    {
      int steps=85*30;
      straight(steps);
    }
    
    if (sig=='~')
    {
      int steps=85*31;
      straight(steps);
    }
    
    if (sig=='!')
    {
      int steps=85*32;
      straight(steps);
    }
    
    if (sig=='#')
    {
      int steps=85*33;
      straight(steps);
    }
    if(sig=='5')
    {
      resetsteps();
    }
  }
}
void straight(int steps)
{
  Serial.println(rstepper.currentPosition());
  digitalWrite(rdir,LOW);
  digitalWrite(ldir,HIGH);
  j=steps;
  positions[0] = 4;
  positions[1] = 4;
  for(i=1;i<=j/4;i++)
  {
  steppers.moveTo(positions);
  steppers.runSpeedToPosition();
  j=j-4;
  }// Blocks until all are in position
  
  //delay(10);
  resetsteps();
}
void clockwise(int steps)
{
  Serial.println(rstepper.currentPosition());
  digitalWrite(rdir,HIGH);
  digitalWrite(ldir,HIGH);
  j=steps;
  positions[0] = 4;
  positions[1] = 4;
  for(i=1;i<=j/4;i++)
  {
  steppers.moveTo(positions);
  steppers.runSpeedToPosition();
  
  j=j-4;
  }
  resetsteps();
}
void anticlockwise(int steps)
{
  Serial.println(rstepper.currentPosition());
  digitalWrite(rdir,LOW);
  digitalWrite(ldir,LOW);
  j=steps;
  positions[0] = 4;
  positions[1] = 4;
  for(i=1;i<=j/4;i++)
  {
  steppers.moveTo(positions);
  steppers.runSpeedToPosition();
  
  j=j-4;
  }
  resetsteps();
}
void resetsteps()
{
  positions[0] = 0;
  positions[1] = 0;
  steppers.moveTo(positions);
  j=0;
  steppers.runSpeedToPosition(); // Blocks until all are in position
  //
}

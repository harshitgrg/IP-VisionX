#define lm1 9
#define lm2 11
#define rm1 6
#define rm2 5
#define enb 2
#define rspeed 255
#define lspeed 255
char val;


void setup() {
  
  // put your setup code here, to run once:
  //pinMode(enb,OUTPUT);
  pinMode(lm1,OUTPUT);
  pinMode(lm2,OUTPUT);    
  pinMode(rm1,OUTPUT);
  pinMode(rm2,OUTPUT);
  Serial.begin(9600);
//  AT+CLASS=1;
  

}

void loop() {
  // put your main code here, to run repeatedly:
  //digitalWrite(enb,HIGH);
  if(Serial.available() )
  {
    val=Serial.read();
    if(val=='w')
  {
    analogWrite(lm1,lspeed);
    analogWrite(lm2,0);
    analogWrite(rm1,rspeed);
    analogWrite(rm2,0);
    Serial.println("MOVING FORWARD");
  }

 else if(val=='s')
  {
    analogWrite(lm1,0);
    analogWrite(lm2,lspeed);
    analogWrite(rm1,0);
    analogWrite(rm2,rspeed);
    Serial.println("MOVING BACKWARD");
    
  }

 else if(val=='d')
  {
    analogWrite(lm1,0);
    analogWrite(lm2,0);
    analogWrite(rm1,rspeed);
    analogWrite(rm2,0);
    Serial.println("TURNING RIGHT");
    
  }
 else if(val=='a')
  {
    analogWrite(lm1,lspeed);
    analogWrite(lm2,0);
    analogWrite(rm1,0);
    analogWrite(rm2,0);
    Serial.println("TURNING LEFT");
  }

 else if(val=='c')
  {
    analogWrite(lm1,lspeed);
    analogWrite(lm2,0);
    analogWrite(rm1,0);
    analogWrite(rm2,rspeed);
    Serial.println("CLOCKWISE ROTATION");
  }

 else if(val=='v')
  {
    analogWrite(lm1,0);
    analogWrite(lm2,lspeed);
    analogWrite(rm1,rspeed);
    analogWrite(rm2,0);
    Serial.println("COUNTER CLOCKWISE ROTATION");
  }
  
  else if(val=='q')
  {
     analogWrite(lm1,lspeed-100);
    analogWrite(lm2,0);
    analogWrite(rm1,rspeed-100);
    analogWrite(rm2,0); 
  }

 else {
  Serial.println("Nothing is passed");
 }

  
  
  
  }
 /* else
  {
    Serial.println("STOP");
    analogWrite(lm1,0);
    analogWrite(lm2,0);
    analogWrite(rm1,0);
    analogWrite(rm2,0); 
  }*/
}

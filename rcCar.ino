#define lm1 5
#define lm2 6
#define rm1 9
#define rm2 11
#define enb 2
String val;


void setup() {
  
  // put your setup code here, to run once:
  pinMode(enb,OUTPUT);
  pinMode(lm1,OUTPUT);
  pinMode(lm2,OUTPUT);    
  pinMode(rm1,OUTPUT);
  pinMode(rm2,OUTPUT);
  Serial.begin(9600);
  

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(enb,HIGH);
  if(Serial.available() )
  {
    val=Serial.read();
    
  }

  if(val=="w")
  {
    analogWrite(lm1,255);
    analogWrite(lm2,0);
    analogWrite(rm1,255);
    analogWrite(rm2,0);
    Serial.println("MOVING FORWARD");
  }

  if(val=="s")
  {
    analogWrite(lm1,0);
    analogWrite(lm2,255);
    analogWrite(rm1,0);
    analogWrite(rm2,255);
    Serial.println("MOVING BACKWARD");
    
  }

  if(val=="a")
  {
    analogWrite(lm1,0);
    analogWrite(lm2,0);
    analogWrite(rm1,255);
    analogWrite(rm2,0);
    Serial.println("TURNING RIGHT");
    
  }
  if(val=="d")
  {
    analogWrite(lm1,255);
    analogWrite(lm2,0);
    analogWrite(rm1,0);
    analogWrite(rm2,0);
    Serial.println("TURNING LEFT");
  }

  if(val=="c")
  {
    analogWrite(lm1,255);
    analogWrite(lm2,0);
    analogWrite(rm1,0);
    analogWrite(rm2,255);
    Serial.println("CLOCKWISE ROTATION");
  }

  if(val=="v")
  {
    analogWrite(lm1,0);
    analogWrite(lm2,255);
    analogWrite(rm1,255);
    analogWrite(rm2,0);
    Serial.println("COUNTER CLOCKWISE ROTATION");
  }

  else
  {
    analogWrite(lm1,0);
    analogWrite(lm2,0);
    analogWrite(rm1,0);
    analogWrite(rm2,0); 
  }
  
  

}

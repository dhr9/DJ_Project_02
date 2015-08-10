int read_write = 13;
int thousand = 9,hundreds = 0;

void setup() {
  
  Serial.begin(57600);
  pinMode(read_write,OUTPUT);
  digitalWrite(read_write,HIGH);
  
}

void loop() {
  
  if(Serial.available() > 0) {
   
    char data = Serial.read();
    if(data == 'w') {
      
      digitalWrite(read_write,LOW);  
      delay(thousand);
      delayMicroseconds(hundreds);
      digitalWrite(read_write,HIGH);
    }
    else if(data == 't'){
      thousand++;
      Serial.print("t");
    }
    else if(data == 'h'){
      hundreds+=100;
      hundreds%=1000;
      Serial.print("h");
    }
  }
  
}

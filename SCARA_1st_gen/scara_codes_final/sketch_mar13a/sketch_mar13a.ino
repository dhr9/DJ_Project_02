int read_write = 13;

void setup() {
  
  Serial.begin(57600);
  pinMode(read_write,OUTPUT);
  digitalWrite(read_write,HIGH);

}

void loop() {
  
  if(Serial.available() > 0) {
    
    char data = Serial.read();
    if(data == 'p') {
      Serial.write('d');
    }
    if(data == 'q') {
      Serial.write('e'); 
    }
    if(data == 'w') {
      
      digitalWrite(read_write,LOW);
      delay(10);
      delayMicroseconds(1);
      digitalWrite(read_write,HIGH);
    }
  }

}

int read = 13;

void setup() {
  Serial.begin(9600);

}

void loop() {
  while(Serial.available() > 0) {
    int data = Serial.read();
    if(data == '0xaa') {
      digitalWrite(read,HIGH);
    }
    if(data == '0x00') {
      digitalWrite(read,LOW);
    }
  }
  
}




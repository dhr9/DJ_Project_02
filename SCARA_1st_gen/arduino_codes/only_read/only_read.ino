void setup() {
  
  Serial.begin(57600);

}

void loop() {

  if(Serial.available() > 0) {
    
    int data = Serial.read();
    Serial.println(data,HEX);
  
  }

}

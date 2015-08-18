int read_write = 13;
int delay_ = 1000;

void setup() {
  Serial.begin(57600);
  pinMode(read_write,OUTPUT);
  digitalWrite(read_write,HIGH);
}

void loop() {
  if(Serial.available() > 0) {
    char data = Serial.read();
    if(data == '\x02') {
      Serial.write('c');
      //delay_ += 1;
    }
    if(data == '\x01') {
      Serial.write('k');
      digitalWrite(read_write,LOW);
      delay(104);
      //delayMicroseconds(delay_%1000);
      digitalWrite(read_write,HIGH);
    }
  }
}

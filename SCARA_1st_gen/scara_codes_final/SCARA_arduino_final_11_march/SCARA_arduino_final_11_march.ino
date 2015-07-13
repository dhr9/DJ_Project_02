int read_write = 13;
int done = 12345;

void setup() {
  
  Serial.begin(57600);
  pinMode(read_write,OUTPUT);
  digitalWrite(read_write,HIGH);
  
}

void loop() {
  
  if(Serial.available() > 0) {
   
    int data = Serial.read(Serial.available());
    Serial.println(data);
  }
  
}

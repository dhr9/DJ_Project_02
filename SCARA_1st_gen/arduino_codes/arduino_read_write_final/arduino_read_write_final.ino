int read_write = 13;
int done = 12345;

void setup() {
  
  Serial.begin(57600);
  pinMode(read_write,OUTPUT);
  digitalWrite(read_write,HIGH);
  
}

void loop() {
  
  if(Serial.available() > 0) {
   
    char data = Serial.read();
    if(data == 'r') {
      
      digitalWrite(read_write,HIGH);
      
    } 
    if(data == 'w') {
      
      digitalWrite(read_write,LOW);
    }
    
    Serial.write('s');
      
  }
  
}

int en = 2;

void setup() {
  Serial.begin(57600);
  pinMode(en,OUTPUT);
  digitalWrite(en,LOW);
  
}

void loop() {
  if(Serial.available() > 0) {
    char data = Serial.read();
    Serial.println(data);
    if(data == 'w') {
      digitalWrite(en,HIGH);
      Serial.println('going high');
    }
    if(data == 'r') {
       digitalWrite(en,LOW);
       Serial.println('going low');
    }
  }
}

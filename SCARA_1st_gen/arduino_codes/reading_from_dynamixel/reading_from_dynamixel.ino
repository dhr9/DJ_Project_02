int ledPin =  13;    // LED connected to digital pin 13
int i = 0;

byte startAddress,val;
byte servoID= 0x01;
byte ledOn = 0x0F;
byte ledOff = 0x05;

//_____________________________________________________//______________
//%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// Run setup Function
void setup() {
Serial.begin(57600);
//int DEPin= 2; // The pin to be used for enable/disable signal
//digitalWrite(DEPin, HIGH); // tell max485 to transmit
pinMode(2,OUTPUT);
digitalWrite(2,HIGH);

}

//___________________________________________________________________
//%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// Run main Function
void loop() {
//Transmission section
delay(1);
digitalWrite(2,LOW); 
 activateServos(0x01, 0xFD,0x07,0xff,0x03);
  delay(5500);
readServos(0x01);
digitalWrite(2,HIGH);

while(Serial.available()==0)
{}

while(Serial.available())
  {
  val=Serial.read();
  Serial.print("    ");
  Serial.print(val,HEX);
  delay(1);
  }
Serial.println();
delay(10);

digitalWrite(2,LOW);
 activateServos(0x01, 0xFF,0x0F,0xff,0x03);
 delay(5500);
readServos(0x01);
digitalWrite(2,HIGH);

while(Serial.available()==0)
{}

while(Serial.available())
  {
  val=Serial.read();
  Serial.print("    ");
  Serial.print(val,HEX);
  delay(1);
  }
Serial.println();



}

//_____________________________________________________//%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
//Function Definitions
//___________________________________________________________________
//%%%%%%%%%%%%%%%%%%%%%%%%%%%%


void readServos (byte servoID){
  byte checksum_ACK;
  byte notchecksum;
  startAddress = 0X1E;     // Turning on led
   
  checksum_ACK =  servoID + 0x04 + 0x02 + 0x24 + 0x04;
  notchecksum = ~checksum_ACK;
 

 
  delay(5);                 // Allow this to take effect

  Serial.write(byte(0xFF));  // 1.These 2 bytes are 'start message'
  Serial.write(byte(0xFF));  // 2.These 2 bytes are 'start message'
  Serial.write(byte(servoID));  // 3.Address 1 is target servo or 0xfe which is broadcast mode
  Serial.write(byte(0x04));  // 4.Length of string
  Serial.write(byte(0x02));  // 5.Ping read write or syncwrite 0x01,2,3,83
  Serial.write(byte(0x24));
  Serial.write(byte(0x04));
  
  Serial.write(byte(notchecksum)); //8. the notchecksum
  delayMicroseconds(1500);
   // allow last byte to go through
}


void activateServos (byte servoID, byte posl, byte posh, byte movspdl, byte movspdh){
	byte checksum_ACK;
	byte notchecksum; 
	checksum_ACK =  servoID + 0x07 + 0x03 + 0x1E + posl + posh + movspdl + movspdh;
	notchecksum = ~checksum_ACK;
	delay(5);
	Serial.write(byte(0xFF));  
	Serial.write(byte(0xFF));  
	Serial.write(byte(servoID));
	Serial.write(byte(0x07));  
	Serial.write(byte(0x03));  
	Serial.write(byte(0x1E));
	Serial.write(byte(posl));
	Serial.write(byte(posh));
	Serial.write(byte(movspdl));
	Serial.write(byte(movspdh));
	Serial.write(byte(notchecksum));
	delayMicroseconds(1500);
}

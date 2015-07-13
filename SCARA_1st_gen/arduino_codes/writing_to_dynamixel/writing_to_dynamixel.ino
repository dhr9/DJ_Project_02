

#include <Servo.h> 
#include <SoftwareSerial.h>
//all the parameters
  SoftwareSerial mySerial(10, 11); // RX, TX
 
  byte servoID, val, posl,posh,movspdl, movspdh;   //initilize link motors parameters
  byte baseh[70];   // because arduino reads character
  byte linkh[70];
  byte basel[70];
  byte linkl[70];
  int m; //m for reading the serial alphabets,setup,scan right,sacan left, placing
  char mode;  //n for starting the system and and mode for particular sequence of operation
  int si[2]={};
  int ssi;
  int ti[2]={};
  int tti;
  int ci[2]={};
  int cci;
  int ri[2]={};
  int rri;
  char test;
  int k;

//setup of the controller
void setup() {
  Serial.begin(57600);
  mySerial.begin(9600);
  pinMode(2,OUTPUT);

  //Make an array of all the blocks position with higher byte and lower byte for both motor i.e. 4 arrays
  byte baseh[]={};
  byte basel[]={};
  byte linkh[]={};
  byte linkl[]={};
  m=1;
}


void loop(){
  activateServos(0x02, 0x00,0x00,0x90,0x00);
  delay(6500);
  activateServos(0x02, 0xFF,0x0F,0x90,0x00);
  delay(6500);
  
// Some functions that will be useful
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



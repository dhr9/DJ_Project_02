import serial
import time

def startup(com) :
    ser = serial.Serial(port = com)      #create an instance of the serial.Serial class 
    print(ser)
    ser.baudrate = 57600                  #set baudrate equal to 9600
    print(ser.baudrate)
    return ser

arduino =  startup('com7')
dynamixel = startup('com3')

def write(id_ ,position_low,position_high,speed_low,speed_high) :
    checksum = id_ + 0x07 + 0x03 + 0x1e + position_low + position_high +speed_low + speed_high
    not_checksum = (~checksum)&0xff 
    data = '\xff\xff' + chr(id_) + '\x07\x03\x1e' + chr(position_low)+ chr(position_high) + chr(speed_low) + chr(speed_high) + chr(not_checksum)
    arduino.write('r')
    time.sleep(0.1)
    dynamixel.write(data)
    time.sleep(0.1)
    arduino.write('w')
    time.sleep(0.1)
    
def read(id_) :
    checksum = id_ + 0x04 + 0x02 + 0x24 + 0x04
    not_checksum = (~checksum)&0xff
    data = '\xff\xff' + chr(id_) + '\x04\x02\x24\x04' + chr(not_checksum)
    arduino.write('r')
    time.sleep(0.1)
    dynamixel.write(data)
    time.sleep(0.1)
    arduino.write('w')
    time.sleep(0.1)
    

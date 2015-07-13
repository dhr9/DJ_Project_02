'''to communicate with the dynamixel motor via the max485 ic , we need to set up a
    virtual com port and create an instance of the serial.Serial class , so as to
    use it to read data from and write data to the dynamixel
    
    serial<id,open=(true/false)>(port = ?,baudrate = ?,bytesize = ?,parity = 'Y/N',
    stopbits = ?,timeout = ?,xonxoff = (True/False),rtscts = (True/False),dsrdtr =
    (True/False))
'''


##INSTRUCTIONS ABOUT HOW TO USE THIS CODE IS AT THE BOTTOM OF THE CODE 


import time                              #import time liabrary to use the time.sleep()
                                        #function to generate delays
import serial                            #import the serial library
from math import *

def startup(com) :
    ser = serial.Serial(port = com)      #create an instance of the serial.Serial class 
    print(ser)
    ser.baudrate = 57600                 #set baudrate equal to 9600
    print(ser.baudrate)
    return ser

arduino =  startup('com6')
dynamixel = startup('com5')
##dynamixel = startup('/dev/tty.usbserial-A90246TV')
##arduino = startup('/dev/tty.usbmodem1411')
##arduino = startup('/dev/tty.usbmodem1421')


'''
I N S T R U C T I O N   P A C K E T :

the instruction packet for the dynamixel consists of 6 parts :
    part1) initialization :
        you need to tell the dynamixel that you are sending it an instruction packet
        for this , you need to send '0xFF' two times
        
    part2) id of the motor :
        you need to specify the id of the motor in case that more than one motors are
        connected in daisy chain configuration .
        in our case, the two motors that we are using have id's 0x01 and 0x02
        but in general there can be maximum of 254 motors connected in daisy chain
        
    part3) length of the packet :
        it is calculated as the number of parameters + 2
        
    part4)instruction :
        this is the opcode of the instruction (in hexadecimal ofcourse)
        the following are the instructions that can be used with the dynamixel motors :
            instruction 1 :
                PING (0x01) --> NO EXECUTION , IT IS USED WHEN THE CONTROLLER IS READY TO
                RECIEVE THE STATUS PACKAGE
                NUMBER OF PARAMETERS --> 0
            instruction 2 :
                READ_DATA (0x02) --> THIS COMMAND READS DATA FROM THE DYNAMIXEL
                NUMBER OF PARAMETERS --> 2
                    PARAMETER1 ---> START ADDRESS OF DATA TO BE READ
                    PARAMETER2 --> LENGTH OF DATA TO BE READ (IN BYTES) 
            instruction 3 :
                WRITE_DATA(0x03) --> THIS COMMAND WRITES DATA TO DYNAMIXEL
                NUMBER OF PARAMETERS --> 2 OR MORE
                    PARAMETER1 --> START ADDRESS TO WRITE DATA
                    PARAMETE2 --> FIRST DATA TO WRITE
                    PARAMETER3 --> SECOND DATA TO WRITE
                    ...
                    PARAMETERN --> NTH DATA TO WRITE
            instruction 4 :
                REG WRITE (0x04) --> THIS COMMAND IS SIMILAR TO WRITE DATA BUT IT REMAINS
                                     IN THE STANDBY STATE WITHOUT BEING EXECUTED UNTIL
                                     THE ACTION COMMAND IS RECEIVED
                NUMBER OF PARAMETERS --> 2 OR MORE
                    PARAMETER1 --> START ADDRESS TO WRITE DATA
                    PARAMETER2 --> FIRST DATA TO WRITE
                    PARAMETER3 --> SECOND DATA TO WRITE
                    ...
                    PARAMETERN --> NTH DATA TO WRITE
            instruction 5 :
                ACTION (0x05) --> THIS COMMAND INITIATES THE MOTIONS REGISTERED WITH THE
                                  REG WRITE INSTRUCTION
                NUMBER OF PARAMETERS --> 0
            instruction 6 :
                RESET (0x06) --> THIS COMMAND RESTORES THE STATE OF DYNAMIXEL TO FACTORY
                                 SETTINGS
                NUMBER OF PARAMETERS --> 0
            instruction 7 :
                SYNC WRITE (0x83) --> THIS COMMAND IS USED TO CONTROL SEVERAL DYNAMIXELS
                                      AT A TIME
                NUMBER OF PARAMETERS --> 4 OR MORE
                    PARAMETER1 --> START ADDRESS OF DATA TO WRITE
                    PARAMETER2 --> LENGTH OF DATA TO WRITE
                    PARAMETER3 --> FIRST ID
                    PARAMETER4 --> FIRST DATA OF FIRST ID
                    PARAMETER5 --> SECOND DATA OF FIRST ID
                    ...
                    PARAMETERX --> SECOND ID
                    PRAMETERX+1 --> FIRST DATA OF SECOND ID
                    ...
                (IN THE SYNC WRITE INSTRUCTION , THE LENGTH OF THE INSTRUCTION SHOULD
                 NOT EXCEED 143 BYTES , SINCE THE VOLUME OF THE RECEIVING BUFFER IS 143
                 BYTES )
                
    part5)parameters :
        parameter is used when the instruction requires ancillary data

    part6)check sum :
        it is used to check if the packate is damaged using commumication . checksum is
        calculated according to the formula :
            checksum = ~(id + length + instruction + parameter1 + parameter2 + .. + parameterN)
'''

'''

S T A T U S    P A C K E T :

the dynamixel executes command received from the main controller and returns the result
    to the main controller . the returned data is called the status packet .
    the status packet containg of 6 parts :

    part1)identification :
        this signal identifies the beginning of the status packet (0xFF two times)

    part2)id :
        id of the dynamixel motor which transfers the status packet

    part3)length :
        it is the length of the status packet
        it is given as number of parameters + 2

    part4)error byte :
        it displays the error status occured during the operation of the dynamixel
        each bit in the error byte has a meaning and is explained below
            BIT0 INPUT VOLTAGE ERROR --> WHEN THE APPLIED VOLTAGE IS OUT OF RANGE OF
                                         OPERATING VOLTAGE SET IN THE CONTROL TABEL
                                         IT IS SET AS 1
            BIT1 ANGLE LIMIT ERROR --> WHEN THE GOAL POSITION IS WRITTEN OUT OF THE RANGE
                                       FROM THE CW ANGLE LIMIT TO CCW ANGLE LIMIT , IT IS
                                       SET TO 1
            BIT2 OVERHEATING ERROR --> WHEN THE INTERNAL TEMPERATURE OF THE DYNAMIXEL IS
                                       OUT OF RANGE OF THE OPERATING TEMPERATURE SET IN
                                       THE CONTROL TABEL , IT IS SET AS 1
            BIT3 RANGE ERROR --> WHEN A COMMAND IS OUT OF THE RANGE FOR USE , IT IS SET AS 1
            BIT4 CHECKSUM ERROR --> WHEN THE CHECKSUM OF THE TRANSMITTED INSTRUCTION PACKET
                                    IS INCORRECT , IT IS SET AS 1
            BIT5 OVERLOAD ERROR --> WHEN THE CURRENT LOAD CAN NOT BE CONTROLLED BY THE SET
                                    TORQUE , IT IS SET AS 1
            BIT6 INSTRUCTION ERROR --> IN CASE OF SENDING AN UNDEFINED INSTRUCTION OR DELIVERING
                                       THE ACTION COMMAND WITHOUT THE REG_WRITE COMMAND , IT
                                       IS SET AS 1
            BIT7 --> 0

    part5)parameter :
        it is the data except the error
        
    part6)checksum :
        it is used to check if the packet is damaged during communication
        checksum = ~(id + length + error + parameter1 + parameter2 + ...)

'''


def angle_to_hex(angle) :
    angle_ = (angle/360.0)*4095
    print angle_
    higher_byte = int(angle_/256)
    lower_byte = int(angle_%256)
    return[lower_byte,higher_byte]

def write(id_ ,position_low,position_high,speed_low,speed_high) :
    checksum = [id_ , 0x07 , 0x03 , 0x1e , position_low , position_high , speed_low + speed_high]
    __not_checksum__ = not_checksum(checksum) 
    data = '\xff\xff' + chr(id_) + '\x07\x03\x1e' + chr(position_low)+ chr(position_high) + chr(speed_low) + chr(speed_high) + chr(__not_checksum__)
    rw('w')
    time.sleep(0.1)
    dynamixel.write(data)
    time.sleep(0.001)
    rw('r')
    time.sleep(0.00001)
    if(dynamixel.inWaiting() != 0) :
        data = dynamixel.read(dynamixel.inWaiting())
        print(data)
        time.sleep(1)

def dhr_write(id_ ,angle,speed_low,speed_high):
    pos_bytes = angle_to_hex(angle)
    position_low = pos_bytes[0]
    position_high = pos_bytes[1]
    print position_low
    print position_high
    dhr_write1(id_ ,position_low,position_high,speed_low,speed_high)


def dhr_test2():
    dhr_write(0x01,0,0xff,0x03)
    time.sleep(3)
    dhr_write(0x02,0,0xff,0x03)
    time.sleep(3)
    dhr_write(0x01,360,0xff,0x03)
    time.sleep(3)
    dhr_write(0x02,360,0xff,0x03)
    
def  dhr_write1(id_ ,position_low,position_high,speed_low,speed_high):
    checksum = [id_ , 0x07 , 0x03 , 0x1e , position_low , position_high , speed_low , speed_high]
    __not_checksum__ = not_checksum(checksum)

    position_low = chr(position_low)
    position_high = chr(position_high)

    data = '\xff\xff' + chr(id_) + '\x07\x03\x1e' + position_low + position_high + chr(speed_low) + chr(speed_high) + chr(__not_checksum__)
    print list(data)
    rw('w')
    time.sleep(0.001)
    dynamixel.write(data)

def  dhr_write2(id_ ,position_low,position_high,speed_low,speed_high):
    checksum = [id_ , 0x07 , 0x03 , 0x1e , position_low , position_high , speed_low , speed_high]
    __not_checksum__ = not_checksum(checksum)

    data = '\xff\xff' + chr(id_) + '\x07\x03\x1e' + chr(position_low) + chr(position_high) + chr(speed_low) + chr(speed_high) + chr(__not_checksum__)
    print list(data)
    rw('w')
    time.sleep(0.001)
    dynamixel.write(data)


##def  dhr_write(id_ ,position_low,position_high,speed_low,speed_high):
##    checksum = [id_ , 0x07 , 0x03 , 0x1e , position_low , position_high , speed_low + speed_high]
##    __not_checksum__ = not_checksum(checksum) 
##    data = '\xff\xff' + chr(id_) + '\x07\x03\x1e' + chr(position_low)+ chr(position_high) + chr(speed_low) + chr(speed_high) + chr(__not_checksum__)
##    a=5000
##    rw('w')
##    time.sleep(0.001)
##    dynamixel.write(data)
##    while(dynamixel.inWaiting()==0 and a!=0):
##        print('its 0')
##        a=a-1
##    while(dynamixel.inWaiting()!=0):
##        data = dynamixel.read(dynamixel.inWaiting())
##        print(data)
##        time.sleep(.001)

##def  dhr_write(id_ ,position_low,position_high,speed_low,speed_high):
##    checksum = [id_ , 0x07 , 0x03 , 0x1e , position_low , position_high , speed_low + speed_high]
##    __not_checksum__ = not_checksum(checksum) 
##    data = '\xff\xff' + chr(id_) + '\x07\x03\x1e' + chr(position_low)+ chr(position_high) + chr(speed_low) + chr(speed_high) + chr(__not_checksum__)
##    a=50
##    rw('w')
##    time.sleep(0.001)
##    dynamixel.write(data)
##    time.sleep(.001)
##    rw('r')
##    time.sleep(.001)
##    while(dynamixel.inWaiting()==0 and a!=0):
##        print('its 0')
##        a=a-1
##    while(dynamixel.inWaiting()!=0):
##        data = dynamixel.read(dynamixel.inWaiting())
##        print(data)
##        time.sleep(.001)

def dhr_test():
    dhr_write2(0x01,0x00,0x00,0xff,0x03)
    time.sleep(3)
    dhr_write2(0x02,0x00,0x00,0xff,0x03)
    time.sleep(3)
    dhr_write2(0x01,0x0ff,0x0f,0xff,0x03)
    time.sleep(3)
    dhr_write2(0x02,0x0ff,0x0f,0xff,0x03)
##    time.sleep(3)
##    data=dynamixel.inWaiting()
##    print data
##    data=dynamixel.read(dynamixel.inWaiting())
##    print data

def ping() :
    
    data = '\xff\xff\x01\x02\x01\xfb'
    rw('w')
    time.sleep(0.1)
    dynamixel.write(data)
    time.sleep(0.1)
    rw('r')
    while(dynamixel.inWaiting() == 0) :
        print('.')
    if(dynamixel.inWaiting() != 0) :
        data = dynamixel.read(dynamixel.inWaiting())
        print(data)
        time.sleep(1)
def pk() :
    checksum = [0x01 , 0x07 , 0x03 , 0x06 , 0x00 , 0x00 , 0x0ff + 0x0f]
    __not_checksum__ = not_checksum(checksum) 
    data = '\xff\xff\x01\x07\x03\x06\x00\x00\x0ff\x0f' + chr(__not_checksum__)
    rw('w')
    time.sleep(0.1)
    dynamixel.write(data)
    time.sleep(3)
    write5()
    time.sleep(3)
    write6()
    time.sleep(3)
    write4()
    time.sleep(3)
    write3()

##def read(id_) :
##    checksum = [id_ , 0x04 , 0x02 , 0x24 , 0x04]
##    __not_checksum__ = not_checksum(checksum)
##    data = '\xff\xff' + chr(id_)
##    rw(arduino,'r')
##
def read(id_) :
    checksum = [id_ , 0x04 , 0x02 , 0x24 , 0x04]
    __not_checksum__ = not_checksum(checksum)
    data = '\xff\xff' + chr(id_) + '\x04\x02\x24\x04' + chr(__not_checksum__)
    rw('w')
    write4()
    time.sleep(3)
    write3()
    time.sleep(3)
    dynamixel.write(data)
    time.sleep(0.1)
    rw('r')
    time.sleep(3)
    write4()
    time.sleep(3)
    write3()
    time.sleep(3)
    data = dynamixel.read(dynamixel.inWaiting())
    return data

def not_checksum(l) :
    checksum = 0
    for i in range(len(l)) :
        checksum += (l[i])
    not_checksum = (~checksum)&0xff
    return not_checksum

def rw(n) :
    if(n == 'w')  :
        arduino.write('w')
    if(n == 'r') :
        arduino.write('r')

def ping(id_) :
    checksum = [id_,0x02,0x01]
    __not_checksum__ = not_checksum(checksum)
    data = '\xff\xff' + chr(id_) + '\x02\x01'
    rw('w')
    time.sleep(0.1)
    dynamixel.write(data)
    time.sleep(0.1)
    rw('r')

def write3() :
    write(0x01,0x00,0x00,0xff,0x03)

def write4() :
    write(0x01,0x0ff,0x0f,0xff,0x03)

def write5() :
    write(0x02,0x00,0x00,0xff,0x03)

def write6() :
    write(0x02,0x0ff,0x0f,0xff,0x03)
    


##def check() :
##    data = []
##    for i in range(0.1,1,0.1) :
##        data.append(wite1())
##        time.sleep(2)
##    return data 
    
'''instructions --->
    setp1: download the serial library for python (pyserial) if you havent already done so
    setp2: put in the appropriate com port for instantiating the arduino and dynamixel serial ports
           eg: arduino = startup('com7')
    step3: run the program once (F5)
    step4: after running, the initialization of the serial port should be indicated by the properties
           of the serial port displayed in blue
    step5: after initializing, the >> symbol will appear indicating that python is waiting for you to type into
           here, check if dynamixel is working by calling the check() function

    IF (DYNAMIXEL MOVES) :
        OKAY SIR !!!
    ELSE :
        DROP DEAD
'''

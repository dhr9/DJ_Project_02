'''to communicate with the dynamixel motor via the max485 ic , we need to set up a
    virtual com port and create an instance of the serial.Serial class , so as to
    use it to read data from and write data to the dynamixel
    
    serial<id,open=(true/false)>(port = ?,baudrate = ?,bytesize = ?,parity = 'Y/N',
    stopbits = ?,timeout = ?,xonxoff = (True/False),rtscts = (True/False),dsrdtr =
    (True/False))
'''


##INSTRUCTIONS ABOUT HOW TO USE THIS CODE
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
    ELSE :\]
    
        DROP DEAD
'''
##-------------------------INITIALIZATION------------------------------

import time                              #import time liabrary to use the time.sleep()
                                         #function to generate delays
import serial                            #import the serial library

import string

def startup(com) :
    ser = serial.Serial(port = com)      #create an instance of the serial.Serial class 
    print(ser)
    ser.baudrate = 57600                 #set baudrate equal to 9600
    print(ser.baudrate)
    return ser

##arduino =  startup('com7')
##dynamixel = startup('com3')
##dynamixel = startup('/dev/tty.usbserial-A90246TV')
dynamixel = startup('/dev/tty.usbserial-A800doqB')
arduino1 = startup('/dev/tty.usbmodem1411')
##arduino2 = startup('/dev/tty.usbmodem14141')

##---------------------------------------------------------------------
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




##----------------------------------CODE-----------------------------------

def not_checksum(l) :
    checksum = 0
    for i in range(len(l)) :
        checksum += l[i]
    __not_checksum__ = (~checksum)&0xff
    return __not_checksum__



def rw(n) :
    if(n == 'w')  :
        arduino1.write('w')
    if(n == 'r') :
        arduino1.write('r')

def instruction_packet(id_,address,length,__not_checksum__) :
    __instruction_packet__ = '\xff\xff' + chr(id_) + '\x04\x02' + chr(address) + chr(length) + chr(__not_checksum__)
    array = []
    for i in range(len(__instruction_packet__)) :
        array.append(escape(__instruction_packet__[i]))
    return array
        

def escape(c) :
        
	if c in string.printable :
		return c
	elif c <= '\xff' :
		return r'\x{0:02x}'.format(ord(c))
	else :
		return c.encode('unicode_escape').decode('ascii')

def read(id_,address,length) :
    checksum_array = [id_,0x04,0x02,address,length]
    __instruction_packet__ = instruction_packet(id_,address,length,not_checksum(checksum_array)) 
    print(__instruction_packet__)
    __not_checksum__ = not_checksum(checksum_array)
    __instruction_packet__ = '\xff\xff' + chr(id_) + '\x04\x02' + chr(address) + chr(length) + chr(__not_checksum__)
    rw('r')
    time.sleep(0.1)
    dynamixel.write(__instruction_packet__)
    time.sleep(0.001)
    rw('w')
    time.sleep(0.1)
    print('--->')
    data = arduino2.read(arduino2.inWaiting())
    print(data)

def eeprom_read() :
    print('motor 1 --------------------------------------------')
    for i in range(73) :
        read(01,i,1)
    print('motor 2 --------------------------------------------')
    for i in range(73) :
        read(02,i,1)

def write(id_ ,position_low,position_high,speed_low,speed_high) :
    
    checksum = [id_ , 0x07 , 0x03 , 0x1e , position_low , position_high , speed_low + speed_high]
    __not_checksum__ = not_checksum(checksum) 
    data = '\xff\xff' + chr(id_) + '\x07\x03\x1e' + chr(position_low)+ chr(position_high) + chr(speed_low) + chr(speed_high) + chr(__not_checksum__)
    rw('r')
    time.sleep(0.1)
    dynamixel.write(data)
    rw('w')

def write1() :
    write(0x01,0x00,0x00,0xff,0x03)

def write2() :
    write(0x01,0x0ff,0x0f,0xff,0x03)

def write3() :
    write(0x02,0x00,0x00,0xff,0x03)

def write4() :
    write(0x02,0x0ff,0x0f,0xff,0x03)
##------------------------------------------------------------------------




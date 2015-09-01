from debug import debug

import time                              #import time liabrary to use the time.sleep()
                                         #function to generate delays
import serial                            #import the serial library
import platform
import serial_ports_setup
import check_status_packet
import exception_handling

GO_TO_DYNA_1_POS=0
GO_TO_DYNA_2_POS=0

watchdog = 10     #change later
#arduino = ''
dynamixel = ''
system = ''

def dyna_write():
    global GO_TO_DYNA_1_POS
    global GO_TO_DYNA_2_POS
    global watchdog

    write(1,GO_TO_DYNA_1_POS)
    write(2,GO_TO_DYNA_2_POS)

    print("moving to ",GO_TO_DYNA_1_POS,",",GO_TO_DYNA_2_POS)
    for i in range(watchdog):
        check_bit = 0
        check_bit += dyna_read(1,GO_TO_DYNA_1_POS)
        check_bit += dyna_read(2,GO_TO_DYNA_2_POS)
        time.sleep(0.001)
        if(check_bit==2):
            print("dyna reached in ",i," iterations")
            break
    if(check_bit!=2):
        print("watchdogtimer overflowed")
    else:
        print("reached !")

def dyna_read(motor_id,goal_pos):
    value = read(motor_id,0x1e,2)
    if(value==False):
        return 0
    else:
        current_pos = value[1]*256 + value[0]
    if(goal_pos==current_pos):
        return 1
    else:
        return 0

def write(motor_id,pos):

    def convert_to_two_bytes(n):
        return([int(n/256),int(n%256)])

    [h_byte,l_byte] = convert_to_two_bytes(pos)
    check_bit = send_instruction(motor_id,3,0x1e,l_byte,h_byte)
    if(check_bit==1):
        return
    if(check_bit==0):
        print("oh shit...wrong check bit returned")

def read(motor_id,location,no_of_bytes):
    a = send_instruction(motor_id,2,location,no_of_bytes)
    if(a==False):
        print("read mein jhol hai")
    else:
        return a

def startup(com) :
    ser = serial.Serial(port = com)      #create an instance of the serial.Serial class
    print(ser)
    ser.baudrate = 57600                 #set baudrate equal to 9600
    print(ser.baudrate)
    return ser

def init() :

    global system
    global dynamixel
    # global arduino

    system = platform.system()
    # [dynamixel,arduino] = serial_ports_setup.find_dynamixel_and_arduino()
    [dynamixel] = serial_ports_setup.find_dynamixel_and_arduino()
    print('dynamixel : ',dynamixel)
    # print('arduino : ',arduino)

    '''
    EXCEPTION CHECK --> cant connect
    '''
    try : 
        dynamixel = startup(dynamixel)
    except OSError : 
        exception_handling.handle_exception(__name__,'cant connect')
    # arduino = startup(arduino)

def not_checksum(l) :
    checksum = 0
    for i in range(len(l)) :
        checksum += l[i]
    not_checksum = (~checksum)&0xff
    return not_checksum

def instruction_length(instruction,*args) :
    instructions_that_require_parameters = [0x02,0x03,0x04]
    if(instruction in instructions_that_require_parameters) :
        return (len(args) + 2)
    else :
        return 2

def build_instruction_packet(motor_id,instruction,*args) :
    instructions_that_require_parameters = [0x02,0x03,0x04]
    instruction_length_ = instruction_length(instruction,*args)
    checksum = [motor_id,instruction_length_,instruction]
    if(instruction in instructions_that_require_parameters) :
        for i in range(len(args)) :
            checksum.append(args[i])
    not_checksum_ = not_checksum(checksum)
    instruction_packet = '\xff\xff'
    for i in range(len(checksum)) :
        instruction_packet += chr(checksum[i])
    instruction_packet += chr(not_checksum_)
    #print (list(instruction_packet))
    return(instruction_packet)


def send_instruction(motor_id,instruction,*args) :
    instruction_packet = build_instruction_packet(motor_id,instruction,*args)
    dynamixel.write(instruction_packet)
    time.sleep(0.01)
    status_packet = dynamixel.read(dynamixel.inWaiting())
    status_packet = check_status_packet.get_status_packet(instruction_packet,status_packet)
    if(status_packet != False) :
        check_status_packet.print_packet(status_packet)
    else :
        print('incorrect statuss packet')
    #if(check_status_packet(instruction_packet,status_packet)) :
    #    print('succesful')
    #else :
    #    print('something went wrong')

def char_to_int(character) :
    for i in range(256) :
        if(chr(i) == character) :
            return(i)

def wait_for_reply() :
    while(arduino.inWaiting() == 0) :
        print('waiting for arduino reply')
    data = arduino.read(arduino.inWaiting())
    print(data)

count_ = 0
count = 0

def print_count() :
    global count_
    if(count__ > 9):
        count_ += 1
        count__ = 0
    print(str(count_) + '.' + str(count))

def setup_dynamixel_communication() :
    global count
    send_instruction(1,1)
    time.sleep(0.1)
    data = 0
    count += 1
    print(count)
    if(dynamixel.inWaiting() != 0) :
        print(dynamixel.read())
        data = dynamixel.read(1)
    if(data != 0) :
        print('done')
    else :
        if(count < 200) :
            arduino.write('\x02')
            setup_dynamixel_communication()



init()



'''to communicate with the dynamixel motor via the max485 ic , we need to set up a
    virtual com port and create an instance of the serial.Serial class , so as to
    use it to read data from and write data to the dynamixel
        serial<id,open=(true/false)>(port = ?,baudrate = ?,bytesize = ?,parity = 'Y/N',
    stopbits = ?,timeout = ?,xonxoff = (True/False),rtscts = (True/False),dsrdtr =
    (True/False))
'''


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
--------------------------------------------------------------------------------------
'''

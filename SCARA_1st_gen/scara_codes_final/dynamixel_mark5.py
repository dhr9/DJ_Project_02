#---------------------------INITIALIZATION-------------------------------

import time    #for using the time.sleep(delay) function to include delays in your code 
import serial

def startup(com) : #com --> communication port number to which your device is connected
    ser = serial.Serial(port = com)
    ser.baudrate = 57600
    print(ser)
    return ser

##dynamixel = startup('/dev/tty.usbserial-A800doqB')
##arduino = startup('/dev/tty.usbmodem14121')
#--------------------------------------------------------------------------

def not_checksum(l) :
    checksum = 0
    for i in range(len(l)) :
        checksum += (l[i])
    not_checksum = (~checksum)&0xff
    return not_checksum

def angle_to_hex(angle) :
    angle_ = (angle/360.0)*65535
    print angle_
    higher_byte = int(angle_/256)
    lower_byte = int(angle_%256)
    return[lower_byte,higher_byte]

def  write_data_to_dynamixel(id_ ,angle,speed_low,speed_high):
    position_bytes = angle_to_hex(angle)
    position_low = position_bytes[0]
    position_high = position_bytes[1]
    print(position_low)
    print(position_high)
    checksum = [id_ , 0x07 , 0x03 , 0x1e , position_low , position_high , speed_low, speed_high]
    __not_checksum__ = not_checksum(checksum)
    print(__not_checksum__)
    data = '\xff\xff' + chr(id_) + '\x07\x03\x1e' + chr(position_low)+ chr(position_high) + chr(speed_low) + chr(speed_high) + chr(__not_checksum__)
    val = [data]
    print val
    rw('w')
    time.sleep(0.01)
##    dynamixel.write(data)
    val = data
    print(val)

def read_data_from_dynamixel(id_,starting_address,length) :
    checksum = [id_ , 0x04 , 0x02 , starting_address , length]
    __not_checksum__ = not_checksum(checksum)
    data = '\xff\xff' + chr(id_) + '\x04\x02' + chr(starting_address) + chr(length) + chr(__not_checksum__)
    rw('w')
    time.sleep(0.001)
    dynamixel.write(data)
    val = data
    print(val)
    data = dynamixel.read(dynamixel.inWaiting())
    return(data)

def rw(n) :
    if(n == 'w')  :
        arduino.write('w')
        print()
    else :
        print('error !')

def dynamixel_reset_position() :
    move_to_position(0x01,180)
    move_to_positing(0x02,180)
    
#--------------------------------------------------------------------------


def move_to_position(motor_id,angle) :
    position_high = (angle_to_hex(angle))[0]
    position_low = (angle_to_hex(angle))[1]
    write_data_to_dynamixel(motor_id,angle,0xff,0x03)
    data = read_data_from_dynamixel(motor_id)
    data = '\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
    current_position = list(data)
    print(current_position)
    current_position_low = current_position[6]
    current_position_high = current_position[7]
    while((current_position_low == position_low) & (current_position_high == position_high)) :
        print(current_position)
        current_position_low = current_position[6]
        current_position_high = current_position[7]        
    print('okay sirji :)')


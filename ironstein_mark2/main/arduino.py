working_directory = '/users/ironstein/documents/projects working directory'
import os
os.chdir(working_directory)

from subordinate import serial_ports_setup

arduino = ''

def init() :

    def startup(com) :
        ser = serial.Serial(port = com)      #create an instance of the serial.Serial class
        print(ser)
        ser.baudrate = 57600                 #set baudrate equal to 9600
        print(ser.baudrate)
        return ser

    global arduino
    [arduino] = serial_ports_setup.find_dynamixel_and_arduino()
    
    '''
    EXCEPTION CHECK --> cant connect
    '''
    try : 
        arduino = startup(arduino)
    except OSError: 
        exception_handling.handle_exception(__name__,'cant connect')

def pick(pick_angle) :
    arduino.write(chr(200) + chr(222) + chr(pick_angle))

def place(place_angle) :
    arduino.write(chr(211) + chr(222) + chr(place_angle))
    
init()


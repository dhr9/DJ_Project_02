import sys # sys.platform
import glob # glob.glob
import serial # serial.Serial  
import platform # platform.system
import inspect # inspect.stack
from subordinate_directory import exception_handling

def find_dynamixel_and_arduino() :
    global dynamixel_port,arduino_port

    #check if this function called by dynamixel.py or arduino.py
    #return the arduino or arduino or dynamixel port respectively
    stack = inspect.stack()
    if 'dynamixel' in stack[1][1] :
        try :
            ser = serial.Serial(port = dynamixel_port)      #create an instance of the serial.Serial class 
        except : 
            exception_handling.handle_exception('dynamixel','cant connect')
        else :
            print(ser)
            ser.baudrate = 57600                 #set baudrate equal to 57600
            return ser

    elif 'arduino' in stack[1][1] :
        return[arduino]
    else : 
        print('serial_ports_setup.py called by some module\
            other that dynamixel.py or arduino.py')

def get_connected_serial_ports() : 
    serial_ports_list = serial_ports()
    
    system = platform.system()
    # print('system --> ',system)
    print('available serial ports : ',serial_ports_list)
    dynamixel_port = ''
    arduino_port = ''

    #for unix
    if system.startswith('Darwin') :
        for port in serial_ports_list :
            if port.startswith('/dev/tty.usbserial') :
                dynamixel_port = port
            elif port.startswith('/dev/tty.usbmodem') :
                arduino_port = port
    #for windows
    elif system.startswith('Win') :
        if len(serial_ports_list) != 2 :
            print("Connect Exactly two serial devices")
            # CHANGE -- Let GUI print this in a msg box
        dynamixel_port = 'com4'
        arduino_port = 'com3'      # CHANGE
    #for others
    else :
        print('unsupported operating system')
        # CHANGE -- Let GUI print this in a msg box
        
    return [dynamixel_port,arduino_port]

def serial_ports():
    """Lists serial ports

    :raises EnvironmentError:
        On unsupported or unknown platforms
    :returns:
        A list of available serial ports
    """
    if sys.platform.startswith('win'):
        ports = ['COM' + str(i + 1) for i in range(256)]

    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this is to exclude your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')

    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')

    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

[dynamixel_port,arduino_port] = get_connected_serial_ports()

__all__ = ['find_dynamixel_and_arduino']
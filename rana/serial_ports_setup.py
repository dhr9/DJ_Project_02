import sys
import glob
import serial
import platform

def find_dynamixel_and_arduino() : 
    system = platform.system()
    print(system)
    serial_ports_list = serial_ports()
    print('available serial ports : ')
    print(serial_ports_list)
    dynamixel = ''
    arduino = ''
    if(system.startswith('Darwin')) : 
        for port in serial_ports_list : 
            if(port.startswith('/dev/tty.usbserial')) : 
                dynamixel = port
            elif(port.startswith('/dev/tty.usbmodem')) : 
                arduino = port 
    elif(system.startswith('Win')) :
        if(len(serial_ports_list) != 2):
            print("Connect Exactly two serial devices")
        dynamixel = 'com7'
        arduino = 'com3'
    else : 
        print('unsupported operating system')

    # return [dynamixel,arduino]
    return [dynamixel]
    

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
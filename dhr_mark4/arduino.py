import serial_ports_setup

arduino = ''

def init() :
    global arduino
    [arduino] = serial_ports_setup.find_dynamixel_and_arduino()

def pick(pick_angle) :
    arduino.write(chr(200) + chr(222) + chr(pick_angle))

def place(place_angle) :
    arduino.write(chr(211) + chr(222) + chr(place_angle))
    
init()

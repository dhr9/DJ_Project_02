import serial_ports_setup
def init() :
    [arduino] = serial_ports_setup.find_dynamixel_and_arduino()


init()

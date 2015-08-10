import serial

SERVO_ANGLE = 0

def startup(com) :
    ser = serial.Serial(port = com)      #create an instance of the serial.Serial class 
    print(ser)
    ser.baudrate = 57600                 #set baudrate equal to 9600
    print(ser.baudrate)
    return ser


#arduino =  startup('com3')
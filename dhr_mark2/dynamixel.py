from debug import debug
import exception_handling
import arduino

import time
import serial

GO_TO_DYNA_1_POS=0
GO_TO_DYNA_2_POS=0

def startup(com) :
    ser = serial.Serial(port = com)      #create an instance of the serial.Serial class 
    print(ser)
    ser.baudrate = 57600                 #set baudrate equal to 9600
    print(ser.baudrate)
    return ser

#dynamixel = startup('com4')

@debug()	
def dyna_write() :
	global GO_TO_DYNA_1_POS
	global GO_TO_DYNA_2_POS
	print("moving to "+str(GO_TO_DYNA_1_POS)+","+str(GO_TO_DYNA_2_POS))
	for i in range(2):
		dyna_read()
	print("reached !")


#@debug()
def	dyna_read() :
	print("reading...")

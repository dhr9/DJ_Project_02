import serial_ports_setup
arduino = ''

def init() : 
	def startup(com) : 
		ser = serial.Serial(port = com) 
		print(ser)
		ser.baudrate = 57600
		print(ser.baudrate)
		return ser

	global arduino
	[arduino] = serial_ports_setup.find_dynamixel_and_arduino()
	arduino = startup(arduino)

def write(position) : 
	instruction_packet = '\x00' + chr(position)
	arduino.write(instruction_packet)
	while(not arduino.inWaiting()) : pass
	arduino.read(arduino.inWaiting())
	
def pick() : 
	arduino.write('\x01')
	pass

def place() : 
	arduino.write('\x02')
	pass
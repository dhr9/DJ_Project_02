import dynamixel

def check() :
	for id_ in range(200) :
		send(id_)
		if (int(ser.inWaiting()) != int(0)) :
			print('inWaiting')
			print(id_)
			print(ser.inWaiting())
			break

def read(id_) :
	ser.write('\xff')
	ser.write('\xff')
	ser.write(chr(id_))
	ser.write('\x04')
	ser.write('\x02')
	ser.write('\x1e')
	ser.write('\x04')
	ser.write(chr(215-id_))

def write(id_) :
        ser.write('\xff')
        ser.write('\xff')
        ser.write(chr(id_))
        ser.write('\x04')
        ser.write('\x03')
        ser.write('\x1e')
        ser.write('\x02')
        ser.write('\x00')
        ser.write('\x0f')
        ser.write(chr(0xda - id_))

ser = dynamixel.startup('com3')

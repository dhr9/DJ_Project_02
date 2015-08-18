def check_status_packet(instruction_packet,status_packet) : 
	status_packet = get_status_packet(instruction_packet,status_packet)
	expected_status_packet = generated_expected_status_packet(instruction_packet)
	if(expected_status_packet.instruction != '\x02') :
		if (expected_status_packet.generated_status_packet in status_packet) :
			return True
		else : 
			new_status_packet = ''
			for i in range(len(expected_status_packet)) :
				new_status_packet += status_packet[i]
			status_packet = new_status_packet
			del(new_status_packet)
			if((status_packet[0] == '\xff') and (status_packet[1] == '\xff')) : 
				if(status_packet[4] != '\x00') : 
					error = error_byte_decode(char_to_int(status_packet[4]))
					print(error)
					return False
				else :
					print('BAD STATUS PACKET')
					return False
			else : 
				print('INVALID PACKET SYNTAX')
				return False
	else :
		number_of_parameters = expected_status_packet.number_of_parameters
		if((status_packet[0]+status_packet[1]) == '\xff\xff') :
			if(status_packet[4] != '\x00') : 
				error = error_byte_decode(char_to_int(status_packet[4]))
				print(error)
				return False
			else : 
				parameters = []
				for i in range(5,5+number_of_parameters) : 
					parameters.append(status_packet[i])
				return parameters
		else : 
			print('INVALID PACKET SYNTAX')
			return False

def error_byte_decode(error_byte) : 
	error = {
	0 : 'INPUT VOLTAGE ERROR',
	1 : 'ANGLE LIMIT ERROR',
	2 : 'OVERHEATING ERROR',
	3 : 'RANGE ERROR',
	4 : 'CHECKSUM ERROR',
	5 : 'OVERLOAD ERROR',
	6 : 'INSTRUCTION ERROR',
	7 : 'INVALID ERROR BYTE', 
	}
	error_byte_list = []
	for i in range(8) :
		error_byte_list.append((int(error_byte/(2**i)))&0x01)
	error_message = ''
	for i in range(len(error_byte_list)) : 
		if(error_byte_list[i]) : 
			error_message += '\n' + error.get(i)
	return error_message

def char_to_int(character) : 
	for i in range(256) : 
		if(chr(i) == character) : 
			return i

class generated_expected_status_packet() : 
	
	def __init__(self,instruction_packet) : 
		self.instruction_packet = list(instruction_packet)
		self.motor_id = instruction_packet[2]
		self.number_of_parameters = self.char_to_int(instruction_packet[3]) - 2
		self.instruction = instruction_packet[4]
		self.parameters = []
		for i in range(5,5+self.number_of_parameters) : 
			self.parameters.append(instruction_packet[i])
		self.checksum = instruction_packet[-1]
		self.length_of_status_packet = ''
		self.status_packet_parameters = []
		self.generated_status_packet = ''
		self.instruction_switch_case(self.char_to_int(self.instruction))
		self.__print__()

	def __print__(self) : 
		print('self.instruction_packet',self.instruction_packet)
		print('self.motor_id',self.motor_id)
		print('self.number_of_parameters',self.number_of_parameters)
		print('self.instruction',self.instruction)
		print('self.parameters',self.parameters)
		print('self.checksum',self.checksum)
		print('self.length_of_status_packet',self.length_of_status_packet)
		print('status_packet_parameters',self.status_packet_parameters)
		print('generated_status_packet',self.generated_status_packet)

	def instruction_switch_case(self,instruction) : 
		switcher = {
		1 : self.ping,
		2 : self.read,
		3 : self.write,
		4 : self.reg_write,
		5 : self.action,
		6 : self.reset,
		83 : self.sync_write,
		}
		function =  switcher.get(instruction)
		function()
		self.status_packet()

	def status_packet(self) :
		status_packet = '\xff\xff'
		status_packet += self.motor_id
		status_packet += chr(self.length_of_status_packet)
		status_packet += '\x00'
		
		if (len(self.status_packet_parameters) != 0) : 
			for parameter in self.status_packet_parameters : 
				status_packet += parameter
			status_packet += '\checksum'
		else : 
			checksum = [self.motor_id,self.length_of_status_packet + 2]
			not_checksum_ = self.not_checksum(checksum) 
			status_packet += chr(not_checksum_)
		self.generated_status_packet = status_packet

	def not_checksum(self,l) : 
		checksum = 0
		for element in l : 
			if(type(element) != type(1)) :
				checksum += self.char_to_int(element)
			else : 
				checksum += element
		not_checksum = (~checksum)&0xff
		return not_checksum

	def ping(self) : 
		self.length_of_status_packet = 0
		self.status_packet_parameters = []

	def read(self) : 
		self.length_of_status_packet = self.char_to_int(self.instruction_packet[6])
		for i in range(self.char_to_int(self.instruction_packet[6])) : 
			self.status_packet_parameters.append('\data')

	def write(self) : 
		self.length_of_status_packet = 0
		self.status_packet_parameters = []

	def reg_write(self) : 
		self.length_of_status_packet = 0
		self.status_packet_parameters = []

	def action(self) : 
		self.length_of_status_packet = 0
		self.status_packet_parameters = []

	def reset(self) : 
		self.length_of_status_packet = 0
		self.status_packet_parameters = []

	def sync_write(self) : 
		self.length_of_status_packet = 0
		self.status_packet_parameters = []

	def char_to_int(self,character) : 
		for i in range(256) : 
			if(chr(i) == character) : 
				return i

def get_status_packet(instruction_packet,status_packet) : 

	def char_to_int(character) : 
		for i in range(256) : 
			if(chr(i) == character) : 
				return i

	common_string = ''
	for i in range(3) : 
		common_string += instruction_packet[i]
	if(common_string not in status_packet) : 
		return False 
	for i in range(len(status_packet)) : 
		if((status_packet[i] == common_string[0]) and \
			(status_packet[i+1] == common_string[1]) and \
			(status_packet[i+2] == common_string[2])) :
			breaks

	number_of_parameters = char_to_int(status_packet[i+3]) - 2
	error_byte = status_packet[i+4]
	parameters = ''
	for i in range(i+5,i+5+number_of_parameters) : 
		parameters = status_packet[i]
	checksum = status_packet[i+5+number_of_parameters]

	return_status_packet = ''
	return_status_packet += common_string
	return_status_packet += chr(number_of_parameters + 2)
	return_status_packet += error_byte
	return_status_packet += parameters
	return_status_packet += checksum

	return return_status_packet

def print_packet(packet) : 

	def char_to_int(character) : 
		for i in range(256) : 
			if(chr(i) == character) : 
				return i

	for character in packet : 
			print(hex(char_to_int(character)),end=' ')
		print()

	# for character in packet : 
	# 	print (hex(char_to_int(character))),

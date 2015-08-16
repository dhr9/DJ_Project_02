def check_status_packet(instruction_packet,status_packet) : 
	expected_status_packet = generated_expected_status_packet(instruction_packet)
	if(expected_status_packet.instruction != 2) :
		if (expected_status_packet.generated_status_packet in status_packet) :
			return True
		else : 
			new_status_packet = ''
			for i in range(len(expected_status_packet)) :
				new_status_packet += status_packet[i]
			status_packet = new_status_packet
			if((status_packet[0] == '\xff') and (status_packet[1] == '\xff')) : 
				if(status_packet[5] != 0) : 
					error = error_byte_decode(status_packet[5])
					return error
				else :
					return 'BAD STATUS PACKET'
			else : 
				return 'INVALID PACKET SYNTAX'
	else : 
		print()

def error_byte_decode() : 
	error = {
	0 : 'INPUT VOLTAGE ERROR'
	1 : 'ANGLE LIMIT ERROR'
	2 : 'OVERHEATING ERROR'
	3 : 'RANGE ERROR'
	4 : 'CHECKSUM ERROR'
	5 : 'OVERLOAD ERROR'
	6 : 'INSTRUCTION ERROR'
	7 : 'INVALID ERROR BYTE' 
	
	}

class generated_expected_status_packet() : 
	
	def __init__(self,instruction_packet) : 
		self.instruction_packet = list(instruction_packet)
		self.motor_id = instruction_packet[2]
		self.number_of_parameters = self.char_to_int(instruction_packet[3]) - 2
		self.instruction = instruction_packet[4]
		self.parameters = []
		for i in range(6,6+self.number_of_parameters) : 
			self.parameters.append(instruction_packet[i])
		self.checksum = instruction_packet[-1]
		self.length_of_status_packet = ''
		self.status_packet_parameters = []
		self.generated_status_packet = ''
		self.instruction_switch_case(self.char_to_int(self.instruction))

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
		self.length_of_status_packet = self.parameters[-1]
		for i in range((self.length_of_status_packet)) : 
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

m = generated_expected_status_packet('\xff\xff\x02\x05\x03\x1e\x00\x00\xd7')
generated_status_packet = m.generated_status_packet
print(len(generated_status_packet))
for character in generated_status_packet : 
	print(m.char_to_int(character),end = ' ')
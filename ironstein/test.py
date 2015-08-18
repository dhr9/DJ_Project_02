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
			break

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
			print(hex(char_to_int(character)))
	print('\n')

	# for character in packet : 
	# 	print (hex(char_to_int(character))),

a = get_status_packet('\xff\xff\x02\x05\x03\x1e\x00\x00\xd7',\
	'\x01\x02\x03\xff\xff\x02\x02\x00\x23')
print_packet(a)

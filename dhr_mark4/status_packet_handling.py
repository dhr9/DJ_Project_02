from string_handling import char_to_int

def get_status_packet(instruction_packet,status_packet) : 

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
	for j in range(i+5,i+5+number_of_parameters) : 
		parameters += status_packet[j]
	checksum = status_packet[i+5+number_of_parameters]

	return_status_packet = ''
	return_status_packet += common_string
	return_status_packet += chr(number_of_parameters + 2)
	return_status_packet += error_byte
	return_status_packet += parameters
	return_status_packet += checksum

	if(check_checksum(return_status_packet)) : 
		return return_status_packet
	return False

def check_checksum(status_packet) :

	def not_checksum(l) :
		checksum = 0
		for i in range(len(l)) : 
			checksum += l[i]
		not_checksum = (~checksum)&0xff
		return not_checksum

	checksum = []
	for i in range(2,len(status_packet)-1) : 
		checksum.append(char_to_int(status_packet[i]))
	not_checksum_ = not_checksum(checksum)

	if(chr(not_checksum_) != status_packet[-1]) : 
		return False
	return True

def print_packet(packet) : 

	# for character in packet : 
	# 		print(hex(char_to_int(character)),end=' ')
	# print()

	for character in packet : 
		print (hex(char_to_int(character))),

def check_for_error(status_packet) : 

	error_byte = char_to_int(status_packet[4])
	if(error_byte == 0) : 
		return False
	else : 
		error_byte_list = []
		for i in range(8) :
			error_byte_list.append((int(error_byte/(2**i)))&0x01)
		return error_byte_list

def error_service_routine(error_byte_list,type = 0) : 

	if(type == 0) :
	
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
		error_message = ''
		for i in range(len(error_byte_list)) : 
			if(error_byte_list[i]) : 
				error_message += '\n' + error.get(i)
		print(error_message)

	elif(type == 1) : 
		error_message = 'USER DEFINED ERROR : '
		error = {
		1 : 'COMMUNICATION ERROR'
		}
		error_message += error.get(error_byte_list)
		print(error_message)

# status_packet = get_status_packet('\xff\xff\x02\x05\x03\x1e\x00\x00\xd7','\x03\x23\xff\xff\x02\x03\x03\x01\xf6\xa1\xb4')
# print_packet(status_packet)

# b = check_for_error(status_packet)
# print(b) 
# error_service_routine(b)
# error_service_routine(1,type=1)

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
		parameters = status_packet[j]
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
		log(error_message)

	elif(type == 1) : 
		error_message = 'USER DEFINED ERROR : '
		error = {
		1 : 'COMMUNICATION ERROR'
		}
		error_message += error.get(error_byte_list)
		print(error_message)
		log(error_message)

def log(error) : 

	class get_time() : 

		def __init__(self) : 
			self.t = ''
			self.year = ''
			self.month = ''
			self.day = ''
			self.hour = ''
			self.minute = ''
			self.second = ''
			self.week_day = ''

			self.get_time()

		def __print__(self) : 
			print('time : ',self.t)
			print('year : ',self.year)
			print('month : ',self.month)
			print('day : ',self.day)
			print('hour : ',self.hour)
			print('minute : ',self.minute)
			print('second : ',self.second)
			print('week_day : ',self.week_day)

		def get_time(self) :
			import time

			def get_before_and_after(string,after,before) : 
				dont_need_character_list = [' ']
				if((after in string) and (before in string)) : 
					i = string.index(after) + len(after)
					j = string.index(before,i,i+5)
					return_string = ''
					for k in range(i,j) : 
						if(string[k] not in dont_need_character_list) :
							return_string += string[k]
					return return_string
				else : 
					print('before or after not in string') 

			def char_to_int(character) : 
				for i in range(256) : 
					if(chr(i) == character) : 
						return i

			self.t = str(time.localtime())
			self.year = get_before_and_after(self.t,'tm_year=',',')
			self.month = get_before_and_after(self.t,'tm_mon=',',')
			self.day = get_before_and_after(self.t,'tm_mday=',',')
			self.hour = get_before_and_after(self.t,'tm_hour=',',')
			self.minute = get_before_and_after(self.t,'tm_min=',',')
			self.second = get_before_and_after(self.t,'tm_sec=',',')
			self.week_day = get_before_and_after(self.t,'tm_wday=',',')
			day = {
				'0':'Mon',
				'1':'Tue',
				'2':'Wed',
				'3':'Thu',
				'4':'Fri',
				'6':'Sat',
				'7':'Sun'
			}
			month = {
				'1':'Jan',
				'2':'Feb',
				'3':'Mar',
				'4':'Apr',
				'5':'May',
				'6':'Jun',
				'7':'Jul',
				'8':'Aug',
				'9':'Sep',
				'10':'Aug',
				'11':'Nov',
				'12':'Dec'
			}

			self.week_day = day.get(self.week_day)
			self.month = month.get(self.month)

	t = get_time()
	return_string = t.day + '/' + t.month + '/' + t.year \
	+ ' ' + t.hour + ':' + t.minute + ':' + t.second\
	+ ' --> ' + error + '\n'
	
	log = open('log.txt','a')
	log.write(return_string)
	log.close()

for i in range(5) : 
	log('lets try it out')

# status_packet = get_status_packet('\xff\xff\x02\x05\x03\x1e\x00\x00\xd7','\x03\x23\xff\xff\x02\x03\x03\x01\xf6\xa1\xb4')
# print_packet(status_packet)

# b = check_for_error(status_packet)
# print(b) 
# error_service_routine(b)
# error_service_routine(1,type=1)
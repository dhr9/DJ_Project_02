# send_and_check_limit = 10

# def not_checksum(l) :
# 	checksum = 0
# 	for i in range(len(l)) : 
# 		checksum += l[i]
# 	not_checksum = (~checksum)&0xff
# 	return not_checksum

# def instruction_length(instruction,*args) :
#     instructions_that_require_parameters = [0x02,0x03,0x04]
#     if(instruction in instructions_that_require_parameters) :
#         return (len(args) + 2)
#     else :
#         return 2

# def build_instruction_packet(motor_id,instruction,*args) : 
#     instructions_that_require_parameters = [0x02,0x03,0x04]
#     instruction_length_ = instruction_length(instruction,*args)
#     checksum = [motor_id,instruction_length_,instruction]
#     if(instruction in instructions_that_require_parameters) :
#         for i in range(len(args)) :
#             checksum.append(args[i])
#     not_checksum_ = not_checksum(checksum)
#     instruction_packet = '\xff\xff'
#     for i in range(len(checksum)) :
#         instruction_packet += chr(checksum[i])
#     instruction_packet += chr(not_checksum_)
#     return(instruction_packet)

# def send_and_check(motor_id,instruction,*args) : 
# 	instruction_packet = build_instruction_packet(motor_id,instruction,*args)
	
# 	global send_and_check_limit
# 	count = 0

# 	while(count < send_and_check_limit) :
# 		dynamixel.write(instruction_packet)
# 		time.sleep(0.01)
# 		status_packet = dynamixel.read(dynamixel.inWaiting())
# 		status_packet = status_packet_handling.get_status_packet(instruction_packet,status_packet)
# 		if(status_packet == False) :
# 			count+=1
# 		else:
# 			error = check_for_error(status_packet) 
# 			if(error == False) :
# 				return status_packet
# 			else:
# 				status_packet_handling.error_service_routine(error)
# 	return False

def angles_from_status_packet(packet,offset) : 

	def char_to_int(character) : 
		for i in range(256) : 
			if(chr(i) == character) : 
				return i

	number_of_parameters = char_to_int(packet[3]) - 2
	parameters = []
	for i in range(5,5+number_of_parameters) : 
		parameters.append(packet[i])

	def hex_to_angle(position_low,position_high,offset):
		angle = (char_to_int(position_high))*256 + char_to_int(position_low)
		angle *= 360
		angle /= 4096
		angle += offset
		angle %= 360
		return int(angle)

	return hex_to_angle(parameters[0],parameters[1],offset)


# def angle_to_hex(angle,offset) : 
# 	angle = (angle+offset)%360
# 	angle = int((angle*4095)/360)
# 	angle_high = int(angle/256)
# 	angle_low = angle%256
# 	return([chr(angle_low),chr(angle_high)])

def angle_to_hex(angle,offset):
	if(angle == int(angle)) : 
		if(angle%45 != 0) : 
			angle += 0.1
	angle += offset
	angle %= 360
	angle *= 4096
	angle /= 360
	angle %= 4096
	angle = int(angle)
	return([chr(int(angle%256)),chr(int(angle/256))])

def hex_to_angle(position_low,position_high,offset):
	def char_to_int(character) : 
		for i in range(256) : 
			if(chr(i) == character) : 
				return i
	angle = (char_to_int(position_high))*256 + char_to_int(position_low)
	angle *= 360
	angle /= 4096
	angle += offset
	angle %= 360

	return int(angle)


# c=0
# for i in range(3600):
# 	j = i / 10
# 	t = angle_to_hex(j,180)
# 	g = hex_to_angle(t[0],t[1],180)
# 	# if(j == int(j)) : 
# 	# 	if(j%45 != 0) :
# 	# 		j -=0.01
# 	if(int(j)!=g):
# 		print(j)
# 		print(g)
# 		print("--")
# 		c += 1
# print(c)

# print(hex_to_angle('\xff','\x07',180))
# print(angle_to_hex(359,180))


a = angles_from_status_packet('\xff\xff\x02\x04\x00\x00\x08\xfb',180)
print(a)
print(angle_to_hex(a,180))
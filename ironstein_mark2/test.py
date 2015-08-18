send_and_check_limit = 10

def not_checksum(l) :
	checksum = 0
	for i in range(len(l)) : 
		checksum += l[i]
	not_checksum = (~checksum)&0xff
	return not_checksum

def instruction_length(instruction,*args) :
    instructions_that_require_parameters = [0x02,0x03,0x04]
    if(instruction in instructions_that_require_parameters) :
        return (len(args) + 2)
    else :
        return 2

def build_instruction_packet(motor_id,instruction,*args) : 
    instructions_that_require_parameters = [0x02,0x03,0x04]
    instruction_length_ = instruction_length(instruction,*args)
    checksum = [motor_id,instruction_length_,instruction]
    if(instruction in instructions_that_require_parameters) :
        for i in range(len(args)) :
            checksum.append(args[i])
    not_checksum_ = not_checksum(checksum)
    instruction_packet = '\xff\xff'
    for i in range(len(checksum)) :
        instruction_packet += chr(checksum[i])
    instruction_packet += chr(not_checksum_)
    return(instruction_packet)

def send_and_check(motor_id,instruction,*args) : 
	instruction_packet = build_instruction_packet(motor_id,instruction,*args)
	
	global send_and_check_limit
	count = 0

	while(count < send_and_check_limit) :
		dynamixel.write(instruction_packet)
		time.sleep(0.01)
		status_packet = dynamixel.read(dynamixel.inWaiting())
		status_packet = status_packet_handling.get_status_packet(instruction_packet,status_packet)
		if(status_packet == False) :
			count+=1
		else:
			error = check_for_error(status_packet) 
			if(error == False) :
				return status_packet
			else:
				status_packet_handling.error_service_routine(error)
	return False





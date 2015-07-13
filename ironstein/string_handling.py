def char_to_int(c) : 
	for i in range(256) :
		if(chr(i) == c) : 
			return i

def skip_character(string,character,i) : 
	j = i
	while((string[j] == character)and(i<len(string))) : 
		j += 1 

	return j-i

def skip_until_character(string,character,i) : 
	j = i
	while((string[j] != character)and(i<len(string))) : 
		j += 1

	return j-i

useless_array = [' ','\n','\t']
def skip_useless(string,i) : 
	j = i
	while(string[j] in useless_array) : 
		for k in range(len(useless_array)) : 
			j += skip_character(string,useless_array[k],j)

def remove_useless(string) : 
	i = 0
	return_string = ''
	while(i < len(string)) : 
		if(not(string[i] in useless_array)) : 
			return_string += string[i]
		i += 1 
	return(return_string)

def string_to_int(string) : 
	num = 0
	for i in range(len(string)) : 
		num += (10**(len(string)-i-1))*int(string[i])
	return num

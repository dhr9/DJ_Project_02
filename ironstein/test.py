def skip_character(string,character,i) : 
	j = i
	while((string[j] == character)and(i<len(string))) : 
		j += 1 
		print(j)

	return j-i


def edit_position_array(logs) : 

	character = ''
	array = []
	i = 0
	print(logs)
	while(i < len(logs)) : 
		i += skip_character(logs,' ',i)
		print(logs[i])
		print('banana')
		#print(i)
		break

edit_position_array('      sdf ')

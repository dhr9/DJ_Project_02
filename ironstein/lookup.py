from debug import debug
from string_handling import *

POSITION_ARRAY = []

@debug('init_lookup')
def init_lookup() : 
	logs = open('lookup.txt','r')
	logs_ = logs.read()
	print(logs_)
	edit_position_array(logs_)
	logs.close()

@debug()
def edit_position_array(logs) : 

	character_array = []
	array = []
	i = 0
	while(i < len(logs)) : 

		skip_useless(logs,i)

		if(logs[i] == '#') : 
			i += skip_until_character(logs,'\n',i)
			break

		character_array.append(logs[i])
		i += skip_until_character(logs,'{',i)
		i += 1

		string = ''
		while(logs[i] != '}') : 
			string += logs[i] 
			i += 1
		i += 1

		array.append(string)
		if(i != len(logs)) : 
			skip_useless(logs,i)
		else : 
			break

	# now we have the array consisting of 
	for i in range(len(array)) : 
		array[i] = remove_useless(array[i])

	array = decode_array(array)
	print(array)
	return(array)

@debug()
def decode_array(array) : 
	return_array = []
	for i in range(len(array)) : 
		return_array.append([])
	for i in range(len(array)) : 
		j = 0
		while(j < len(array[i])) : 
			skip_useless(array[i],j)
			skip_character(array[i],',',j)
			j += skip_until_character(array[i],'[',j)
			j += 1
			string = ''
			while(array[i][j] != ']') : 
				string += array[i][j]
				j += 1
			j += 1
			return_array[i].append(string)
	return(return_array)


init_lookup()

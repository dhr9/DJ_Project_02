from debug import debug
from string_handling import *


LOOKUP_OUTPUT = [0,0,0]
DYNA_1_POS = 0
DYNA_2_POS = 0
#POSITION_ARRAY = [[[-15,-105,-15,-105,38,83,1],[-60,80,2,-40,48,84,1],[80,-92,-2,85,58,85,1]]]
POSITION_ARRAY = []
POSITION_ARRAY_FLAGS = []

max_scalable_area = 3072

@debug()
def lookup(letter,directive):
	#directive = 0 for pick and 1 for place
	###direction = 0 for fwd and 1 for bckwrd
	#letter needs to be local
	#directive needs to be local

	global LOOKUP_OUTPUT #delete later

	if (letter == "A"):
		sort(0,directive)
		# for A, index is 0
	if (letter == "B"):
		sort(1,directive)
	if (letter == "C"):
		sort(2,directive)
	if (letter == "D"):
		sort(3,directive)

@debug()
def sort(index,directive):
	#directive needs to be local
	global POSITION_ARRAY
	global POSITION_KEY

	# len_letters = len(POSITION_ARRAY)   #length of letters
	no_of_instances = len(POSITION_ARRAY[index])
	maximum = []
	for i in range(no_of_instances*2) :  
		maximum.append([])
	#loop to find maximums
	for i in range (no_of_instances):
		for j in range (2):
			if ( POSITION_ARRAY_FLAGS[ index ][ i ] != directive ):
				#checking availability

				#print("i = ",i," j = ",j)

				x = POSITION_ARRAY[ index ][ i ][ (j*2) +0 ]
				y = POSITION_ARRAY[ index ][ i ][ (j*2) +1 ]
				maximum[(2*i)+j] = max_of_two(x,y)
				#print("max[",(2*i)+j,"] = ",maximum[(2*i)+j])

			else :
				maximum[(2*i)+j] = max_scalable_area
				#max value possible
	
	# to find minimum
	i_min = 0
	j_min = 0
	for i in range (no_of_instances):
		for j in range (2):
			if(maximum[(2*i)+j] < maximum[(2*i_min)+j_min]):
				i_min = i
				j_min = j

	LOOKUP_OUTPUT[0] = POSITION_ARRAY[ index ][ i_min ][ (2*j_min) ]
	LOOKUP_OUTPUT[1] = POSITION_ARRAY[ index ][ i_min ][ (2*j_min) + 1 ]
	LOOKUP_OUTPUT[2] = POSITION_ARRAY[ index ][ i_min ][ j_min + 4 ]
	POSITION_ARRAY_FLAGS[ index ][ i_min ] = directive
	change_array(POSITION_ARRAY_FLAGS,0)

#@debug()
def max_of_two(x,y):
	global DYNA_1_POS
	global DYNA_2_POS
	a = mod(DYNA_1_POS - x)      	 #difference 1
	b = mod(DYNA_2_POS - y)       	 #difference 2
	if (a<b):
		a=b                       	 #if b is greater
	return a

#@debug()
def mod(s):
	if (s<0):
		s*=-1
	return s                        #make positive

######### ARRAY OPERATIONS ###########
def change_array(array,num):
	#num=0 ==> POSITION_ARRAY_FLAGS
	#num=1 ==> DISPLAY_AREA_POSITIONS
	a = open("variable_array.txt","r")
	k=[]
	for line in a:
		k.append(line)
	a.close()
	s = str(array)
	if(num != len(k)-1):
		s += '\n'
	k[num] = s
	a = open("variable_array.txt","w")
	for i in range(len(k)):
		a.write(k[i])
	a.close()
########### RIYANSH CODES ##########

#@debug('init_lookup')
def init_lookup() : 
	logs = open('lookup.txt','r')
	logs_ = logs.read()
	#print(logs_)
	edit_position_array(logs_)
	logs.close()

#@debug()
def edit_position_array(logs) : 

	character_array = []
	array = []
	i = 0
	while(i < len(logs)) : 

		i += skip_useless(logs,i)

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
		if(i < len(logs)) : 
			i += skip_useless(logs,i)
		else : 
			break

	# print(logs)

	# now we have the array consisting of 
	for i in range(len(array)) : 
		array[i] = remove_useless(array[i])


	array = decode_array(array)
	#print(array)

	return_array = []
	for i in range(len(array)) : 
		return_array.append([])
		for j in range(len(array[i])) : 
			return_array[i].append([])

	#print(return_array)

	for i in range(len(array)) : 
		for j in range(len(array[i])) : 
			#print(len(array[i][j]))
			k = 0
			while(k < len(array[i][j])) : 
				string = ''
				while((k < len(array[i][j])) and (array[i][j][k] != ',')and(array[i][j][k] != '\n')) : 
					string += array[i][j][k]
					k += 1
					#print(k)
				k += 1

				return_array[i][j].append(string)
				#print(string)

	#print(return_array)
	array = return_array

	return_array = []
	for i in range(len(array)) : 
		return_array.append([])
		for j in range(len(array[i])) : 
			return_array[i].append([])

	for i in range(len(array)) : 
		for j in range(len(array[i])) : 
			for k in range(len(array[i][j])) : 
				return_array[i][j].append(string_to_int(array[i][j][k]))

	#print(return_array)

	global POSITION_ARRAY 
	POSITION_ARRAY = return_array

	global POSITION_ARRAY_FLAGS
	for character in POSITION_ARRAY :
		array = [] 
		for element in character : 
			array.append(element.pop())
		POSITION_ARRAY_FLAGS.append(array)

#@debug()
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

######### Initialization call #########

init_lookup()
print("Position array :- ",POSITION_ARRAY)
print
print('position array flags : ',POSITION_ARRAY_FLAGS)
print
change_array(POSITION_ARRAY_FLAGS,0)
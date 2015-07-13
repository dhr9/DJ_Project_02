from debug import debug

LOOKUP_OUTPUT = [0,0,0]
DYNA_1_POS = 0
DYNA_2_POS = 0
POSITION_ARRAY = [[[-15,-105,-15,-105,38,83,1],[-60,80,2,-40,48,84,1],[80,-92,-2,85,58,85,1]]]


@debug()
def lookup(letter,directive,direction):
	#directive = 0 for pick and 1 for place
	#direction = 0 for fwd and 1 for bckwrd
	#letter needs to be local
	#directive needs to be local

	global LOOKUP_OUTPUT #delete later

	if (directive == 1):
		#sort(26,directive)
		LOOKUP_OUTPUT = [12,20,30]

	else:
		if (letter == "A"):
			sort(0,directive)
			# for A, index is 0
		else:
			LOOKUP_OUTPUT = [63,73,83]

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
			if ( POSITION_ARRAY[ index ][ i ][ 6 ] != directive ):
				#checking availability

				#print("i = ",i," j = ",j)

				x = POSITION_ARRAY[ index ][ i ][ (j*2) +0 ]
				y = POSITION_ARRAY[ index ][ i ][ (j*2) +1 ]
				maximum[(2*i)+j] = max_of_two(x,y)
				#print("max[",(2*i)+j,"] = ",maximum[(2*i)+j])

			else :
				maximum[(2*i)+j] = 270
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
	POSITION_ARRAY[ index ][ i_min ][ 6 ] = directive

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

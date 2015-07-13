import lookup
# import dynamixel

#from debug import debug

CURRENT_ARRAY_LENGTH = 0
CURRENT_ARRAY = []

#@debug()
def modify_blocks():
	global CURRENT_ARRAY_LENGTH
	global CURRENT_ARRAY

	CURRENT_ARRAY_LENGTH = len(CURRENT_ARRAY)

	print(CURRENT_ARRAY_LENGTH)
	print("-----------------")
	for i in range (CURRENT_ARRAY_LENGTH):
		print(i)
		print(lookup.LOOKUP_OUTPUT)
		# print(lookup.DYNA_1_POS)
		# print(lookup.DYNA_2_POS)
		print(CURRENT_ARRAY[i])
		lookup.lookup(CURRENT_ARRAY[i],0,0)
		# eg:- "A",pick,fwd
		print(lookup.LOOKUP_OUTPUT)
		# dynamixel.GO_TO_DYNA_1_POS = lookup.LOOKUP_OUTPUT[0]
		# dynamixel.GO_TO_DYNA_2_POS = lookup.LOOKUP_OUTPUT[1]
		# dynamixel.dyna_write()
		# lookup.DYNA_1_POS = dynamixel.GO_TO_DYNA_1_POS
		# lookup.DYNA_2_POS = dynamixel.GO_TO_DYNA_2_POS
		# print(lookup.DYNA_1_POS)
		# print(lookup.DYNA_2_POS)
		print("----")

	print("-----------------")
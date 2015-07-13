import lookup

CURRENT_ARRAY_LENGTH = 0
CURRENT_ARRAY = []

def modify_blocks():
	global CURRENT_ARRAY_LENGTH
	global CURRENT_ARRAY

	CURRENT_ARRAY_LENGTH = len(CURRENT_ARRAY)
	print(CURRENT_ARRAY_LENGTH)
	print("-----------------")
	for i in range (CURRENT_ARRAY_LENGTH):
		print(i)
		print(lookup.LOOKUP_OUTPUT)
		print(CURRENT_ARRAY[i])
		lookup.lookup(CURRENT_ARRAY[i])
		print(lookup.LOOKUP_OUTPUT)
		print("----")

	print("-----------------")
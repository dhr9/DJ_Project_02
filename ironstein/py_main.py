import lookup
import dynamixel

from debug import debug

CURRENT_ARRAY_LENGTH = 0
CURRENT_ARRAY = []
DISPLAY_AREA_POSITIONS = []

@debug()
def modify_blocks():
	global CURRENT_ARRAY_LENGTH
	global CURRENT_ARRAY
	global DISPLAY_AREA_POSITIONS

	CURRENT_ARRAY_LENGTH = len(CURRENT_ARRAY)

	display_area_calc()

	print(CURRENT_ARRAY_LENGTH)
	print("-----------------")
	for i in range (CURRENT_ARRAY_LENGTH):
		print(i)
		# print("LOOKUP_OUTPUT = ",lookup.LOOKUP_OUTPUT)
		# print("DYNA_1_POS = ",lookup.DYNA_1_POS)
		# print("DYNA_2_POS = ",lookup.DYNA_2_POS)
		#--------------- PICK FORWARD --------------------------
		print("Picking ",CURRENT_ARRAY[i]," from trash")
		lookup.lookup(CURRENT_ARRAY[i],0)
		# # eg:- "A",pick
		# print("LOOKUP_OUTPUT = ",lookup.LOOKUP_OUTPUT)
		dynamixel.GO_TO_DYNA_1_POS = lookup.LOOKUP_OUTPUT[0]
		dynamixel.GO_TO_DYNA_2_POS = lookup.LOOKUP_OUTPUT[1]
		dynamixel.dyna_write()
		lookup.DYNA_1_POS = dynamixel.GO_TO_DYNA_1_POS
		lookup.DYNA_2_POS = dynamixel.GO_TO_DYNA_2_POS
		# print("DYNA_1_POS = ",lookup.DYNA_1_POS)
		# print("DYNA_2_POS = ",lookup.DYNA_2_POS)
		# print("----")
		#-------------------------------------------------------
		print("----")
		#---------------- PLACE FORWARD ------------------------
		print("Placing ",CURRENT_ARRAY[i]," on display area")
		print(dynamixel.GO_TO_DYNA_1_POS)
		dynamixel.GO_TO_DYNA_1_POS = DISPLAY_AREA_POSITIONS[i][0]
		print('rananannananan')
		print(dynamixel.GO_TO_DYNA_1_POS)
		dynamixel.GO_TO_DYNA_2_POS = DISPLAY_AREA_POSITIONS[i][1]
		dynamixel.dyna_write()
		lookup.DYNA_1_POS = dynamixel.GO_TO_DYNA_1_POS
		lookup.DYNA_2_POS = dynamixel.GO_TO_DYNA_2_POS
		#-------------------------------------------------------
		print("-----------------")
	print("wait thoda...\nwait thoda...\nwait thoda...")
	print("-----------------")
	for k in range (CURRENT_ARRAY_LENGTH):
		i=CURRENT_ARRAY_LENGTH-k-1
		#----------------- PICK REVERSE ------------------------
		print("Picking ",CURRENT_ARRAY[i]," from display area")
		dynamixel.GO_TO_DYNA_1_POS = DISPLAY_AREA_POSITIONS[i][0]
		dynamixel.GO_TO_DYNA_2_POS = DISPLAY_AREA_POSITIONS[i][1]
		dynamixel.dyna_write()
		lookup.DYNA_1_POS = dynamixel.GO_TO_DYNA_1_POS
		lookup.DYNA_2_POS = dynamixel.GO_TO_DYNA_2_POS
		#-------------------------------------------------------
		print("----")
		#--------------- PLACE REVERSE --------------------------
		print("Placing ",CURRENT_ARRAY[i]," in trash")
		lookup.lookup(CURRENT_ARRAY[i],1)
		dynamixel.GO_TO_DYNA_1_POS = lookup.LOOKUP_OUTPUT[0]
		dynamixel.GO_TO_DYNA_2_POS = lookup.LOOKUP_OUTPUT[1]
		dynamixel.dyna_write()
		lookup.DYNA_1_POS = dynamixel.GO_TO_DYNA_1_POS
		lookup.DYNA_2_POS = dynamixel.GO_TO_DYNA_2_POS
		#-------------------------------------------------------
		print("-----------------")
	print("bring it on")

@debug()
def display_area_calc():
	global CURRENT_ARRAY_LENGTH
	global DISPLAY_AREA_POSITIONS

	DISPLAY_AREA_POSITIONS = [[23,32],[34,43],[45,54],[56,65],[67,76],[78,87],[89,98]]
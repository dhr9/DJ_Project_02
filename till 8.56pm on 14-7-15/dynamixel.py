from debug import debug
import exception_handling
import arduino

GO_TO_DYNA_1_POS=0
GO_TO_DYNA_2_POS=0

@debug()	
def dyna_write() :
	global GO_TO_DYNA_1_POS
	global GO_TO_DYNA_2_POS
	print("moving to "+str(GO_TO_DYNA_1_POS)+","+str(GO_TO_DYNA_2_POS))
	for i in range(2):
		dyna_read()
	print("reached !")


#@debug()
def	dyna_read() :
	print("reading...")

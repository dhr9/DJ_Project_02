from debug import debug

GO_TO_DYNA_1_POS=0
GO_TO_DYNA_2_POS=0

@debug()	
def dyna_write() :
	for i in range(5):
		dyna_read()
	print()


@debug()
def	dyna_read() :
	print()

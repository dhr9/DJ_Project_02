from debug import debug

GO_TO_DYNA_1_POS=0
GO_TO_DYNA_2_POS=0

def GO_TO_DYNA_1_POS_(*args) :
	if(args != ()) :
		print('rananananana')
		GO_TO_DYNA_1_POS = args


@debug()	
def dyna_write() :
	for i in range(3):
		dyna_read()
	print()


@debug()
def	dyna_read() :
	print()

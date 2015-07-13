from debug import debug

LOOKUP_OUTPUT = [0,0,0]
DYNA_1_POS = 0
DYNA_2_POS = 0

@debug()
def lookup(letter):
	global LOOKUP_OUTPUT
	global DYNA_1_POS
	global DYNA_2_POS

	if (letter == "R"):
		LOOKUP_OUTPUT[0] = 45
		LOOKUP_OUTPUT[1] = -30
		LOOKUP_OUTPUT[2] = 28

	else:
		LOOKUP_OUTPUT = [63,73,83]

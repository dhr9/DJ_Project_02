import lookup
import dynamixel
import logging
from debug import debug
from log_decorator import logs

CURRENT_ARRAY_LENGTH = 0
CURRENT_ARRAY = []
#logging.basicConfig(filename='log.txt', level=logging.INFO)

@logs()
def modify_blocks():
	global CURRENT_ARRAY
	# logging.basicConfig(filename='log.txt',format='%(asctime)s %(message )s' ,level=logging.INFO)
 #    	logging.info('hi')
	CURRENT_ARRAY_LENGTH = len(CURRENT_ARRAY)

	logging.info(CURRENT_ARRAY_LENGTH)
	logging.info("-----------------")
	for i in range (CURRENT_ARRAY_LENGTH):
		logging.info(i)
		logging.info(lookup.LOOKUP_OUTPUT)
		logging.info(lookup.DYNA_1_POS)
		logging.info(lookup.DYNA_2_POS)
		logging.info(CURRENT_ARRAY[i])
		logging.info(CURRENT_ARRAY[i])
		lookup.lookup(CURRENT_ARRAY[i])
		logging.info(lookup.LOOKUP_OUTPUT)
		dynamixel.GO_TO_DYNA_1_POS = lookup.LOOKUP_OUTPUT[0]
		dynamixel.GO_TO_DYNA_2_POS = lookup.LOOKUP_OUTPUT[1]
		logging.info(lookup.LOOKUP_OUTPUT[0])
		logging.info(lookup.LOOKUP_OUTPUT[1])
		dynamixel.dyna_write()
		lookup.DYNA_1_POS = dynamixel.GO_TO_DYNA_1_POS
		lookup.DYNA_2_POS = dynamixel.GO_TO_DYNA_2_POS
		logging.info(lookup.DYNA_1_POS)
		logging.info(lookup.DYNA_2_POS)
		logging.info("----")

	logging.info("-----------------")

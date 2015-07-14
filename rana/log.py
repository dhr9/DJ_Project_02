# import logging
# logging.basicConfig(filename='example.log',level=logging.INFO)
# logging.debug('This message should go to the log fil')
# logging.info('So should this')
# logging.warning('And this, too')

import logging
#import gui
#import py_main

def main():
	logging.basicConfig(filename='log.txt', level=logging.INFO)
	logging.info('logging started')
	logging.info('logging fini')

main()
import sys
gui = sys.modules['__main__']

def handle_exception(module_name,exception_name,*args) :
	
	arduino = []
	dynamixel = []
	lookup = []
	status_packet_handling  = []
	py_main = []
	some_file = ['error']

	module_names = {
		'arduino' : arduino,
		'dynamixel' : dynamixel,
		'lookup' : lookup,
		'status_packet_handling' : status_packet_handling,
		'py_main' : py_main,
		'some_file' : some_file
	}

	if exception_name=='r': 
		print(gui.EXCEPTION_MODULE)
		print(gui.EXCEPTION)
		print()

	elif module_name in module_names.keys() and\
		exception_name in module_names[module_name] :
		gui.EXCEPTION_MODULE = module_name
		gui.EXCEPTION = exception_name
		gui.exception_caught(*args)
		gui.some_file.n = int(args[0])
		
	else : 
		print('invalid exception')
		print()
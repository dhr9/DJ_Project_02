import exception_handling
n = 1
def do_some_work() : 
	global n

	while(n) : 
		i = input('enter something : ').split(' ')
		exception_handling.handle_exception(__name__,i[0],*tuple(i[1:]))

	print('n changed to 0')
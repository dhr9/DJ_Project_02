import os
os.chdir('/users/ironstein/documents/projects working directory/scara/dj_project_02/ironstein_mark2/test')

EXCEPTION_MODULE = 'none'
EXCEPTION = 'none'

def exception_caught(*args) :
	print(args)
	global EXCEPTION,EXCEPTION_MODULE

	print(EXCEPTION_MODULE + ' --> ' +EXCEPTION)
	print('printing complete')
	print()
	#some_file.n = int(args[0])

print('-----------------------------------')

import some_file
some_file.do_some_work()
from functools import wraps

class debug() : 
	def __init__(self,*args,**kwargs) : 
		self.args = args

	def __call__(self,func) : 

		@wraps(func)
		def wrapper(*args,**kwargs) : 
			print('entering ' + func.__name__)
			func(*args)
			print('exiting ' + func.__name__)
			print('\n')
		return wrapper
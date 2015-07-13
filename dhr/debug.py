from functools import wraps

class debug() : 
	def __init__(self,*args,**kwargs) : 
		self.args = args
		print(self.args)

	def __call__(self,func) : 

		if((self.args) == ('init_lookup',)) : 
			print('hi')

		@wraps(func)
		def wrapper(*args,**kwargs) : 
			print('entering ' + func.__name__)
			func(*args) 
			print('exiting ' + func.__name__)
		return wrapper

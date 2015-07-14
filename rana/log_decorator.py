from functools import wraps 
import logging
class logs():
	def __init__(self,*args,**kwargs):
		self.args = args
		print(self.args)

	def __call__ (self,func) :

		@wraps(func)
		def wrapper(*args, **kwargs):
			logging.basicConfig(filename='log.txt',format='%(asctime)s: %(message)s: ', level=logging.INFO)
			return(logging.info(*))
		return wrapper
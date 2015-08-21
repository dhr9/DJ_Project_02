class get_time() : 

	def __init__(self) : 
		self.t = ''
		self.year = ''
		self.month = ''
		self.day = ''
		self.hour = ''
		self.minute = ''
		self.second = ''
		self.week_day = ''

		self.get_time()
		self.__print__()

	def __print__(self) : 
		print('time : ',self.t)
		print('year : ',self.year)
		print('month : ',self.month)
		print('day : ',self.day)
		print('hour : ',self.hour)
		print('minute : ',self.minute)
		print('second : ',self.second)
		print('week_day : ',self.week_day)

	def get_time(self) :
		import time

		def get_before_and_after(string,after,before) : 
			dont_need_character_list = [' ']
			if((after in string) and (before in string)) : 
				i = string.index(after) + len(after)
				j = string.index(before,i,i+5)
				return_string = ''
				for k in range(i,j) : 
					if(string[k] not in dont_need_character_list) :
						return_string += string[k]
				return return_string
			else : 
				print('before or after not in string') 

		def char_to_int(character) : 
			for i in range(256) : 
				if(chr(i) == character) : 
					return i

		self.t = str(time.localtime())
		self.year = get_before_and_after(self.t,'tm_year=',',')
		self.month = get_before_and_after(self.t,'tm_mon=',',')
		self.day = get_before_and_after(self.t,'tm_mday=',',')
		self.hour = get_before_and_after(self.t,'tm_hour=',',')
		self.minute = get_before_and_after(self.t,'tm_min=',',')
		self.second = get_before_and_after(self.t,'tm_sec=',',')
		self.week_day = get_before_and_after(self.t,'tm_wday=',',')
		day = {
			'0':'Mon',
			'1':'Tue',
			'2':'Wed',
			'3':'Thu',
			'4':'Fri',
			'6':'Sat',
			'7':'Sun'
		}
		month = {
			'1':'Jan',
			'2':'Feb',
			'3':'Mar',
			'4':'Apr',
			'5':'May',
			'6':'Jun',
			'7':'Jul',
			'8':'Aug',
			'9':'Sep',
			'10':'Aug',
			'11':'Nov',
			'12':'Dec'
		}

		self.week_day = day.get(self.week_day)
		self.month = month.get(self.month)

get_time()


# class rad_to_deg() : 

# 	def __init__(self,function) : 
# 		self.function = function
# 		print('inside __init__')

# 	def __call__(self,*args) : 
# 		import math
# 		deg = args[0]
# 		rad = deg*(math.pi/180)
# 		return self.function(rad)

# import math

# @rad_to_deg
# def sin(theta) :
# 	return(math.sin(theta))

# print(sin(90))
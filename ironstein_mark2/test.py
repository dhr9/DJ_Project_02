# import sys

# try:
#     f = open('lookup.txt')
#     s = f.readline()
#     i = int(s.strip())
# except IOError as e:
#     print ("I/O error({0}): {1}".format(e.errno, e.strerror))
# # except ValueError:
# #     print ("Could not convert data to an integer.")
# except:
#     print ("Unexpected error:", sys.exc_info()[0])
#     raise

for i in range(10) : 
		
	try : 
		print('hmm')
		try : 
			if(i == 5) : 
				raise NameError
			print(i)

		except TypeError: 
			print('exception i == 5')

	except NameError : 
		print('hi')	
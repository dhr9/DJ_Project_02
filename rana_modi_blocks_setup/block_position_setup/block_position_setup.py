import os
working_directory = '/users/ironstein/documents/projects working directory/SCARA/DJ_Project_02/ironstein_mark2'
os.chdir(working_directory)

def block_values(position_list) :
	setup_position_log = open('values.txt','a')
	setup_position_log.write(str(position_list))
	setup_position_log.write('\n')
	setup_position_log.close()

class setup_position_log_to_lookup_txt() :

	def __init__(self,position_list) :
		setup_position_log = open('block_values.txt','r')
		self.position_log = []
		for line in setup_position_log :
			self.position_log.append(self.string_to_list(line))
		setup_position_log.close()

		lookup_list = []
		for i in range(26) :
			lookup_list.append([])
		for i in range(len(self.position_log)) :
			for j in range(len(position_list)):
				if(i+1 in position_list[j]) :
					lookup_list[j].append(self.position_log[i])

		lookup  = open('lookup.txt','w')
		for i in range(len(lookup_list)) :
			string = chr(i+97) + ' = {\n'
			for j in range(len(lookup_list[i])) :
				string += '	  ' + str(lookup_list[i][j]) + str(',\n')
			string = string[:-2]
			string += '\n'
			string += '}\n'
			lookup.write(string)



	def string_to_list(self,string) :
		new_string = ''
		for i in range(string.index('[')+1,string.index(']')) :
			new_string += string[i]
		list_ = new_string.split(',')
		print(list_)
		return_list = []
		for i in range(len(list_)) :
			return_list.append(self.string_to_number(list_[i]))
		return return_list

	def string_to_number(self,string) :
		if('.' in string) :
			return float(string)
		return int(string)

#a = setup_position_log_to_lookup_txt(1)
#a.string_to_list('[1,2,3,4,5,12,34.5,4.233,6.4509]')
position_list = [[1,23],[2,24],[3,25],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17],[18],[19],[20],[21],[22],[],[],[],[]]
setup_position_log_to_lookup_txt(position_list)

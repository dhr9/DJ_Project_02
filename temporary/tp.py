def gui_main():
	print("All Initializations successfully completed")

	print(py_main.CURRENT_ARRAY_LENGTH)
	print(py_main.CURRENT_ARRAY)

	py_main.CURRENT_ARRAY = ['O','K']

	print(py_main.CURRENT_ARRAY_LENGTH)
	print(py_main.CURRENT_ARRAY)

	py_main.modify_blocks()

	print(py_main.CURRENT_ARRAY_LENGTH)
	print(py_main.CURRENT_ARRAY)

# py_main.CURRENT_ARRAY = ['D','H','R']

# print(py_main.CURRENT_ARRAY_LENGTH)
# print(py_main.CURRENT_ARRAY)

# py_main.modify_blocks()

# print(py_main.CURRENT_ARRAY_LENGTH)
# print(py_main.CURRENT_ARRAY)

# py_main.CURRENT_ARRAY = ['R','I']

# print(py_main.CURRENT_ARRAY_LENGTH)
# print(py_main.CURRENT_ARRAY)

# py_main.modify_blocks()

# print(py_main.CURRENT_ARRAY_LENGTH)
# print(py_main.CURRENT_ARRAY)

######### Initialization call #########

gui_main()
import py_main

print(py_main.CURRENT_ARRAY_LENGTH)
print(py_main.CURRENT_ARRAY)

py_main.CURRENT_ARRAY = ['R','A','N','A']
py_main.modify_blocks()

print(py_main.CURRENT_ARRAY_LENGTH)
print(py_main.CURRENT_ARRAY)
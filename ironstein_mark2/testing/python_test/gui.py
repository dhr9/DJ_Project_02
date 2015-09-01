print("module gui")
import py_main as a
print("after gui")

VAR_C = 8

def main():
    a.a()

def c():
    print("inside c")

if __name__ == "__main__":
	main()
	print(VAR_C)
	a.main()
	print(a.VAR_A)
	print(a.b.VAR_B)
	print(VAR_C)

def change(x):
	global VAR_C
	VAR_C = x
print('---c---')
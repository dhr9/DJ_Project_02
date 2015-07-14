print("module c")
import a
print("after c")

VAR_C = 8

def main():
    a.a()

def c():
    print("inside c")

if __name__ == "__main__":
	main()
	print(VAR_C)
	a.main()
	print(a.VAR)
	print(VAR_C)

def change(x):
	global VAR_C
	VAR_C = x
print('---c---')
print("module a")
import b
from c import change
print("after a")

import sys


VAR = 0

def main():
	global VAR
	b.b()
	VAR = 10
	print(b.c.VAR_C)
	names = sorted(sys.modules.keys())
	sys.modules['__main__'].VAR_C = 15
	print(names)
	change(15)

def a():
    print("inside a")

if __name__ == "__main__":
    main()
    print(b.c.c())

print('---a---')
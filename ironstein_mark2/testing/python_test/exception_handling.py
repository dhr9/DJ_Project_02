import sys

print("module exception_handling")
c = sys.modules['__main__']
print("after exception_handling")

VAR_B = 10

def main():
    c.c()

def b():
    print("inside b")

def change(x,y) :
	global VAR_B 
	VAR_B = x
	c.VAR_C = y

print('---b---')
print("module b")
import c
print("after b")
VAR_B = 10

def main():
    c.c()

def b():
    print("inside b")

if __name__ == "__main__":
    main()


print('---b---')
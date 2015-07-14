import os
print(os.getcwd())
print

f = open("Test.txt",'a');
print f
 
value = 'My name is', 'riyansh'
myString = str(value)

f.write(myString)

f.close()
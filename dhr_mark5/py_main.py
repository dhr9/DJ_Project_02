import time

CURRENT_ARRAY = []
FLAG = False

def modify_blocks(obj):
    global FLAG
    global CURRENT_ARRAY
    
    print("entering modify blocks")
    global_string = ''
    string = CURRENT_ARRAY
    FLAG = False
    for i in range(len(CURRENT_ARRAY)):
        if(CURRENT_ARRAY[i] == " "):
            global_string+=" "
            continue
        print("picking block")
        global_string+=string[i]
        obj.update_label(global_string)
        time.sleep(1.5)
        print("placing block")
        global_string+='....'
        obj.update_label(global_string)
        time.sleep(1.5)
        p=i+1
        if(FLAG):
            break
            
    for k in range(p):
        i = p-k-1
        if(CURRENT_ARRAY[i] == " "):
            global_string = global_string[:-1]
            continue
        print(i)
        print("picking block again")
        global_string = global_string[:-4]
        obj.update_label(global_string)
        time.sleep(1.5)
        print("placing block again")
        global_string = global_string[:-1]
        obj.update_label(global_string)
        time.sleep(1.5)

# l = [[[],[]],[[],[],[]],[[],[],[],[]],[[],[]],[[]],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

##def get_max_no_of_blocks(character) :
##    global l
##    def char_to_int(character) : 
## 	for i in range(256) : 
##            if(chr(i) == character) : 
##                return i
##    index = char_to_int(character) - 65
##    return len(l[index])

# print(get_max_no_of_blocks('b'))

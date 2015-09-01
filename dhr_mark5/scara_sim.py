import time
import Tkinter as tk
import py_main

parameter_list = [0,1,1,2,3,5,8,13,21,34]*2

print(parameter_list)

OCCURENCE_LIST = [4, 2, 1, 1, 3, 1, 1, 2, 3, 1, 1, 2, 2,\
                  3, 4, 1, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1]
max_length = 10

def default_values(gui_object):
    print parameter_list
    print(gui_object)
    print(type(gui_object))
    for i in range(gui_object.param_numbers):
        print i,
        gui_object.label_list[i].set(str(parameter_list[i]))
    
    #gui_object.label_list[5].set(str(677))

def check_string(text):
    global OCCURENCE_LIST
    print("checking string => "+text)
    if(len(text) > max_length):
        return False
    g=[]
    for i in range(26):
        g.append(text.count(chr(i+65)))
##    print g
##    print OCCURENCE_LIST
    d = [x<=y for x,y in zip(g,OCCURENCE_LIST)]
##    print d
    if False in d:
##        print("BAA-DUM-TSS")
        return False
    return alphabet_checker(text)

def alphabet_checker(text):
    g = []
    g = [x.isalpha() or x.isspace() for x in text]
    if False in g:return False
    if text.count(" ")>1:return False
    return True
    
def called_by_GUI(obj,progress_page,string):
    print("receiving controool")

    py_main.CURRENT_ARRAY = list(string)
    py_main.modify_blocks(obj)
    obj.deiconify()
    progress_page.destroy()
    print("trying to open button")
    print("returning control")



##def called_by_GUI(obj,progress_page,string):
##    print("receiving controool")
##    #'call write function'
##    global FLAG
##    global_string=''
##    #obj.close_button()
##    print(string)
##    print(len(string))
##    FLAG = False
##    for i in range(len(string)):
##        if(FLAG):
##            print 'interrupted flag status in scara_sim--> called_by_GUI'
##            break
##        modify_blocks()
##        print('SUCCESS--> '+string[i]+'\n')
##        global_string+=string[i]+'....'
##        obj.update_label(global_string)
##        #obj.but.config(state=obj.NORMAL)
##        #delay:tanik sustaye lo do second ke liye
##        
##        time.sleep(2)
##    FLAG = True
##    obj.deiconify()
##    progress_page.destroy()
##    print("trying to open button")

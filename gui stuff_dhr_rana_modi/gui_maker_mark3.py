from Tkinter import *


class window_maker:

    def __init__(self,*args):
        
        self.root = Tk()
        self.line_number = 0
        # self.frame_array = []
        self.main_funct(args)
       
    def main_funct(self,args):   
        self.make_new_frame()
        
        for obj in args:
            if(type(obj) == int):
                print("That line please")
                self.make_new_frame()
                
                while(self.line_number < obj):
                    empty_label.create(self.current_frame)
                    self.make_new_frame()
                    
            elif(obj.name == "button"):
                obj.create(self.current_frame)
                print("creating button...")
            elif(obj.name == "label"):
                obj.create(self.current_frame)
                print("creating label...")
            elif(obj.name == "input_box"):
                obj.create(self.current_frame)
                print("creating input_box...")
                
        self.root.mainloop()
    
    def make_new_frame(self):
        print("PLEASE DEFINE ME")
        new_frame = Frame(self.root)
        new_frame.pack()
        # self.frame_array += new_frame
        self.current_frame = new_frame
        self.line_number += 1
        
class input_box_maker:
    
    def __init__(self):
        self.name = "input_box"
        pass
    
    def create(self,frame):
        self.input_box = Entry(frame)
        self.input_box.pack(side = LEFT)

class label_maker :
    
    def __init__(self, label_name, bg_color = "white", fg_color = "black"):
        self.name = "label"
        self.label_name = label_name
        self.bg_color = bg_color
        self.fg_color = fg_color
        
    def create(self, frame):
        self.label = Label(frame, text = self.label_name, bg = self.bg_color, fg = self.fg_color, font=("Times", 16, "bold") )
        self.label.pack(side = LEFT)
        
class button_maker:
    
    def __init__(self, text, bg_color = "white", fg_color = 'black', command = "none"):
        self.name = "button"
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.text = text
        self.command = command
        
    def create(self,frame):
        self.button = Button(frame, text = self.text, bg = self.bg_color, fg = self.fg_color, command = self.do_something)
        self.button.pack(side = LEFT)

    def do_something(self):
        if(self.command == "none"):
            print("I am doing NOTHING")
        else:
            print("NO COMMANDS DEFINED YET")
        
empty_label = label_maker("  ")
#---------------------------------------------

ok_button = button_maker("OK")

blue_button = button_maker("Blue", fg_color = "blue")

red_ok_button = button_maker("OK", fg_color = "red")

rana_label = label_maker("Rana")

input_box0 = input_box_maker()


win0 = window_maker(blue_button,ok_button,3,rana_label,5,input_box0,8,red_ok_button)
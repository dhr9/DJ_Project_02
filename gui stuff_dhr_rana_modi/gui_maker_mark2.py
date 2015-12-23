from Tkinter import *


class window_maker:

    def __init__(self,obj):
        
        self.root = Tk()
        self.frame0 = Frame(self.root)
        
        self.frame0.pack()   #CHECK LATER
        
        if(obj.name == "button"):
            self.button0 = obj     #CHANGE LATER
            self.make_button()        #CHANGE LATER
            print("you inputted a button")
        elif(obj.name == "label"):
            self.label0 = obj
            self.make_label()
            print("You inputted a label")
        elif(obj.name == "input_box"):
            self.input_box0 = obj
            self.make_input_box()

        self.root.mainloop()
    
    def make_button(self):
        self.button0.create(self.frame0)
    def make_label(self):
        self.label0.create(self.frame0)
    def make_input_box(self):
        self.input_box0.create(self.frame0)
        
class input_box_maker:
    
    def __init__(self):
        self.name = 'input_box'
    
    def create(self,frame):
        self.input_box = Entry(frame)
        self.input_box.pack(side = LEFT)       #check this nd the nxt line if it doesnt work
        #self.input_box.columnspan(2)

class label_maker :
    
    def __init__(self, label_name, bg_color = "white", fg_color = "black"):
        self.name = "label"
        self.label_name = label_name
        self.bg_color = bg_color
        self.fg_color = fg_color
        
    def create(self, frame):
        self.label = Label(frame, text = self.label_name, bg = self.bg_color, fg = self.fg_color, font=("Helvetica", 16) )
        self.label.pack()
        
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
        
ok_button = button_maker("OK")

blue_ok_button = button_maker("OK", fg_color = "blue")

red_ok_button = button_maker("OK", fg_color = "red")

rana_label = label_maker("Rana")

input_box0 = input_box_maker()

# win0 = window_maker(blue_ok_button)

# win1 = window_maker(rana_label)

win2 = window_maker(input_box0)
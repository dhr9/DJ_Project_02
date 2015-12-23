from Tkinter import *


class window_maker:

    def __init__(self,button):
        self.button0 = button     #CHANGE LATER
        
        self.root = Tk()
        self.frame0 = Frame(self.root)
        
        self.frame0.pack()   #CHECK LATER
        
        self.make_button()        #CHANGE LATER
        self.root.mainloop()
    
    def make_button(self):
        self.button0.create(self.frame0)

class input_box_maker:
    
    def __init__(self):
        pass
    
    def create(self,frame):
        self.input_box = Entry(frame)
        self.input_box.pack(side = LEFT)       #check this nd the nxt line if it doesnt work
        self.input_box.columnspan(2)

class label_maker :
    
    def __init__(self, label_name, bg_color = "white", fg_color = "black"):
        self.label_name = label_name
        self.bg_color = bg_color
        self.fg_color = fg_color
        
    def create(self, frame):
        self.label = Label(frame, self.label_name, bg_color = self.bg_color, fg_color = self.fg_color)
        self.label.pack()
        
class button_maker:
    
    def __init__(self, text, bg_color = "white", fg_color = 'black', command = "none"):
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

win0 = window_maker(blue_ok_button)

win1 = window_maker(red_ok_button)
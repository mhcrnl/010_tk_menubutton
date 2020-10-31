#!/usr/bin/env python3

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        
        # create a tkinter menubutton widget
        self.tk_mb= tk.Menubutton(self, text="Tkinter Widgets")
        self.tk_mb.pack(side="top")
        self.tk_mb["activebackground"] = "blue"
        self.tk_mb["activeforeground"] = "red"
        self.tk_mb["anchor"] = "sw"
        self.tk_mb["bg"]="yellow"
        #self.tk_mb["bitmap"]="info"
        self.tk_mb["bd"] = 5
        self.tk_mb["cursor"] = "dot"
        
        self.menu = tk.Menu(self.tk_mb, tearoff=3)
        self.tk_mb["menu"] = self.menu
        self.menu.add_checkbutton(label="Label")
        self.menu.add_checkbutton(label="Button")
        
        # create a button
        self.hi_there=tk.Button(self)
        self.hi_there["text"]="Salut, Lume!\n(click me)"
        self.hi_there["command"]=self.say_hi
        self.hi_there.pack(side="top")

        # create quit button
        self.quit=tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    # Function 
    def say_hi(self):
        print("Salut tuturor!")

root = tk.Tk()
root.title("Tkinter Menubutton")
root.geometry("600x750")
app=Application(master=root)
app.mainloop()

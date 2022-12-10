import tkinter
from tkinter import messagebox

from  tkinter import *

top =Tk()

def msg():
    messagebox.showinfo("Alert", "Button Clicked")

bt=Button(top ,text ="Click me", activeforeground="yellow" ,activebackground="yellow",command=msg)

bt.pack()

top.mainloop()














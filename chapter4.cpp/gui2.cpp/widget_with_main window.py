#CREATING  ANOTHER WINDOW FROM MAIN BUTTON

from tkinter import*

root = Tk()

root.geometry("200x200")

def open():
    top =Toplevel(root)
    top.mainloop()

btn = Button(root,text="open",command =open)    

btn.place(x=75,y=50)

root.mainloop()
from re import I
import tkinter
from tkinter import*

top=Tk()

top.geometry("12343x12333")

lbl =Label(top,text="A list of favourite countries...")

listbox=Listbox(top)

listbox.insert(1,"india")


listbox.insert(2,"USA")

listbox.insert(3,"Japan")

listbox.insert(4,"Australia")

#this button will delete the selected item from the list 
#btn

btn =Button(top,text ="delete",command=lambda listbox=listbox:listbox.delete(ANCHOR))

lbl.pack()
listbox.pack()

btn.pack()
top.mainloop()




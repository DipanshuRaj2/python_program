#how to design gui on windows

# Tkinter geometry method
#pack()
#grid()
#place()

import tkinter 
from tkinter import*


from  tkinter import messagebox

top=Tk()  #MAKE CLASS #tk (tool kit)

# b1 =Button(top, text ="Red", fg="Red", bg="White")

# b1.pack(side =TOP)

# b2 =Button(top , text ="blue",fg ="blue", bg ="white")

# b2.pack(side=LEFT)

top.title("GUI") # title in built function0

l1 = Label(top , text ="Name")

l1.grid(row=0, column=0)

t1 =Entry(top)
t1. grid(row =0 ,column =1)


l2 =Label(top ,text ="Password")
l2.grid(row=1,column=0)

t2=Entry (top)
t2.grid(row=1 , column=1)

b1=Button(top , text ="Submit")
b1.grid(row=3,column=0)

#top=Tk()
# l1=Label(top,text="Name")

# l1.place(x=10,y=10)

# t1=Entry(top)

# t1.place(x=30 , y=20)

top.mainloop()

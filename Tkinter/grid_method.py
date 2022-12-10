'''
Phython Tkinter grid() method
1.It is the type of Phython Tkinter Geometry
2.It is one of them in the out of 3(The pack()method),(The grid() method),(The place()method)
3.we can also specify the column span  or rowspan of a widget.
3.The grid()geometry manager organizes the widgets in the tabular form.
4.widget.grid(options)
'''
import tkinter
from tkinter import *

parent = Tk()

#create label name
name = Label(parent,text ='Name').grid(row = 0, column = 0)

#create textbox for name
e1 = Entry(parent).grid(row = 0, column = 1)

#create label password
password = Label(parent,text ='Password😊😊').grid(row = 1 , column = 0)

#create textbox for password
e2 = Entry(parent).grid(row = 1, column = 1)

#create submit button
submit = Button(parent, text ='Submit').grid(row = 4, column = 0)
parent.mainloop()
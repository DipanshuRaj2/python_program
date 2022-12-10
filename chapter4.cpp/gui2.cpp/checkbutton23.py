import tkinter
from tkinter import*
top =Tk()

top.geometry("200x200")

checkvar1 = IntVar()

checkvar2 =IntVar()

checkvar3 =IntVar()

chkbtn1 =Checkbutton(top,text="C", variable=checkvar1,onevalue=1,offvalue=0,height=2,width=10)
chkbtn2 =Checkbutton(top,text="C++", variable=checkvar2,onevalue=1,offvalue=1,height=2,width=10)
chkbtn3 =Checkbutton(top,text="Java", variable=checkvar3,onevalue=1,offvalue=0,height=2,width=10)
chkbtn1.pack()
chkbtn2.pack()
chkbtn3.pack()
top.mainloop()


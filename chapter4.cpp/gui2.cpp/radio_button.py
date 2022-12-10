#radio button++++++++++++++++++++++++++++

#RADIO BUTTON V/S CHECK BUTTON

from cProfile import label
from distutils.util import run_2to3
from msilib import RadioButtonGroup
from tkinter import*

def selection():
    ##selection is in built function
    selection="You selected the option "+str(Radiobutton.get())
label.config(text =selection)

top =Tk()
top.geometry("300x150")
radio =IntVar()
lbl =label(text="Your favourite programming language")
lbl.pack()

R1=Radiobutton(top,text="C", variable=radio, value=1,command=selection)
R1.pack(anchor =W)

R2=Radiobutton(top,text="C++", variable=radio, value=3,command=selection)
R2.pack(anchor =W)
R3=Radiobutton(top,text="C", variable=radio, value=4,command=selection)
R3.pack(anchor =W)

label =label(top)
label.pack()
top.mainloop()



            

    


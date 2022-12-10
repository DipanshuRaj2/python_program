'''
Phyton Tkinter pack()method
!.It is the type of Phython Tkinter Geometry
2.It is one of them in the out of 3(The pack()method),(The grid() method),(The place()method)
3.we use different possible option like expand , fill and size.

The pack() widget is used to organize widget in the block. 
The positions widgets added to the python application 
using the pack() method can be controlled by using the 
various options specified in the method call.
'''
#create button in phython with the help of Tkinter

import tkinter
from tkinter import *

parent =Tk()

redbutton =Button(parent, text ='Red', fg ='purple')
redbutton.pack(side =LEFT)

greenbutton =Button(parent, text ='Black', fg ='black')
greenbutton.pack(side = RIGHT)

bluebutton =Button(parent, text = 'Blue', fg = 'blue')
bluebutton.pack(side = TOP )

blackbutton = Button(parent, text = 'Green', fg ='red')
blackbutton.pack( side = BOTTOM)

parent.mainloop()

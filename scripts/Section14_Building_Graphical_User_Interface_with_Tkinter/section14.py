##
## Graphical Utility..
##

from tkinter import *

window = Tk()   # This is the main window of the application

def km_to_miles():
    #print(e1_value())
    miles=float(e1_value.get())*1.6
    t1.insert(END,miles)

b1 = Button(window,text="Execute",command=km_to_miles)
b1.grid(row=0,column=0)

e1_value = StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

window.mainloop()   # this is required at the end of the app. This keeps the window open till the time the X is presed to close it.

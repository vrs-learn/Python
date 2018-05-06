#
#

from tkinter import *

window = Tk()

def conversion():
    t1.delete(0.1,END)
    t3.delete(0.1,END)
    t2.delete(0.1,END)
    grams=float(e1_value.get())*1000
    pound=float(e1_value.get())*2.20462
    ounces=float(e1_value.get())*35.274
    t1.insert("1.0",str(grams) +' grams')
    t2.insert("1.0",str(pound) +' pounds')
    t3.insert(END,ounces)


b1 = Button(window,text="Convert",command=conversion)
b1.grid(row=0,column=2)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

l1=Label(window,text="Enter Value in Kg:",font='arial 10')
l1.grid(row=0,column=0)


t1=Text(window,height=1,width=20)
t1.grid(row=2,column=0)

label1=Label(window,text="Grams")
label1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=2,column=1)

label2=Label(window,text="Pounds")
label2.grid(row=1,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=2,column=2)

label3=Label(window,text="Ounces")
label3.grid(row=1,column=2)

window.mainloop()

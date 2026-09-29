from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.geometry("500x500")

def transport():
    f = name.get() +  " " + age.get() + " " +  contact.get() + " " + country.get()
    box.insert(END,f)

title = Label(window,text = "Student Entry Portal",width = 15)
title.place(x=200,y=20)
name = Entry(window,width = 15)
age = Entry(window,width = 15)
contact = Entry(window,width = 15)
country = Entry(window,width = 15)
name.place(x=140,y=100)
age.place(x=140,y=130)
contact.place(x=140,y=160)
country.place(x=140,y=190)
nam = Label(window,text = "Name",width = 10)
ag = Label(window,text = "Age",width = 10)
contac = Label(window,text = "Contact",width = 10)
countr = Label(window,text = "Country",width = 10)
nam.place(x=60,y=100)
ag.place(x=60,y=130)
contac.place(x=60,y=160)
countr.place(x=60,y=190)
box = Listbox(window,width = 30)
box.place(x = 300 , y = 100)   
bu = Button(window,text = "Press to transport details",width = 20,command = transport)
bu.place(x = 130 , y = 220)


window.mainloop()

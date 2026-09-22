from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *

window = Tk()
window.geometry("400x500")

def press():
    a = en.get()
    lis.insert(END,a)

def delete():
    b = lis.curselection()
    if b:
        lis.delete(b[0])

def delete_all():
    lis.delete(0,END)

def save_file():
    output = asksaveasfile(defaultextension = ".txt")
    if output is not None:
        for i in lis.get(0,END):
            print(i,file = output)

def open_file():
    input = askopenfile(title = "openfile")
    if input is not None:
        c = input.readlines()
        for i in c:
            lis.insert(END,i)

    
en = Entry(window,width = 15)
bu = Button(window,text = "Add",width = 18,command = press)
lis = Listbox(window,width = 20,height = 15)
de = Button(window,text = "Delete",command = delete)
dea = Button(window,text = "Delete all",command = delete_all)
save = Button(window,text = "Click to save as file",width = 19,command = save_file)
open = Button(window,text = "Click to view file",width = 15,command = open_file)
en.place(x=100,y=20)
bu.place(x=100,y=60)
lis.place(x=30,y=100)
de.place(x=50,y=350)
dea.place(x=50,y=400)
save.place(x=50,y=425)
open.place(x=50,y = 450)

window.mainloop()
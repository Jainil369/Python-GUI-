from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.geometry("400x400")
window.title("Address Book")

def add():
    g = name.get()
    if g in check.keys():
        check[g] = (address.get(),mobile.get(),email.get(),birthday.get())
    else:
        f = name.get() +  " " + address.get() + " " +  mobile.get() + " " + email.get() + " " + birthday.get()
        lis.insert(END,f)
        check[g] = (address.get(),mobile.get(),email.get(),birthday.get())
        name.delete(0,END)
        address.delete(0,END)
        mobile.delete(0,END)
        email.delete(0,END)
        birthday.delete(0,END)
        
def Delete():
    y = lis.curselection()
    if y:
        del check[lis.get(y[0]).split()[0]]
        lis.delete(y[0])

def Edit():
    y = lis.curselection()
    if y:
        x = lis.get(y[0]).split()
        name.insert(0,x[0])
        address.insert(0,x[1])
        mobile.insert(0,x[2])
        email.insert(0,x[3])
        birthday.insert(0,x[4])
        check[x[0]] = (address.get(),mobile.get(),email.get(),birthday.get())

def Delete_all():
    lis.delete(0,END)
    del check

def save_file():
    output = asksaveasfile(defaultextension = ".txt")
    if output is not None:
        for i,j in check.items():
            print(i + " " +  " ".join(j) ,file = output)

def open_file():
    input = askopenfile(title = "openfile")
    if input is not None:
        c = input.readlines()
        for i in c:
            k = i.split()
            check[k[0]] = [k[1],k[2],k[3],k[4]]
        transport()

def transport():
    lis.delete(0,END)
    for i,j in check.items():
        lis.insert(END,(i + " " + " ".join(j)))

check = {}

title = Label(window,text = "My Address Book")
title.place(x=80,y=10)
open = Button(window,text = "Open",command = open_file)
open.place(x=220,y=8)
lis = Listbox(window,width = 30,height = 12)
lis.place(x=10,y=50)
nam = Label(window,text = "Name:")
nam.place(x=230,y=50)
name = Entry(window,width = 10)
name.place(x=290,y=50)
addres = Label(window,text = "Address:")
addres.place(x=230,y=90)
address = Entry(window,width = 10)
address.place(x=290,y=90)
mobil = Label(window,text = "Mobile:")
mobil.place(x=230,y=130)
mobile = Entry(window,width = 10)
mobile.place(x=290,y=130)
emai = Label(window,text = "Email:")
emai.place(x=230,y=170)
email = Entry(window,width = 10)
email.place(x=290,y=170)
birthda = Label(window,text = "Birthday:")
birthda.place(x=230,y=210)
birthday = Entry(window,width = 10)
birthday.place(x=290,y=210)
edit = Button(window,text = "Edit",width = 10,command = Edit)
edit.place(x=20,y=270)
delete = Button(window,text = "Delete",width = 10,command = Delete)
delete.place(x=110,y=270)
updat = Button(window,text = "Update/Add",command = add)
updat.place(x=260,y=270)
save = Button(window,text = "Save",width = 25,command = save_file)
save.place(x=60,y=300)
delete_all = Button(window,text = "Delete All",command = Delete_all)
delete_all.place(x=260,y=300)






window.mainloop()


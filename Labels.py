from tkinter import *
import random

window = Tk()
window.geometry("400x400")

def check():
    check1 = username.get()
    check2 = password.get()
    if check1 == "Jainil" and check2 == "Good":
        message.config(text="Login successful")
    else:
        message.config(text="Login unsuccessful")


message = Label(window,text="")
Login = Label(window,text="Login")
label1 = Label(window,text="username")
label2 = Label(window,text="password")
username = Entry(window,width=20)
password = Entry(window,width=20)
Submit = Button(window,text="Submit",command = check)
username.place(x = 180,y = 100)
label1.place(x=100,y=100)
label2.place(x=100,y=150)
password.place(x=180,y=150)
Login.place(x=100,y=50)
Submit.place(x=100,y=200)
message.place(x=100,y=250)

window.mainloop()
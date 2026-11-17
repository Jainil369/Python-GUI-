from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import tkinter.messagebox

window = Tk()
window.geometry("400x400")

def submit():
    a = ans.get()
    b = ans2.get()
    c = answer3.get()
    d = "Q1) " + a +  "\nQ2) " +  b + "\nQ3) " +  str(c)
    tkinter.messagebox.showinfo("Survey details", d )


title = Label(window,text = "2026 Survey")
title.place(x=150,y=5)
question1 = Label(window,text = "1) What is your favourite sport?")
question1.place(x = 10,y=25)
ans = StringVar()
answer1_1 = Radiobutton(window,text = "Football",variable = ans,value = "Football")
answer1_1.place(x = 20,y=45)
answer1_2 = Radiobutton(window,text = "Basketball",variable = ans,value = "Basketball")
answer1_2.place(x = 20,y=65)
answer1_3 = Radiobutton(window,text = "Cricket",variable = ans,value = "Cricket")
answer1_3.place(x=20,y=85)
question2 = Label(window,text = "2) What is your favourite food?")
question2.place(x=10,y=120)
ans2 = StringVar()
answer2 = Combobox(window,textvariable = ans2,width = 15)
answer2["values"] = ["Pizza","Pasta","Wrap","Salad","Sandwich"]
ans2.set("Pick food")
answer2.place(x=20,y=145)
question3 = Label(window,text = "3) What is your age?")
question3.place(x=10,y=180)
answer3 = Entry(window,width = 10)
answer3.place(x = 20,y = 205)
submit = Button(window,text = "Submit",command = submit)
submit.place(x=10,y=230)





window.mainloop()
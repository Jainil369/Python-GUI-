from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

window = Tk()
window.geometry("400x400")

title = Label(window,text = "2026 Survey")
title.place(x=150,y=5)
question1 = Label(window,text = "1)What is your favourite sport?")
question1.place(x = 10,y=25)
ans = StringVar()
answer1_1 = Radiobutton(window,text = "Football",variable = ans,value = "Football")
answer1_1.place(x = 20,y=45)
answer1_2 = Radiobutton(window,text = "Basketball",variable = ans,value = "Basketball")
answer1_2.place(x = 20,y=60)
answer1_3 = Radiobutton(window,text = "Cricket",variable = ans,value = "Cricket")
answer1_3.place(x=20,y=75)



window.mainloop()
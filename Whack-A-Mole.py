from tkinter import *
import random

window = Tk()
frame = Frame(window,bg = "green")
window.geometry("400x400")

def rand():
    a = random.choice(lis)
    a.configure(image = mole)

title = Label(window,text = "Whack-A-Mole Game",font = ("Arial",15,"bold"))
title.place(x=100,y=10)
frame.place(x=30,y=50)
mole = PhotoImage(file = "images/Mole.png")
hole = PhotoImage(file = "images/Hole.png")
lis = []
start = Button(window,text = "Start",command = rand)
start.place(x=300,y=10)
for i in range(3):
    for n in range(3):
        buton = Button(frame, image = hole,bg = "green",relief = "flat")
        buton.grid(row = i,column = n)
        lis.append(buton)



window.mainloop()
from tkinter import *
import random

window = Tk()
frame = Frame(window,bg = "green")
window.geometry("400x400")
a = 0
score = 0

def rand():
    global a
    for i in range(9):
        lis[i].configure(image = hole)
    a = random.randint(0,8)
    lis[a].configure(image = mole)
    window.after(900,rand)
    
def click(pos):
    global a 
    global score
    if lis[a] == lis[pos]:
        lab.configure(text = "Congrats")
        score += 1
        side.configure(text = "Score = " + str(score))
    lab.after(1000,clear)   

def clear():
     lab.configure(text = "")

title = Label(window,text = "Whack-A-Mole Game",font = ("Arial",15,"bold"))
title.place(x=100,y=10)
frame.place(x=30,y=50)
lab = Label(window,text = "")
lab.place(x = 200,y=370)
mole = PhotoImage(file = "images/Mole.png")
hole = PhotoImage(file = "images/Hole.png")
lis = []
side = Label(window,text = "Score = " + str(score))
side.place(x = 340,y=10)
start = Button(window,text = "Start",command = rand)
start.place(x=300,y=10)
r = 0
c = 0
for i in range(9):
        buton = Button(frame, image = hole,bg = "green",relief = "flat",command = click(i))
        lis.append(buton)
        buton.grid(row = r,column = c)
        c += 1
        if (i + 1) % 3 == 0:
             r += 1
             c = 0


window.mainloop()
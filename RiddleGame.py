from tkinter import *
import random

window = Tk()
window.geometry("400x400")
b = ""

def pick():
    global b
    #print(type(riddles.keys()))
    b = random.choice(list(riddles.keys()))
    riddle.configure(text = b)

def check():
    global b 
    if answer.get() == riddles[b]:
        congrats.configure(text = "You got it correct")
    else:
        congrats.configure(text = "You got it wrong")


riddles = {"What has to be broken before you can use it?": "An egg", "I’m tall when I’m young, and I’m short when I’m old. What am I?":"A candle"}
title = Label(window,text = "Riddle game")
title.place(x=150,y=10)
rand = Button(window,text = "Press to generate a riddle",command = pick)
rand.place(x=80,y=30)
riddle = Label(window,text = "")
riddle.place(x=10,y=70)
answer = Entry(window)
answer.place(x=100,y=100)
submit = Button(window,text = "Submit",command = check)
submit.place(x=100,y=130)
congrats = Label(window,text = "")
congrats.place(x=50,y=150)

window.mainloop()
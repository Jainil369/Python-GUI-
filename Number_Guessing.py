from tkinter import *
import random

window = Tk()
window.geometry("250x200")
window.configure(bg = "light blue")

random_num = random.randint(0,20)

def checks():
    if random_num == int(answer.get()):
        congrats.configure(text = "Congratulations you guessed it correctly")
    else:
        congrats.configure(text = "You guessed wrong try again")

def things():
    if random_num > int(answer.get()):
        hints.configure(text = "The number is higher")
    elif random_num < int(answer.get()):
        hints.configure(text = "The number is lower")

def combined_command():
    checks()
    things()

def reset():
    global random_num
    random_num = random.randint(1,20)


title = Label(window,text = "Number Guessing Game",bg = "light blue")
title.place(x=30,y=10)
instructions = Label(window,text = "Guess a number from 1 to 20",bg = "light blue")
instructions.place(x=10,y = 30)
answer = Entry(window,width = 8,bg = "light blue")
answer.place(x=50,y=55)
check = Button(window,text = "Press if finsished",command = combined_command)
check.place(x=40,y=75)
congrats = Label(window,text = "",bg = "light blue")
congrats.place(x=5,y=110)
hints = Label(window,text = "",width = 25,bg = "light blue")
hints.place(x=20,y=130)
press = Button(window,text = "Press to play again" , width = 15,command = reset)
press.place(x = 20,y=170)
window.mainloop()

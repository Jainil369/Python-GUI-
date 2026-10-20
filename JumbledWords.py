from tkinter import *
import random

window = Tk()
window.geometry("400x400")
b = ""

def jumble():
    global b
    b = random.choice(words)
    a = list(b)
    random.shuffle(a)
    c = "".join(a)
    jumb.configure(text = c)

def check():
    if ent.get() == b:
        congrats.configure(text = "Congratulations.The word is correct")
    else:
        congrats.configure(text = "Sorry.It is wrong.Try again")

words = ["happy","crazy","sad","carrot","apple"]
title = Label(window,text = "Jumbled Words")
title.place(x=150,y=10)
tries = Button(window,text = "Press to generate a jumbled word",command = jumble)
tries.place(x=75,y=30)
ent = Entry(window,)
ent.place(x=200,y=60)
jumb = Label(window,text = "")
jumb.place(x=100,y=60)
submit = Button(window,text = "Submit",command = check)
submit.place(x=150,y=70)
congrats = Label(window,text = "")
congrats.place(x=50,y=100)
a = list("happy")
random.shuffle(a)
print("".join(a))

















window.mainloop()
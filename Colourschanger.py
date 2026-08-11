from tkinter import *
import random

window = Tk()
window.geometry("400x400")
window.configure(bg = "red")
colours = ["red","orange","blue","green"]
def colourchanger():
    colour = random.choice(colours)
    window.configure(bg = colour)

label = Label(window,text = "hello")
label.place(x = 200,y = 100)
button = Button(window,text = "Click me",command = colourchanger)
button.place(x = 200,y = 200)




window.mainloop()

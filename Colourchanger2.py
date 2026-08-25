from tkinter import *
import random

window = Tk()
window.geometry("400x400")
window.configure(bg = "black")

def red():
    window.configure(bg = "red")

def blue():
    window.configure(bg = "blue")

def green():
    window.configure(bg = "green")

red = Button(window, text = "Red", command = red)
red.place(x = 200,y = 200)
green = Button(window, text = "Green" , command = green)
green.place(x = 100,y = 100)
blue = Button(window, text = "Blue", command = blue)
blue.place(x = 300,y= 300)
window.mainloop()
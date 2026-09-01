from tkinter import *
import random 
import tkinter.font as font

window = Tk()
window.geometry("600x400")
window.configure(bg = "light blue")

Rock = Button(window,text = "Rock",width = 6)
Paper = Button(window,text = "Paper",width = 6)
Scissors = Button(window,text = "Scissors",width = 6)
Title = Label(window,text = "Rock,Paper,Scissors",font = font.Font(size = 30),bg= "light blue" )
Options = Label(window,text = "Your options",font = font.Font(size = 10),fg = "grey",bg = "light blue")

Rock.place(x=150,y=100)
Paper.place(x=225,y=100)
Scissors.place(x=300,y=100)
Title.place(x=100,y=25)
Options.place(x=50,y=100)

window.mainloop()
from tkinter import *
from time import strftime
import tkinter.font as font

window = Tk()
window.geometry("300x100")


clock = Label(window,text = "",font = font.Font(size = 20))
clock.pack(anchor = "center",side = "bottom")
title = Label(window,text="Digital Clock",font = font.Font(size = 20))
title.place(x=75,y=10)

def current_time():
    time = strftime("%H:%M:%S %p")
    clock.config(text = time)
    clock.after(1000,current_time)
current_time()
window.mainloop()
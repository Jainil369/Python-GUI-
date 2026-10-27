from tkinter import *
from gtts import gTTS
import os

window = Tk()
window.geometry("400x400")

def transform():
    language = "en"
    a = gTTS(text = ent.get(),lang = language,slow = False)
    a.save("a.wav")
    #os.system("a.wav")

title = Label(window,text = "Text to Speech")
title.place(x=130,y=10)
ent = Entry(window)
ent.place(x=210,y=40)
submit = Button(window,text = "Submit",command = transform)
submit.place(x=210,y=60)


window.mainloop()
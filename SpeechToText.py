from tkinter import *
import speech_recognition as sr
from tkinter.ttk import *
from tkinter.filedialog import *

window = Tk()
window.geometry("400x400")

def recorder():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            txt = r.recognize_google()
        except:
            txt = "Sorry.Voice cannot be recongised"
        text.delete(1.0,END)
        text.insert(END,txt)


title = Label(window,text = "Speech to Text")
title.place(x=130,y=10)
record = Button(window,text = "Press to record",command = recorder)
record.place(x=40,y=30)
play = Button(window,text = "Press to play")
play.place(x=200,y=30)
text = Text(window)
text.place(x=40,y=60)


window.mainloop()
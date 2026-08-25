from tkinter import *

window = Tk()
window.geometry("400x400")

def convert():
    degrees = int(Enter.get())
    Fahrenheit = (degrees*1.8) + 32
    Answer.config(text=str(degrees) + " degrees celsius is equal to "  +  str(Fahrenheit) + "degrees Fahrenheit")

Answer = Label(window,text = "")
Answer.place(x=100,y=250)
Click = Label(window,text=("Enter your degrees"))
Click.place(x=100,y=100)
Enter = Entry(window,width = 20)
Enter.place(x=210,y=100)
Convert = Button(window,text="Click to convert into fahrenheit",command = convert)
Convert.place(x=100,y=150)

window.mainloop()
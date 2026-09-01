from tkinter import *

window = Tk()
window.geometry("400x400")
window.configure(bg = "black")

def adds():
    answer.config(text = int(num1.get()) + int(num2.get()))

def subtracts():
    answer.config(text=int(num1.get()) - int(num2.get()))

def multiplys():
    answer.config(text = int(num1.get()) * int(num2.get()))

def divides():
    answer.config(text =  int(num1.get()) / int(num2.get()))

num1 = Entry(window,width=10)
num2 = Entry(window,width=10)
add = Button(window,text="+",width=4,command = adds)
subtract = Button(window,text="-",width=4,command =subtracts)
multiply = Button(window,text="x",width=4,command = multiplys)
divide = Button(window,text="/",width=4,command = divides)
answer = Label(window,text = "",width=4)

num1.place(x=50,y=50)
num2.place(x=150,y=50)
add.place(x=50,y=100)
subtract.place(x=100,y=100)
multiply.place(x=50,y=150)
divide.place(x=100,y=150)
answer.place(x=200,y=125)

window.mainloop()
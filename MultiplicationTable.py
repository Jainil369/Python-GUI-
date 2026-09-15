from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry("400x500")
window.configure(bg = "light blue")

def generate_table():
    numbers = ""
    v = num.get()
    for i in range(num2.get() + 1):
        numbers +=  str(v) + " x " + str(i) + "=" + str(i * v) +  "\n"
    table.configure(text = numbers)
        
        

Title = Label(window,text = "Multiplication Table",width = 25)
Title.place(x=110,y=20)
num = IntVar()
number_box = Combobox(window,textvariable = num,width = 15)
number_box["values"] = tuple(range(1,51))
num.set(1)
number_box.place(x=130,y=60)
num2 = IntVar()
r1 = Radiobutton(window,text = "10",variable = num2,value = 10)
r2 = Radiobutton(window,text = "15",variable = num2,value = 15)
r3 = Radiobutton(window,text = "20",variable = num2,value = 20)
num2.set(10)
r1.place(x=110,y=100)
r2.place(x=160,y=100)
r3.place(x=210,y=100)
click = Button(window,text = "Click on me",command = generate_table)
click.place(x=100,y=150)
table = Label(window,text = "")
table.place(x=100,y=180)

window.mainloop()
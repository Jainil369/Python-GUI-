from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry("400x400")
window.configure(bg = "light blue")

def order():
    a = num1.get()
    b = num2.get()
    pizza = Label(window,text = "Your pizza contains " + str(a) + " and the size is " + str(b) )
    pizza.place(x=100,y=200)

Title = Label(window,text = "Order your pizza",width = 25)
Title.place(x=110,y=20)
num1 = StringVar()
toppings = Combobox(window,textvariable = num1,width = 15)
toppings["values"] = ["Pepper","Sweetcorn","Jalapeno","Olives","Mushrooms","Mozzarella"]
num1.set("Pick toppings")
toppings.place(x=130,y=60)
num2 = StringVar()
s1 = Radiobutton(window,text = "Small",variable = num2,value = "small")
s2 = Radiobutton(window,text = "Medium",variable = num2,value = "medium")
s3 = Radiobutton(window,text = "Large",variable = num2,value = "large")
num2.set(10)
s1.place(x=100,y=100)
s2.place(x=155,y=100)
s3.place(x=230,y=100)
click = Button(window,text = "Click here to generate order",width = 35,command = order)
click.place(x=95,y=160)

window.mainloop()
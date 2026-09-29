from tkinter import *

window = Tk()
window.geometry("400x400")
frame = Frame(window)
turn = "X"

def winning():
    if b1.cget("text") == b2.cget("text") == b3.cget("text") != "":
        print("you won")

def b1_choice():
    global turn
    if b1.cget("text") == "":
        if turn == "X":
            b1.configure(text = "X")
            turn = "O"
        elif turn == "O":
            b1.configure(text = "O") 
            turn = "X"

def b2_choice():
    global turn
    if b2.cget("text") == "":
        if turn == "X":
            b2.configure(text = "X")
            turn = "O"
        elif turn == "O":
            b2.configure(text = "O") 
            turn = "X"

def b3_choice():
    global turn
    if b3.cget("text") == "":
        if turn == "X":
            b3.configure(text = "X")
            turn = "O"
        elif turn == "O":
            b3.configure(text = "O") 
            turn = "X"
    winning()

def b4_choice():
    global turn
    if b4.cget("text") == "":
        if turn == "X":
            b4.configure(text = "X")
            turn = "O"
        elif turn == "O":
            b4.configure(text = "O") 
            turn = "X"

def b5_choice():
    global turn
    if b5.cget("text") == "":
        if turn == "X":
            b5.configure(text = "X")
            turn = "O"
        elif turn == "O":
            b5.configure(text = "O") 
            turn = "X"

def b6_choice():
    global turn
    if b6.cget("text") == "":
        if turn == "X":
            b6.configure(text = "X")
            turn = "O"
        elif turn == "O":
            b6.configure(text = "O") 
            turn = "X"

def b7_choice():
    global turn
    if b7.cget("text") == "":
        if turn == "X":
            b7.configure(text = "X")
            turn = "O"
        elif turn == "O":
            b7.configure(text = "O") 
            turn = "X"

def b8_choice():
    global turn
    if b8.cget("text") == "":
        if turn == "X":
            b8.configure(text = "X")
            turn = "O"
        elif turn == "O":
            b8.configure(text = "O") 
            turn = "X"

def b9_choice():
    global turn
    if b9.cget("text") == "":
        if turn == "X":
            b9.configure(text = "X")
            turn = "O"
        elif turn == "O":
            b9.configure(text = "O") 
            turn = "X"

title = Label(window,text = "Tic Tac Toe")
b1 = Button(frame,width = 10,text = "",command = b1_choice)
b2 = Button(frame,width = 10,text = "",command = b2_choice)
b3 = Button(frame,width = 10,text = "",command = b3_choice)
b4 = Button(frame,width = 10,text = "",command = b4_choice)
b5 = Button(frame,width = 10,text = "",command = b5_choice)
b6 = Button(frame,width = 10,text = "",command = b6_choice)
b7 = Button(frame,width = 10,text = "",command = b7_choice)
b8 = Button(frame,width = 10,text = "",command = b8_choice)
b9 = Button(frame,width = 10,text = "",command = b9_choice)
title.place(x=150,y=15)
frame.place(x=50,y=100)
b1.grid(row = 15,column = 3)
b2.grid(row = 15,column = 4)
b3.grid(row = 15,column = 5)
b4.grid(row = 16,column = 3)
b5.grid(row = 16,column = 4)
b6.grid(row = 16,column = 5)
b7.grid(row = 17,column = 3)
b8.grid(row = 17,column = 4)
b9.grid(row = 17,column = 5)
window.mainloop()
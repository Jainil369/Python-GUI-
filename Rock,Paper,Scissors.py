from tkinter import *
import random 
import tkinter.font as font

window = Tk()
window.geometry("600x400")
window.configure(bg = "light blue")
choices = ["Rock","Paper","Scissors"]
score = 0
scores = Label(window,text = "Your score is " + str(score), width = 13,bg = "light blue")
scores.place(x=310,y=160)
computer_score = 0
computer_scores = Label(window,text = "Computer score is " + str(computer_score),width=15,bg = "light blue")
computer_scores.place(x=315,y=200)

def Rocks():
    global score
    global computer_score
    computer_choice = random.choice(choices)
    Computer.config(text = "Computer has picked " + computer_choice) 
    if computer_choice == "Rock":
        answer.config(text = "There is a tie")
    if computer_choice == "Paper":
        answer.config(text = "Computer has won")
        computer_score += 1
        computer_scores.config(text = "Computer score is " + str(computer_score))
    if computer_choice == "Scissors":
        answer.config(text = "You have won")
        score += 1
        scores.config(text = "Your score is " + str(score))

def paper():
    global score
    global computer_score
    computer_choice = random.choice(choices)
    Computer.config(text = "Computer has picked " + computer_choice)
    if computer_choice == "Paper":
        answer.config(text = "There is a tie")
    if computer_choice == "Scissors":
        answer.config(text = "Computer has won")
        computer_score += 1
        computer_scores.config(text = "Computer score is " + str(computer_score))
    if computer_choice == "Rock":
        answer.config(text = "You have won")
        score += 1
        scores.config(text = "Your score is " + str(score))
        
def scissors():
    global score
    global computer_score
    computer_choice = random.choice(choices)
    Computer.config(text = "Computer has picked " + computer_choice) 
    if computer_choice == "Scissors":
        answer.config(text = "There is a tie")
    if computer_choice == "Paper":
        answer.config(text = "Computer has won")
        computer_score += 1
        computer_scores.config(text = "Computer score is " + str(computer_score))
    if computer_choice == "Rock":
        answer.config(text = "You have won")
        score += 1
        scores.config(text = "Your score is " + str(score))
        
Rock = Button(window,text = "Rock",width = 6,command = Rocks,)
Paper = Button(window,text = "Paper",width = 6,command = paper)
Scissors = Button(window,text = "Scissors",width = 6,command = scissors)
Computer = Label(window,text = "",width = 30,bg = "light blue")
Title = Label(window,text = "Rock,Paper,Scissors",font = font.Font(size = 30),bg= "light blue" )
Options = Label(window,text = "Your options",font = font.Font(size = 10),fg = "grey",bg = "light blue")
answer = Label(window,text = "",width = 18)

Rock.place(x=150,y=100)
Paper.place(x=225,y=100)
Scissors.place(x=300,y=100)
Title.place(x=100,y=25)
Options.place(x=50,y=100)
Computer.place(x=100,y=150)
answer.place(x=125,y=200)


window.mainloop()
from tkinter import *
from tkinter.simpledialog import askstring
from backend import request_methods
import time

BG_COLOR = "#353535"
TEXT = "#fdf0d5"
DANGER = "#bb2124"
RIGHT = "#40a944"
SCOREBRD = "#ffb703"


data = askstring(title="Quiz Subject",prompt="Choose any of subject from following : \n\n1. Geography\n2. Geography\n3. Sports").capitalize()
# data must be capitalized because dictionary has keys of this format



try:
    requestClass = request_methods(subject=data)
except Exception as e:
    requestClass = request_methods(subject="Computer")
    
# window declaration
window = Tk()

window.minsize(width=400,height=400)
window.config(background=BG_COLOR,padx=30,pady=50)
window.title("Quiz Application")

# functions for UI
def change_Back():
    canvas.config(bg = BG_COLOR)
    
def right_or_wrong(response="True"):
    if len(requestClass.questionList)>0:
        ans = requestClass.questionList[0]["ans"]
        
        if response==ans:
            requestClass.score +=1
            canvas.itemconfig(scoreboard,text=f"Score  {requestClass.score}")
            canvas.config(bg = RIGHT)
            canvas.after(800,change_Back)
            canvas.itemconfig(quizTxt, text = requestClass.nextQuestion())
            return
        canvas.config(bg = DANGER)
        canvas.after(800,change_Back)
        canvas.itemconfig(quizTxt, text = requestClass.nextQuestion())
    else:
        canvas.itemconfig(quizTxt, text = "FINISHED",fill=RIGHT, font=("Monospace",44))
        


# canvas area ... ... USING GRID SYSTEM
crossImg = PhotoImage(file="no.png")
TickImg = PhotoImage(file="yes.png")
canvas = Canvas(window, width=400,height=400, bg=BG_COLOR)   # if want to remove border  use as parameter with Canvas  --- highlightthickness=0
quizTxt = canvas.create_text(200,150,width=280,fill=TEXT,font=("Arial",20,"bold"),justify="center")
scoreboard = canvas.create_text(360,30,width=60,text="Score 0", fill=SCOREBRD,font=("Calibri",16,"bold"),justify="center")

canvas.grid(row=0,column=1,columnspan=2)

# Buttons part .... 
cancel = Button(image=crossImg,bg=BG_COLOR,command=lambda : right_or_wrong("False"))
accept = Button(image=TickImg,bg=BG_COLOR,command=right_or_wrong)
cancel.grid(row=1,column=1)
accept.grid(row=1,column=2)


canvas.itemconfig(quizTxt,text = requestClass.nextQuestion())

canvas.after_cancel(change_Back)  # must cancel the after affect
window.mainloop()
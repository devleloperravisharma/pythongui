import tkinter
from tkinter import *
import random
from tkinter import messagebox

root = Tk()
answers = ["mango", "megumi", "sukuna", "itadori", "minho", "nirvana", "boba", "afternoon", "acorn", "autumn", "winter", "spring", "summer", "tree", "strawberry", "blueberry", "snoopy", "woodstock", "christmas"]
words = ["gmano", "gummei", "aunksu", "riiodta", "ohmin", "aarvinn", "bboa", "ennaofotr", "ranco", "uutanm", "wirnte", "igrspn", "sremmu", "eter", "rasrertwby", "eluebbyrr", "ynospo", "oowkdstoc", "amscrsith"]
# global variables
num = random.randrange(0, len(words), 1)
correct_answer = 0
total_attempts = 0
score_text = ""
lbl = Label(root)

# reset function
def reset():
    global words, answers, num
    num = random.randrange(0, len(words), 1)
    lbl.config(text = words[num])
    e1.delete(0, END)

def default():
    global words, answers, num
    lbl.config(text = words[num])

# check for the answer
def checkanswer():
    global words, answers, num, correct_answer, total_attempts, score_text, lbl
    total_attempts = int(total_attempts) + 1
    ans_var = e1.get() # user input

    if ans_var == answers[num]:
        messagebox.showinfo("yayy !!", "it's the correct answer :)")
        correct_answer = int(correct_answer) + 1
    else:
        messagebox.showerror("whoops!", "it's wrong :(")
    score_text = "score:" +str(correct_answer)+ "/" + str(total_attempts)
    lbl.forget()
    lbl = Label(root, font = ("Roboto", 16), text = score_text, bg = "white")
    lbl.pack(side = LEFT)
    reset()

root.geometry("500x500")
root.title("jumbled word game")
root.configure(background = "#6E80AC")

Label(root, text = "jumbled word game", font = ("Roboto", 28), bg = "#6E80AC", fg = "#ffffff").pack(pady = 5)
lbl = Label(root, font = ("Roboto", 22), bg = "#6E80AC", fg = "#ffffff")
lbl.pack(pady=30, ipady =10, ipadx = 10)

ans = StringVar()
e1 = Entry(root, font = ("Roboto", 20), textvariable = ans)
e1.pack(ipady = 5, ipadx = 5)

Button(root, text = "check", font = ("Comic", 20), width = 10,
       bg = "#6E80AC", fg = "#ffffff", relief = GROOVE, command = checkanswer).pack(pady = 40)
Button(root, text = "reset", font = ("Comic", 20), width = 10,
       bg = "#6E80AC", fg = "#ffffff", relief = GROOVE, command = reset).pack()

default()
root.mainloop()



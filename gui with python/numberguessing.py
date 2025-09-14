import tkinter as tk
import tkinter.messagebox
import random

# create window
window = tk.Tk()
window.minsize(350, 260)
window.title("guess the number !!")

# logic of the game

# generate a random number between 1-20
number = random.randint(1,20)

# create a func to check the guess ><
def check_number():
    guess = text_guess.get()
    guess = int(guess)
    if guess > number:
        tkinter.messagebox.showinfo("high", "your guess is too high ! try again !")
    elif guess < number:
        tkinter.messagebox.showinfo("low", "your guess is too low !! try again !")
    else:
        tkinter.messagebox.showinfo("good", "good job !!")

# configure the name from the user !!
def btn_confirm():
    my_name = text_name.get()
    tkinter.messagebox.showinfo("name", "well then," + my_name + "i hope you win ! im thinking of a number 1-20, good luck !!")

# gui parttt !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# welcome label !
welcome = tkinter.Label(window, text = "welcome !!")
welcome.pack()

# name label
name_lbl = tk.Label(window, text = "what is your name ? ")
name_lbl.place(x = 10, y = 60)
text_name = tk.Entry(window, width = 20)
text_name.place(x = 10, y = 90)

# okk !!
ok_yay = tk.Button(window, text = "ok !", command = btn_confirm)
ok_yay.place(x = 200, y = 90, height = 28)

# guess input
guess = tk.Label(window, text = "take a guess !! ")
guess.place(x = 10, y = 150)
text_guess = tk.Entry(window, width = 10)
text_guess.place(x = 90, y = 150)

# guess button !
button_check = tk.Button(window, text = "guess", command = check_number)
button_check.place(x = 200, y= 150)

# finish !!
window.mainloop()
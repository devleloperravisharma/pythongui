from tkinter import *
from tkinter import messagebox
# create main window
window = Tk()
window.title("tic tac toe !!")
# global variables
turn = 1
result = ''
# the win() function to check all combinations(rows ,, columns ,, and diagonals)
def win():
    global result
    # checking for rows and column combonations
    if (b1.cget('text') == b2.cget('text') == b3.cget('text')) and b1.cget('text') != '':
        result = f"player {'1' if b1.cget('text') == 'x' else '2'} wins !!"
        messagebox.showinfo('result', result)
        window.destroy()
    elif (b4.cget('text') == b5.cget('text') == b6.cget('text')) and b4.cget('text') != '':
        result = f"player {'1' if b4.cget('text') == 'x' else '2'} wins !!"
        messagebox.showinfo('result', result)
        window.destroy()
    elif (b7.cget('text') == b8.cget('text') == b9.cget('text')) and b7.cget('text') != '':
        result = f"player {'1' if b7.cget('text') == 'x' else '2'} wins !!"
        messagebox.showinfo('result', result)
        window.destroy()
    elif (b1.cget('text') == b4.cget('text') == b7.cget('text')) and b1.cget('text') != '':
        result = f"player {'1' if b1.cget('text') == 'x' else '2'} wins !!"
        messagebox.showinfo('result', result)
        window.destroy()
    elif (b2.cget('text') == b5.cget('text') == b8.cget('text')) and b2.cget('text') != '':
        result = f"player {'1' if b2.cget('text') == 'x' else '2'} wins !!"
        messagebox.showinfo('result', result)
        window.destroy()
    elif (b3.cget('text') == b6.cget('text') == b9.cget('text')) and b3.cget('text') != '':
        result = f"player {'1' if b3.cget('text') == 'x' else '2'} wins !!"
        messagebox.showinfo('result', result)
        window.destroy()
    # checking for diagonal combos
    elif (b1.cget('text') == b5.cget('text') == b9.cget('text')) and b1.cget('text') != '':
        result = f"player {'1' if b1.cget('text') == 'x' else '2'} wins !!"
        messagebox.showinfo('result', result)
        window.destroy()
    elif (b3.cget('text') == b5.cget('text') == b7.cget('text')) and b3.cget('text') != '':
        result = f"player {'1' if b3.cget('text') == 'x' else '2'} wins !!"
        messagebox.showinfo('result', result)
        window.destroy()
# button click functions
def b1click():
    global turn
    mytext = b1.cget('text')
    if mytext == '':
        if turn == 1:
            b1.configure(text = "x")
            turn = 2
        else:
            b1.configure(text = "o")
            turn = 1
        lbl.configure(text = "player" + str(turn) + 'turn !!')
        win()
def b2click():
    global turn
    mytext = b2.cget('text')
    if mytext == '':
        if turn == 1:
            b2.configure(text = "x")
            turn = 2
        else:
            b2.configure(text = "o")
            turn = 1
        lbl.configure(text = "player" + str(turn) + 'turn !!')
        win()
def b3click():
    global turn
    mytext = b3.cget('text')
    if mytext == '':
        if turn == 1:
            b3.configure(text = "x")
            turn = 2
        else:
            b3.configure(text = "o")
            turn = 1
        lbl.configure(text = "player" + str(turn) + 'turn !!')
        win()
def b4click():
    global turn
    mytext = b4.cget('text')
    if mytext == '':
        if turn == 1:
            b4.configure(text = "x")
            turn = 2
        else:
            b4.configure(text = "o")
            turn = 1
        lbl.configure(text = "player" + str(turn) + 'turn !!')
        win()
def b5click():
    global turn
    mytext = b5.cget('text')
    if mytext == '':
        if turn == 1:
            b5.configure(text = "x")
            turn = 2
        else:
            b5.configure(text = "o")
            turn = 1
        lbl.configure(text = "player" + str(turn) + 'turn !!')
        win()
def b6click():
    global turn
    mytext = b6.cget('text')
    if mytext == '':
        if turn == 1:
            b6.configure(text = "x")
            turn = 2
        else:
            b6.configure(text = "o")
            turn = 1
        lbl.configure(text = "player" + str(turn) + 'turn !!')
        win()
def b7click():
    global turn
    mytext = b7.cget('text')
    if mytext == '':
        if turn == 1:
            b7.configure(text = "x")
            turn = 2
        else:
            b7.configure(text = "o")
            turn = 1
        lbl.configure(text = "player" + str(turn) + 'turn !!')
        win()
def b8click():
    global turn
    mytext = b8.cget('text')
    if mytext == '':
        if turn == 1:
            b8.configure(text = "x")
            turn = 2
        else:
            b8.configure(text = "o")
            turn = 1
        lbl.configure(text = "player" + str(turn) + 'turn !!')
        win()
def b9click():
    global turn
    mytext = b9.cget('text')
    if mytext == '':
        if turn == 1:
            b9.configure(text = "x")
            turn = 2
        else:
            b9.configure(text = "o")
            turn = 1
        lbl.configure(text = "player" + str(turn) + 'turn !!')
        win()

# gui layout
b1 = Button(window, text = '', width = 5, command = b1click)
b1.grid(column = 0, row = 0, padx = 5, pady = 5) # each button will be in a square shape
b2 = Button(window, text = '', width = 5, command = b2click)
b2.grid(column = 1, row = 0, padx = 5, pady = 5)
b3 = Button(window, text = '', width = 5, command = b3click)
b3.grid(column = 2, row = 0, padx = 5, pady = 5)
b4 = Button(window, text = '', width = 5, command = b4click)
b4.grid(column = 0, row = 1, padx = 5, pady = 5)
b5 = Button(window, text = '', width = 5, command = b5click)
b5.grid(column = 1, row = 1, padx = 5, pady = 5)
b6 = Button(window, text = '', width = 5, command = b6click)
b6.grid(column = 2, row = 1, padx = 5, pady = 5)
b7 = Button(window, text = '', width = 5, command = b7click)
b7.grid(column = 0, row = 2, padx = 5, pady = 5)
b8 = Button(window, text = '', width = 5, command = b8click)
b8.grid(column = 1, row = 2, padx = 5, pady = 5)
b9 = Button(window, text = '', width = 5, command = b9click)
b9.grid(column = 2, row = 2, padx = 5, pady = 5)

lbl = Label(window, text = "player 1 turn")
lbl.grid(row = 3, column = 1, padx = 10, pady = 10)

window.mainloop()
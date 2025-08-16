from tkinter import *

# create gui window
window = Tk()

# functin to convert weight
# given in kg to grams , pounds
# and ounces

def from_kg():
    # convert kg to gram
    gram = float(e2_value.get()) * 1000
    # convert kg to pound
    pound = float(e2_value.get()) * 2.20462
    # convert kg to ounce
    ounce = float(e2_value.get()) * 35.274

    # enters the converted weight
    # the text widget
    t1.delete("1.0", END)
    t1.insert(END, gram)

    t2.delete("1.0", END)
    t2.insert(END, pound)

    t3.delete("1.0", END)
    t3.insert(END, ounce)

# create the label widgets
e1 = Label(window, text = "enter the weight in kg")
e2_value = StringVar()
e2 = Entry(window, textvariable = e2_value)
e3 = Label(window, text = "gram")
e4 = Label(window, text = "pounds")
e5 = Label(window, text = "ounce")

# create the text widgets
t1 = Text(window, height = 1, width = 20)
t2 = Text(window, height = 1, width = 20)
t3 = Text(window, height = 1, width = 20)

# create the button widget
b1 = Button(window, text = "convert", command = from_kg)

# grid method is used for placing
# the widgets at respective positions
# in grid like structure
e1.grid(row = 0, column = 0)
e2.grid(row = 0, column = 1)
e3.grid(row = 1, column = 0)
e4.grid(row = 1, column = 1)
e5.grid(row = 1, column = 2)

t1.grid(row = 2, column = 0)
t2.grid(row = 2, column = 1)
t3.grid(row = 2, column = 2)
b1.grid(row = 0, column = 2)

window.mainloop()
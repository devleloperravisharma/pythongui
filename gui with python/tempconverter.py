from tkinter import *

# create gui window
window = Tk()



def from_cel():
    # convert cel to f
    far = (float(e2_value.get()) * 1.8)+32
   

    # enters the converted weight
    # the text widget
    t1.delete("1.0", END)
    t1.insert(END, far)

# create the label widgets
e1 = Label(window, text = "enter the temp in celcius")
e2_value = StringVar()
e2 = Entry(window, textvariable = e2_value)
e3 = Label(window, text = "farenheit")

# create the text widgets
t1 = Text(window, height = 1, width = 20)


# create the button widget
b1 = Button(window, text = "convert", command = from_cel)


e1.grid(row = 0, column = 0)
e2.grid(row = 0, column = 1)
e3.grid(row = 1, column = 0)


t1.grid(row = 2, column = 0)
b1.grid(row = 0, column = 2)

window.mainloop()
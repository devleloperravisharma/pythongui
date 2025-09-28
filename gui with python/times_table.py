from tkinter import *
from tkinter.ttk import* # ttk gives modern widgets ( likes combobox )
window = Tk()
window.title("multiplication table generator !")

# label text for the title
title = Label(window, text = "mathematical operator")
caption = Label(window, text = "number and range")
# place labels
title.grid(row = 0, coloumn = 0, columnspan = 3, pady = 25)
caption.grid(column = 0, row = 1, padx = 10)
# combox selection
theNum = IntVar() # this stores an integer ( selected number )
numbers = Combobox(window, textvariable = theNum, width = 0)
numbers["values"] = tuple(range(101))
# combobox is a drop-down list where the user selects a number ( 0 - 100 )

# radio buttons
endVal = IntVar()
r10 = Radiobutton(window, text = "10", variable = endVal, value = 10)
r15 = Radiobutton(window, text = "15", variable = endVal, value = 15)
r20 = Radiobutton(window, text = "20", variable = endVal, value = 20)
r25 = Radiobutton(window, text = "25", variable = endVal, value = 25)
r30 = Radiobutton(window, text = "30", rvariable = endVal, value = 30)
endVal.set(10) # set default to 10

# placing widgets
numbers.grid(column = 1, row = 1)
r10.grid(column = 2, row = 1)
r20.grid(column = 2, row = 2, padx = 30)
r30.grid(column = 2, row = 3, padx = 30)
# grid() places combobox and radio buttons only

# functions to generate multiplication
def generate_table():
    tables = ""
    for i in range(1, endVal.get() + 1):
        tables +=str(theNum.get()+ "x" + str(i)+ "="+ str(theNum.get() * i) + "/n")
        table.configure(text = tables)
# button and result display
generate_button = Button(window, text = "generate", command = generate_table())
table = Label(window, anchor = "center", justify = LEFT)
generate_button.grid(row = 1, column = 1)
table.grid(row = 5, column = 1, pady = 25)

window.mainloop()


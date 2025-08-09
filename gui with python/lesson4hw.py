import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = tk.Tk()
window.geometry("500x500")
window.title("recap")
#make scrollbar
scrollbar = Scrollbar(window)
scrollbar.pack(side = RIGHT, fill=Y)
#button
making_button = tk.Button(window, text = "button", bd = '5', background = "sky blue").place(x = 50, y = 30)
#label
making_label = tk.Label(window, text = "entry box below").place(x = 50, y = 70)
#entry box
making_entrybox = tk.Entry(window, width = 20).place(x = 50, y = 100)
#spinbox
making_spinbox = tk.Spinbox(window, from_ = 0, to = 10).place(x = 50, y = 130)
#listbox
listbox = Listbox(window, yscrollcommand=scrollbar.set, width = 10, height = 5)
listbox.pack(side = RIGHT, fill = BOTH)
#scrollbar
scrollbar.config(command = listbox.yview)
#items
listbox.insert(1, "cupcake")
listbox.insert(2, "cake")
listbox.insert(3, "chocolate")
listbox.insert(4, "brownie")
#message box
messagebox.showinfo("showinfo", "this is me using every widget that i've learned !")

window.mainloop()
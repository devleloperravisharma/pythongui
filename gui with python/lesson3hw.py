import tkinter as tk
import tkinter as tk
window = tk.Tk()
window.geometry("500x500")
window.title("drinks")

# creating the listbox
listbox = tk.Listbox(height = 30, width = 45, bg = "sky blue", fg = "white", activestyle = "dotbox")
# define the label for the list
label = tk.Label(window, text = "drinks")
# putting the drinks
listbox.insert(1, "chocolate milkshake")
listbox.insert(2, "coca cola")
listbox.insert(3, "strawberry milkshake")
listbox.insert(4, "sprite")
listbox.insert(5, "limca")
listbox.insert(6, "fanta")
listbox.insert(7, "lemonade")
listbox.insert(8, "pink lemonade")
listbox.insert(9, "orange juice")
listbox.insert(10, "apple juice")
listbox.insert(11, "apple cider")
listbox.insert(12, "vanilla milkshake")


label.pack
listbox.pack()

window.mainloop()
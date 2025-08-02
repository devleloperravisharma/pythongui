import tkinter as tk
window = tk.Tk()
window.geometry("300x150")
window.title("my favorite dish")
"-"
# create the listbox
listbox = tk.Listbox(height = 10, width = 25, bg = "sky blue", fg = "white", activestyle = "dotbox")
# define the label for the list
label = tk.Label(window, text = "food items")
# insert
listbox.insert(1, "chicken sandwich")
listbox.insert(2, "naan")

label.pack
listbox.pack()

window.mainloop()
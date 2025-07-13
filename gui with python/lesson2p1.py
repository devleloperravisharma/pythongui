import tkinter as tk
#creating the window
window = tk.Tk()
window.title("menu demo")
#making the widgets
menubar = tk.Menu(window)
#adding menu items
#adding file menu and command
file = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label = "file", menu = file)
file.add_command(label = "new file", command = None)
file.add_command(label = "open", command = None)
file.add_command(label = "save", command = None)
file.add_separator()
file.add_command(label = "exit", command = window.destroy)
#attaching the menu bar to the window to be able to display the items
window.config(menu = menubar)

window.mainloop()


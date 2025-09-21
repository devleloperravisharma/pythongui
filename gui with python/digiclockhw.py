import tkinter as tk
from time import strftime
import random

# creating window

window = tk.Tk()
window.title("digiclock (hw)!")

# random color ( using hex codes !! )
def random_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

# heading
title_label = tk.Label(window, text="my digital clock", font=("calibre", 24, "bold"),fg="sky blue", bg="white", pady=10)
title_label.pack(fill="x")

# time
lbl = tk.Label(window,
               font=("calibre", 50, "bold"),
               fg="sky blue",
               bg="white",
               padx=20, pady=20)
lbl.pack(anchor="center", expand=True)

# change colors
def time():
    # update time
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)

    # 50 50 chance for changing fg or bg ( i did use a lil bit of chatgpt ,, but i do understand it ! )
    if random.random() < 0.5:    # random.random() gives a float 0.0–1.0
        lbl.config(fg=random_color())
    else:
        lbl.config(bg=random_color())

    lbl.after(1000, time)  # call again after 1 sec

# end
time()

window.mainloop()
window.mainloop()
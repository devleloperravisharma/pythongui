from tkinter import *
import tkinter.font as font

# functions
def calculate_distance():
    """Calculate distance = speed * time and show result."""
    t = float(time_entry.get())
    s = float(speed_entry.get())
    d = s * t
    result_label.config(text=f"Distance Covered: {d} units")

def clear_inputs():
    """Clear all fields."""
    time_entry.delete(0, END)
    speed_entry.delete(0, END)
    result_label.config(text="")

# gui
window = Tk()
window.title("Distance Calculator")

# font settings
app_font = font.Font(family="Roboto", size=12)

# title
title_label = Label(window, text="Distance Calculator", font=font.Font(size=20), fg="grey")
title_label.pack(pady=10)

# input stuff
input_frame = Frame(window)
input_frame.pack(pady=10)

# more input but time
time_label = Label(input_frame, text="Time (hours):", font=app_font)
time_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
time_entry = Entry(input_frame, font=app_font)
time_entry.grid(row=0, column=1, padx=5, pady=5)

# more input but speed
speed_label = Label(input_frame, text="Speed (units/hour):", font=app_font)
speed_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
speed_entry = Entry(input_frame, font=app_font)
speed_entry.grid(row=1, column=1, padx=5, pady=5)

# buttons !!!
button_frame = Frame(window)
button_frame.pack(pady=10)

calc_button = Button(button_frame, text="Calculate Distance", font=app_font, command=calculate_distance)
calc_button.grid(row=0, column=0, padx=5)

clear_button = Button(button_frame, text="Clear", font=app_font, command=clear_inputs)
clear_button.grid(row=0, column=1, padx=5)

# result
result_label = Label(window, text="", font=app_font, fg="blue")
result_label.pack(pady=20)

window.mainloop()
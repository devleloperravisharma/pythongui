import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("student report log")
root.geometry("750x500")

# main screen
screen = tk.Frame(root, bg="lightblue", bd=2, relief="solid")
screen.pack(fill="both", expand=True, padx=15, pady=15)

# title label
title = tk.Label(screen, text="STUDENT REPORT LOG", font=("Arial", 14, "bold"), bg="white")
title.place(x=15, y=10)

# ------- labels + entries ( left ) -------
# name
lbl_name = tk.Label(screen, text="name :", font=("Arial", 12), bg="lightblue")
lbl_name.place(x=15, y=60)

ent_name = tk.Entry(screen, width=25)
ent_name.place(x=120, y=62)

# roll number
lbl_roll = tk.Label(screen, text="roll number :", font=("Arial", 12), bg="lightblue")
lbl_roll.place(x=15, y=100)

ent_roll = tk.Entry(screen, width=25)
ent_roll.place(x=120, y=102)

# ------- labels + entries ( right ) -------
# science grade
lbl_science = tk.Label(screen, text="science grade :", font=("Arial", 12), bg="lightblue")
lbl_science.place(x=430, y=60)

ent_science = tk.Entry(screen, width=15)
ent_science.place(x=570, y=62)

# math grade
lbl_math = tk.Label(screen, text="math grade :", font=("Arial", 12), bg="lightblue")
lbl_math.place(x=430, y=100)

ent_math = tk.Entry(screen, width=15)
ent_math.place(x=570, y=102)

# percentage
lbl_percentage = tk.Label(screen, text="percentage :", font=("Arial", 12), bg="lightblue")
lbl_percentage.place(x=430, y=140)

ent_percentage = tk.Entry(screen, width=15)
ent_percentage.place(x=570, y=142)

# listbox
listbox = tk.Listbox(screen, height=8, bg="white", font=("Arial", 11))
listbox.place(x=3, y=190, width=710, height=160)

# bottom buttons
button_frame = tk.Frame(screen, bg="white")
button_frame.place(x=15, y=370, width=710, height=80)

# make buttons
btn_edit = ttk.Button(button_frame, text="Edit")
btn_delete = ttk.Button(button_frame, text="Delete")
btn_open = ttk.Button(button_frame, text="Open")
btn_update = ttk.Button(button_frame, text="Update/Add")
btn_save = ttk.Button(button_frame, text="Save")
# spacing
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.columnconfigure(3, weight=1)
button_frame.columnconfigure(4, weight=1)

btn_edit.grid(row=0, column=0, padx=10, pady=20)
btn_delete.grid(row=0, column=1, padx=10)
btn_open.grid(row=0, column=2, padx=10)
btn_update.grid(row=0, column=3, padx=10)
btn_save.grid(row=0, column=4, padx=10)

root.mainloop()

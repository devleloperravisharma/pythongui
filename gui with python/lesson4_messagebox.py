from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("300x200")
w = Label(window, text = "hii !! i'm messagebox", font = "50")
w.pack()

# finding the different functions possible with message box

messagebox.showinfo("showinfo", "information")
messagebox.showwarning("show warning", "WARNING")
messagebox.showerror("show error", "there's an error, please try again")
messagebox.askquestion("show questions", "pretend like i'm asking you a question")
messagebox.askokcancel("askokcancel", "are you sure you want to cancel ?")
messagebox.askyesno("ask no", "find the value")
messagebox.askretrycancel("askretrycancel", "try again !!")

# loop

window.mainloop()
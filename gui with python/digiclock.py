import tkinter as tk

from time import strftime

# create window

window = tk.Tk()

window.title("digiclock !")

# funcs to update time

def time():

    string = strftime('%H:%M:%S:%p') # 12 hour format w am and pm

    lbl.config(text = string) # update label text

    lbl.after(1000, time) # call the func again after 1 second !!

# create label

lbl = tk.Label(window, font = ("calibre", 40, "bold"), fg = "sky blue", bg = "white")

lbl.pack(anchor = "center") # anchor helps center "lbl" at the center of the section

#done !!

time()

window.mainloop()
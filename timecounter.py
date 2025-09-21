from tkinter import *
import time
from tkinter import messagebox

# making the window
window = Tk()
window.geometry("300x250")
window.title("time counter")
# creating the variables
hour = StringVar()
minute = StringVar()
second = StringVar()
# default values !
hour.set("00")
minute.set("00")
second.set("00")
# entries !!
hour_entry = Entry(window, width = 3, font = ("arial", 18, ""), textvariable = hour)
hour_entry.place(x = 80, y = 20)
# input minutes
minute_entry = Entry(window, width = 3, font = ("arial", 18, ""), textvariable = minute)
minute_entry.place(x = 130, y = 20)
# input seconds
second_entry = Entry(window, width = 3, font = ("arial", 18, ""), textvariable = second)
second_entry.place(x = 180, y = 20)

# function for counting logic !
def submit():
    try:
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("that doesn't work, please enter the right values.")
    while temp > -1:
        mins,secs = divmod(temp, 60) # splitting in mins and secs
        hours = 0
        if mins > 60:
            hours,mins = divmod(mins, 60)
        # set the time
        hour.set("{0:02d}".format(hours))
        minute.set("{}".format(mins))
        second.set("{0:02d}".format(secs))
        # gui update !!
        window.update() # refreshes gui after every second
        time.sleep(1)
        # time's up !!
        if temp == 0:
            messagebox.showinfo("message from time counter", " time's up !")
            # if the countdown reaches zero -- then the pop up appears !!
        temp = temp - 1 # reduces time until temp is less than or equal to zero !
# button !
start_button = Button(window, text = "set time countdown", bd = "5", command = submit)
start_button.place(x = 70, y = 120)

# main loop
window.mainloop()
# importing needed methods and classes from tkinter
from tkinter import *
# import calendar module
import calendar
def show_cal():
    window = Tk()
    window.configure(background = "white")
    # title of the screen
    window.title("calendar")
    # screen size
    window.geometry("500x600")
    # getting the methods to fetch the current year
    fetch_year = int(year_field.get())
    # calendar method to get the calendar in return
    cal_content = calendar.calendar(fetch_year)
    # label for showing the content of the year
    cal_year = Label(window, text = cal_content, font = ("courier new", 10))
    # grid to show
    cal_year.grid(rows = 5, column = 1, padx = 20)

# driver code
if __name__ == '__main__':
    new_window= Tk()

    # set background color
    new_window.config(background = "white")
    new_window.title("calendar")
    new_window.geometry('250x140')
    cal = Label(new_window, text = "calendar", bg = "sky blue", font=("roboto" ,28, "bold"))

    # create a label
    year = Label(new_window, text = "enter year", bg = "light green")

    # enter a text entry box
    year_field = Entry(new_window)

    # create a show calendar button and the call the function 'showCal()'
    show = Button(new_window, text = "show calendar", fg = "white", bg = "sky blue", command = show_cal)
    Exit = Button(new_window, text = "exit", fg = "white", bg = "pink", command = new_window.destroy)

    # arranging the widgets
    cal.grid(row = 1, column = 1)
    year.grid(row = 2, column = 1)
    year_field.grid(row = 3, column = 1)
    show.grid(row = 4, column = 1)
    Exit.grid(row = 6, column = 1)

    # keep the window open
    new_window.mainloop()

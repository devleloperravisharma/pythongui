import tkinter as tk
window = tk.Tk()
window.title("login")
window.geometry('500x500')
window.config(background='sky blue')

#creating a label
username = tk.Label(window, text = "username").place(x = 50, y = 70)
#making a password
password = tk.Label(window, text = "password").place(x = 50, y = 100)
#making the submit button
submit_button = tk.Button(window, text = "submit", bd = 7, background = "pink").place(x = 50, y = 130)
#enter name
name_input_area = tk.Entry(window, width = 30).place(x = 110, y = 70)
#enter password
password_input_area = tk.Entry(window, show = "*", width = 30).place(x = 110, y = 100)
#try again button
try_again = tk.Button(window, text = "try again", bd = 7, background = "pink").place(x = 130, y = 130)

window.mainloop()
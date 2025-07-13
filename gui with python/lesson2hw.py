import tkinter as tk
#quantity_spinbox = tk.Spinbox(window, from_ = 0, to = 10).place(x = xx, y=xx)
window = tk.Tk()
window.geometry("500x400")
window.title("your-door up!")
window.config(background = "sky blue")
#creating email and password label
email = tk.Label(window, text = "email").place(x = 30, y = 15)
password = tk.Label(window, text = "password").place(x = 30, y = 40)
#creating the text input as per the email and password
email_input = tk.Entry(window, width = 30).place(x = 100, y = 16)
password_input = tk.Entry(window, show = "●", width = 30).place(x = 100, y = 41)
#note - you must type your choice as seen in the options
tk.Label(window, text = "**please note that you must type your choice as seen in the options, thank you !**").place(x = 30, y = 70)
#text number one - what food would you like ?
txt1 = tk.Label(window, text = "which food option would you like ? a chicken sandwich, b.l.t, a veg sandwich, or none ?").place(x = 15, y = 100)
#text number two - which drink would you like ?
txt2 = tk.Label(window, text = "which drink would you like ? a cola, fanta, orange juice, water, or none ?").place(x = 50, y = 160)
#text number three - which dessert  would you like ?
txt3 = tk.Label(window, text = "which dessert would you like ? an ice cream, a donut, a chocolate cake, or none ?").place(x = 20, y = 220)
#text entry -- text one
txt1entry = tk.Entry(window, width = 25).place(x = 80, y = 130)
#dropdown 1
quantity_spinbox1 = tk.Spinbox(window, from_ = 0, to = 10).place(x = 260, y = 130)
#text entry -- text two
txtentry2 = tk.Entry(window, width = 25).place(x = 80, y = 190)
#dropdown 2
quantity_spinbox2 = tk.Spinbox(window, from_ = 0, to = 10).place(x = 260, y = 190)
#text entry -- text three
txtentry3 = tk.Entry(window, width = 25).place(x = 80, y = 250)
#dropdown 3
quantity_spinbox3 = tk.Spinbox(window, from_ = 0, to = 10).place(x = 260, y = 250)
#"thank you for ordering from 'your-door up !'"
thanks = tk.Label(window, text = "thank you for ordering from 'your-door up !', enjoy your food :)").place(x = 65, y = 290)
#submit your order
submit = tk.Button(window, text = "submit your order !", bd = 5, command = window.destroy).place(x = 180, y = 330)
window.mainloop()
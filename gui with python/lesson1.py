#this lesson shows the tkinter library that helps the desktop application
import tkinter as tk
#refer to tkinter elements such as this
#creating the window
root = tk.Tk()
#opening the window having dimenstions (200x200)
root.geometry('200x200')
#making a button
button = tk.Button(root, text = "click me !", bd = '5', background = "sky blue", command = root.destroy)
#set the button position at the top of the window
button.pack(side = 'top')
#creating another button
button2 = tk.Button(root, text = "say hi !", bd = '5', background = "pink", command = root.destroy)
#placement
button.pack(side = 'top')
#to run
root.mainloop()
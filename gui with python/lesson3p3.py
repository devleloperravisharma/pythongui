from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("lesson 3 -- listbox with scrollbar")
# creating the scrollbar
scrollbar = Scrollbar(window)
scrollbar.pack(side = RIGHT, fill=Y)
# create a listbox and connect to the scrollbar
listbox = Listbox(window, yscrollcommand=scrollbar.set, width = 25, height = 10, font = "Roboto")
listbox.pack(side = LEFT, fill = BOTH)
# configure scroll with the listbox
scrollbar.config(command = listbox.yview)
for i in range(1,20):
    listbox.insert(END, f"list item{i}")
# run the mainloop
window.mainloop()
# notes for wanting to use your own items vv
'''
#add custom items
foods = [ "pizza", "burger" (KEEP GOING WITH ITEMS)]
#insert items in the listbox
for item in foods:
    listbox.insert(END, item)
'''
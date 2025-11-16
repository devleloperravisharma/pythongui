from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
# basics
window = Tk()
window.title('address book')
# -------------------------- CODE !!! --------------------------
myaddressbook = {}
# clear all the text boxes on the main screen
def clear_all():
    name.delete(0, END)
    address.delete(0, END)
    number.delete(0, END)
    email.delete(0, END)
    birthday(0, END)
# update listbox
def update():
    key = name.get()
    if key == "":
        messagebox.showinfo("error", "name cannot be empty")
    else:
        # add entry in the box only if it is a new entry
        if key not in myaddressbook.keys():
            book_list.insert(END, key)
        # update the dictionary
        myaddressbook[key] = (address.get(), number.get(), birthday.get(), email.get())
        # clear the textboxes
        clear_all()
# edit the data
def edit():
    clear_all()
    index = book = book_list.curselection()
    if index:
        # add name to the text
        name.insert(0, book_list.get(index))
        details = myaddressbook[name.get()]
        # add details to the boxes
        address.insert(0, details[0])
        number.insert(0, details[1])
        email.insert(0, details[2])
        birthday.insert(0, details[3])
    else:
        messagebox.showinfo("error ", "select a name !!")
# delete selected item
def delete():
    # get select line index
    index = book_list.curselection()
    if index:
        # delete from dictionary
        del myaddressbook[book_list.get()]

        # delete from listbox
        book_list.delete(index)

        # clear the text boxes
        clear_all()

    else:
        messagebox.showerror("error", "select a name")
# display function
def display(event):
    new_window = Toplevel(window)
    index = book_list.curselection()
    contact = ""

    if index:
        key = book_list.get(index)
        details = myaddressbook[key]
        contact = (
            f"name : {key}\n\n"
            f"address : {details[0]}\n\n"
            f"number : {details[1]}\n"
            f"email : {details[2]}\n"
            f"birthday : {details[3]}\n"
        )
    lbl = Label(new_window)
    lbl.grid(row = 0, column = 0)
    lbl.configure(text = contact)

def reset():
    clear_all()
    book_list.delete(0, END)
    myaddressbook.clear()
    book_list.configure(text = "my address book") # last left off HERE
             # ------------- gui !! -------------
book_name = Label(window, text = "address book", width = 35)
book_name.grid(row = 0, column = 1, pady = 10, columnspan = 3)
# open address book
open_button = Button(window, text = "open")
open_button.grid(row = 0, column = 3, pady = 10)
# contact list
book_list = Listbox(window, height = 15, width = 30)
book_list.grid(row = 2, column = 0, columnspan = 3, rowspan = 5)
# name
name_lbl = Label(window, text = "name :")
name_lbl.grid(row = 2, column = 3)
name = Entry(window)
name.grid(row = 2, column = 4, padx = 5)
# address
address_lbl = Label(window, text = "address :")
address_lbl.grid(row = 3, column = 3)
address = Entry(window)
address.grid(row = 3, column = 4, padx = 5)
# number
number_lbl = Label(window, text = "number:")
number_lbl.grid(row = 4, column = 3)
number = Entry(window)
number.grid(row = 4, column = 4, padx = 5)
# email
email_lbl = Label(window, text = "email")
email_lbl.grid(row = 5, column = 3)
email = Entry(window)
email.grid(row = 5, column = 4, padx = 5)
# birthday
birthday_lbl = Label(window, text = "birthday:")
birthday_lbl.grid(row = 6, column = 3)
birthday = Entry(window)
birthday.grid(row = 6, column = 4, padx = 5)
# ---- buttons ! ----
# update //  add button
add_button = Button(window, text = "update/add", width = 10, command = update)
add_button.grid(row = 7, column = 4, padx = 12, pady = 12)
# edit button
edit_button = Button(window, text = "edit", width = 10, command = edit)
edit_button.grid(row = 7, column = 0, padx = 12, pady = 12)
# delete button
delete_button = Button(window, text = "delete", width = 10, command = delete)
delete_button.grid(row = 7, column = 1, padx = 12, pady = 12)
# save button
save_button = Button(window, text = "save", width = 10)
save_button.grid(row = 8, column = 1, pady = 10, columnspan = 3)


window.mainloop()

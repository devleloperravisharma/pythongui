import tkinter as tk
window = tk.Tk()
window.geometry("300x150")
window_label = tk.Label(window, text = "choose choco and ice cream", font = "50")
window_label.pack
frame = tk.Frame(window)
frame.pack()
# bottom frame
bottom_frame = tk.Frame(window)
bottom_frame.pack(side = tk.BOTTOM)
# make the buttons !!
# button one
b1_button = tk.Button(frame, text = "dark chocolate", fg = "white", bg = "pink")
b1_button.pack(side = "left")
# button two
b2_button = tk.Button(frame, text = "milk chocolate", fg = "white", bg = "pink")
b2_button.pack(side = "left")
# button three
b3_button = tk.Button(frame, text = "white chocolate", fg = "white", bg = "pink")
b3_button.pack(side = "left")
# more buttons for the second frame
# button four
b4_button = tk.Button(bottom_frame, text = "pastry", fg = "white", bg = "sky blue")
b4_button.pack(side = tk.BOTTOM)
# button five
b5_button = tk.Button(bottom_frame, text = "tirmasu", fg = "white", bg = "sky blue")
b5_button.pack(side = tk.BOTTOM)
# button six
b6_button = tk.Button(bottom_frame, text = "cake", fg = "white", bg = "sky blue")
b6_button.pack(side = tk.BOTTOM)


window.mainloop()
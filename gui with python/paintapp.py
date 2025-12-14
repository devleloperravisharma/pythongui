from tkinter import *
from tkinter.colorchooser import askcolor

class Paint(object):
    default_pen_size = 5.0
    default_color = "black"

    def __init__(self):
        self.root = Tk()
        self.pen_button = Button(self.root, text = "pen", command = self.use_pen)
        self.pen_button.grid(row =0, column = 0)
        self.brush_button = Button(self.root, text = "brush", command = self.use_brush)
        self.brush_button.grid(row = 0, column = 1)
        self.color_button = Button(self.root, text = "color", command = self.choose_color)
        self.color_button.grid(row = 0, column = 2)
        self.eraser_button = Button(self.root, text = "eraser", command = self.use_brush)
        self.eraser_button.grid(row = 0, column = 3)
        self.choose_pen_size = Scale(self.root, from_= 1, to = 10, orient = HORIZONTAL)
        self.choose_pen_size.grid(row = 0, column = 4)
        self.c = Canvas(self.root, bg = "white", width = 600, height = 600)
        self.c.grid(row = 1, columnspan = 5)
        self.setup()
        self.root.mainloop()
    def setup(self):
        self.old_x = None # stores the previous position of the mouse
        self.old_y = None
        self.line_width = self.choose_pen_size.get()
        self.color = self.default_color
        self.eraser_on = False
        self.active_button = self.pen_button # pen button is active
        # mouse events
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
    # pen and brush methods
    def use_pen(self):
        self.activate_button(self.pen_button)
    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color = self.color)[1]
    # eraser mode
    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode = True)
    # button activation
    def activate_button(self, some_button, eraser_mode = False):
        self.active_button.config(relief = RAISED) # makes the old button look raised
        some_button.config(relief = SUNKEN) # makes the new button look pressed
        self.active_button = some_button
        self.eraser_on = eraser_mode
    def paint(self, event):
        # update the brush size
        self.line_width = self.choose_pen_size.get()
        # choose color or erase
        paint_color = 'white' if self.eraser_on else self.color
        # draw line
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y, 
                               width = self.line_width, 
                               fill = paint_color, 
                               splinesteps = 36, 
                               capstyle = ROUND, 
                               smooth = TRUE)
        self.old_x = event.x
        self.old_y = event.y
    def reset(self, event):
        self.old_x, self.old_y = None, None
# program Entry point
if __name__ == "__main__":
    Paint()




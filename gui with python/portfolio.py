import tkinter as tk
import random
import math

WIDTH = 500
HEIGHT = 520
CENTER_X = WIDTH // 2
CENTER_Y = 260
RADIUS = 200
SNOW_COUNT = 130

FESTIVE_COLORS = [
    "red", "green", "gold", "blue",
    "purple", "pink", "cyan", "orange",
    "saddlebrown", "darkgreen", "peru",
    "azure", "lightcyan", "powderblue",
    "lightblue", "sienna", "indianred",
    "lavenderblush", "cadetblue"
    ]
# -----
class SnowGlobe:
    def __init__(self, root):
        self.root = root
        self.root.title("Snow Globe ❄️")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#0b1d3a")
        self.canvas.pack()

        self.snowflakes = []
        self.snow_speed = 2
        self.snowing = True

        self.draw_globe()
        self.draw_scene()
        self.create_snow()
        self.create_controls()
        self.animate_snow()

    # fat ahh circle
    def draw_globe(self):
        self.canvas.create_oval(
            CENTER_X - RADIUS, CENTER_Y - RADIUS,
            CENTER_X + RADIUS, CENTER_Y + RADIUS,
            outline="white", width=4
        )

    # look at the scenery !
    def draw_scene(self):
        globe_bottom_y = CENTER_Y + RADIUS

        self.canvas.create_oval(
            CENTER_X - 130,
            globe_bottom_y - 100,
            CENTER_X + 130,
            457.7,
            fill="white",
            outline=""
        )

        # i am TREE !!!
        self.tree_leaves = self.canvas.create_polygon(
            CENTER_X, CENTER_Y + 10,
            CENTER_X - 50, CENTER_Y + 100,
            CENTER_X + 50, CENTER_Y + 100,
            fill="darkgreen", tags="leaves"
        )

        self.tree_trunk = self.canvas.create_rectangle(
            CENTER_X - 12, CENTER_Y + 100,
            CENTER_X + 12, CENTER_Y + 145,
            fill="saddlebrown", outline="", tags="trunk"
        )

        # sweet HOME alabamaaaa
        self.house_walls = self.canvas.create_rectangle(
            CENTER_X + 70, CENTER_Y + 80,
            CENTER_X + 140, CENTER_Y + 150,
            fill="#c97c5d", tags="walls"
        )

        self.house_roof = self.canvas.create_polygon(
            CENTER_X + 60, CENTER_Y + 80,
            CENTER_X + 105, CENTER_Y + 40,
            CENTER_X + 150, CENTER_Y + 80,
            fill="#8b0000", tags="roof"
        )

        # clicking !
        for tag in ("leaves", "trunk", "walls", "roof"):
            self.canvas.tag_bind(tag, "<Button-1>", self.change_color)

    # snow + animation of the snow
    def create_snow(self):
        for _ in range(SNOW_COUNT):
            x, y = self.random_point_in_circle()
            flake = self.canvas.create_oval(
                x, y, x + 3, y + 3,
                fill="white", outline=""
            )
            self.snowflakes.append(flake)

    def random_point_in_circle(self):
        while True:
            x = random.randint(CENTER_X - RADIUS, CENTER_X + RADIUS)
            y = random.randint(CENTER_Y - RADIUS, CENTER_Y + RADIUS)
            if math.dist((x, y), (CENTER_X, CENTER_Y)) < RADIUS - 6:
                return x, y

    def animate_snow(self):
        if self.snowing:
            for flake in self.snowflakes:
                self.canvas.move(flake, 0, self.snow_speed)
                x1, y1, _, _ = self.canvas.coords(flake)

                if math.dist((x1, y1), (CENTER_X, CENTER_Y)) > RADIUS - 8:
                    x, y = self.random_point_in_circle()
                    self.canvas.coords(flake, x, y, x + 3, y + 3)

        self.root.after(35, self.animate_snow)

    # change the color ? YAYAYA
    def change_color(self, event):
        item = self.canvas.find_withtag("current")
        new_color = random.choice(FESTIVE_COLORS)
        self.canvas.itemconfig(item, fill=new_color)

    # controls !
    def create_controls(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=8)

        tk.Button(
            frame, text="Toggle Snow ❄️",
            command=self.toggle_snow
        ).grid(row=0, column=0, padx=5)

        tk.Label(frame, text="Snow Speed").grid(row=0, column=1)

        slider = tk.Scale(
            frame, from_=1, to=8,
            orient=tk.HORIZONTAL,
            command=self.set_speed
        )
        slider.set(self.snow_speed)
        slider.grid(row=0, column=2, padx=5)

    def toggle_snow(self):
        self.snowing = not self.snowing

    def set_speed(self, value):
        self.snow_speed = int(value)


# FINNA RUN TS
root = tk.Tk()
SnowGlobe(root)
root.mainloop()

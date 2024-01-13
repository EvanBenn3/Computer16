import tkinter as tk

# Screen Class
class Screen:
    # Initiallizes all the variables
    def __init__(self):
        self.pos = 0
        self.color = 0
        self.root = tk.Tk()
        self.pixelSize = 2
        self.canvas = tk.Canvas(self.root, width=256*self.pixelSize, height=256*self.pixelSize, bg="black")
        self.canvas.pack()
        # self.canvas.create_rectangle(0, 0, 8, 8, fill="red")

    # Updates the Screen
    def update(self):
        x = (self.pos & 0xFF)
        y = (self.pos & 0xFF00) >> 8
        color = ((self.color & 0b11111) * 8 - 1, ((self.color & 0b1111100000) >> 5) * 8 - 1, ((self.color & 0b111110000000000) >> 10) * 8 - 1)
        # print(x)
        # print(y)
        # print(color)
        self.canvas.create_rectangle(x, y, (x+1)*self.pixelSize * 2, (y+1)*self.pixelSize * 2, fill="#%02x%02x%02x" % color)

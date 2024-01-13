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

    # Updates the Screen
    def update(self):
        x = (self.pos & 0xFF)
        y = (self.pos & 0xFF00) >> 8
        color = ((self.color & 0b11111) * 8, ((self.color & 0b1111100000) >> 5) * 8, ((self.color & 0b111110000000000) >> 10) * 8)

        self.canvas.create_rectangle(x, y, x+self.pixelSize, y+self.pixelSize, fill="#%02x%02x%02x" % color)

    def display(self):
        self.canvas.mainloop()

    # Control Signals
    def screen_io(self, device):
        if device.io_device_signal_a == True & device.io_device_signal_b == False:
            self.pos = device.reg_output
        if device.io_device_signal_a == False & device.io_device_signal_b == True:
            self.color = device.reg_output
        if device.io_device_signal_a == True & device.io_device_signal_b == True:
            self.update()

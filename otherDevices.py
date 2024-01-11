# Screen Class
class Screen:
    # Initiallizes all the variables
    def __init__(self):
        self.pixels = [0] * (1024 * 512)
        self.pos = 0
        self.color = 0

    # Updates the Screen
    def update(self):
        self.pixels[self.pos] = self.color

    # Displays the Screen
    def display(self):
        d = 0
        #for later, dont mind the variable.

    # Control Signals
    def screen_io(self, device):
        if device.io_device_signal_a == True & device.io_device_signal_b == False:
            self.pos = device.reg_output
        if device.io_device_signal_a == False & device.io_device_signal_b == True:
            self.color = device.reg_output
        if device.io_device_signal_a == True & device.io_device_signal_b == True:
            self.update()
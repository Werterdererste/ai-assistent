
class LED:

    def __init__(self, gpioPin_R, gpioPin_G, gpioPin_B):
        self.gpioPin_R = gpioPin_R
        self.gpioPin_G = gpioPin_G
        self.gpioPin_B = gpioPin_B

    def on(self, r, g, b):
        # Wert den es annehmen soll oder an oder aus ??
        raise NotImplementedError

    def of(self):
        raise NotImplementedError

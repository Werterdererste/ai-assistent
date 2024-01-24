
class Button:

    def __init__(self, gpioPin):
        self.gpioPin = gpioPin

    def isPress(self) -> bool:
        raise NotImplementedError


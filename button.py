import RPi.GPIO as GPIO

class Button:
    """
    Button über gpio
    """
    def __init__(self, gpioPin):
        self.gpioPin = gpioPin

    def isPress(self) -> bool:
        """
        liefert einen wert zurück ob der button gedrückt wird
        :return:
        """
        raise NotImplementedError


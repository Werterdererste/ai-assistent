try:
    import RPi.GPIO as GPIO
except RuntimeError:
    import Mock.GPIO as GPIO
from time import sleep


class Button:
    """
    Button über gpio
    """
    def __init__(self, gpioPin):
        self.gpioPin = gpioPin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.gpioPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def press(self) -> bool:
        """
        liefert true zurück wen der button gedrückt wird
        :return:
        """
        if not GPIO.input(self.gpioPin):
            return True
        return False

    def clean(self):
        """
        gibt alle pins frei.
        ! Beim Schließen ausführen
        :return:
        """
        GPIO.cleanup()
        print("button clean")

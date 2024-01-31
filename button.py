import RPi.GPIO as GPIO

class Button:
    """
    Button über gpio
    """
    def __init__(self, gpioPin):
        self.gpioPin = gpioPin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.gpioPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    def isPress(self) -> bool:
        """
        liefert einen wert zurück ob der button gedrückt wird
        :return:
        """
        if GPIO.input(self.gpioPin) == GPIO.HIGH:
            return True

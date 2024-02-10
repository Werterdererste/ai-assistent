try:
    import RPi.GPIO as GPIO
except RuntimeError:
    import Mock.GPIO as GPIO

class LED:
    """
    Ansteuerungs code für eine LED
    """

    def __init__(self, gpioPin_R: int, gpioPin_G: int, gpioPin_B: int):
        """
        Constructor zum Setzen der Ansteuerung pinns.
        :param gpioPin_R:
        :param gpioPin_G:
        :param gpioPin_B:
        """
        self.gpioPin_R: int = gpioPin_R
        self.gpioPin_G: int = gpioPin_G
        self.gpioPin_B: int = gpioPin_B

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.gpioPin_R, GPIO.OUT)
        GPIO.setup(self.gpioPin_G, GPIO.OUT)
        GPIO.setup(self.gpioPin_B, GPIO.OUT)

    def off(self):
        """
        Schalltet LED aus
        :return:
        """
        GPIO.output(self.gpioPin_R, False)
        GPIO.output(self.gpioPin_G, False)
        GPIO.output(self.gpioPin_B, False)
        print("led off")

    def clean(self):
        """
        gibt alle pins frei.
        ! Beim Schließen ausführen
        :return:
        """
        GPIO.cleanup()
        print("led clean")

    def white(self):
        """
        LED farbe Weiß
        R on
        G on
        B on
        :return:
        """
        GPIO.output(self.gpioPin_R, True)
        GPIO.output(self.gpioPin_G, True)
        GPIO.output(self.gpioPin_B, True)
        print("led white")

    def red(self):
        """
        LED farbe Rot

        R on
        G off
        B off
        :return:
        """
        GPIO.output(self.gpioPin_R, True)
        GPIO.output(self.gpioPin_G, False)
        GPIO.output(self.gpioPin_B, False)
        print("led red")

    def green(self):
        """
        LED farbe Grün

        R off
        G on
        B off
        :return:
        """
        GPIO.output(self.gpioPin_R, False)
        GPIO.output(self.gpioPin_G, True)
        GPIO.output(self.gpioPin_B, False)
        print("led green")

    def blue(self):
        """
        LED farbe Blau

        R off
        G off
        B on
        :return:
        """
        GPIO.output(self.gpioPin_R, False)
        GPIO.output(self.gpioPin_G, False)
        GPIO.output(self.gpioPin_B, True)
        print("led blue")

    def yellow(self):
        """
        LED farbe Gelb

        R on
        G on
        B off
        :return:
        """
        GPIO.output(self.gpioPin_R, True)
        GPIO.output(self.gpioPin_G, True)
        GPIO.output(self.gpioPin_B, False)
        print("led yellow")

    def lightblue(self):
        """
        LED farbe Hellblau

        R off
        G on
        B on
        :return:
        """
        GPIO.output(self.gpioPin_R, False)
        GPIO.output(self.gpioPin_G, True)
        GPIO.output(self.gpioPin_B, True)
        print("led lightblue")

    def magenta(self):
        """
        LED farbe Magenta

        R on
        G off
        B on
        :return:
        """
        GPIO.output(self.gpioPin_R, True)
        GPIO.output(self.gpioPin_G, False)
        GPIO.output(self.gpioPin_B, True)
        print("led magenta")

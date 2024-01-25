
class LED:

    def __init__(self, gpioPin_R: int = 1, gpioPin_G: int = 1, gpioPin_B: int = 1):
        self.gpioPin_R: int = gpioPin_R
        self.gpioPin_G: int = gpioPin_G
        self.gpioPin_B: int = gpioPin_B

    def off(self):
        raise NotImplementedError

    def white(self):
        #r on
        #g on
        #b on
        raise NotImplementedError

    def red(self):
        #r on
        #g off
        #b off
        raise NotImplementedError

    def green(self):
        # r off
        # g on
        # b off
        raise NotImplementedError

    def blue(self):
        # r off
        # g off
        # b on
        raise NotImplementedError

    def yellow(self):
        # r on
        # g on
        # b off
        raise NotImplementedError

    def lightblue(self):
        # r off
        # g on
        # b off
        raise NotImplementedError
    def magenta(self):
        # r on
        # g off
        # b on
        raise NotImplementedError
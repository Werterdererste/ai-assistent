import audio_interface
from status_led import LED
from button import Button
from audio_interface import AudioInterface
from controller_assistent import ControllerAssistent
from models import IModels, TestModel, TinyLlama11b

from time import sleep


class Program:

    def __init__(self):
        self.model: IModels = TinyLlama11b()

        self.status_led: LED = LED(gpioPin_R=22, gpioPin_G=24, gpioPin_B=26)
        self.button: Button = Button(gpioPin=37)
        self.audio: AudioInterface = AudioInterface()
        self.controller = ControllerAssistent(self.status_led, self.button, self.audio, self.model)

    def main(self):
        self.controller.speak_assistent()

    def led_test(self):
        sleep(5)
        self.status_led.red()
        sleep(5)
        self.status_led.blue()
        sleep(5)
        self.status_led.green()
        sleep(5)
        self.status_led.yellow()
        sleep(5)
        self.status_led.magenta()
        sleep(5)
        self.status_led.lightblue()
        sleep(5)
        self.status_led.white()
        sleep(5)
        self.status_led.off()


if __name__ == '__main__':
    program: Program = Program()
    program.main()

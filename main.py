import audio_interface
from model_tinyllama import TinyLlama11b
from status_led import LED
from button import Button
from audio_interface import AudioInterface
from translater import Translater
from modelTest import ModelTest

from time import sleep


class Program:

    def __init__(self):
        #self.tinyllama: TinyLlama11b = TinyLlama11b()
        # TODO: pins
        self.status_led: LED = LED()
        self.button: Button = Button(1)
        self.audio: AudioInterface = AudioInterface()
        self.translater: Translater = Translater()

        self.modelTest: ModelTest = ModelTest()

    def main(self):
        print("test")
        self.audio.speak(self.modelTest.send("You can queue up multiple items."))

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



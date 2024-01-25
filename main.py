import audio_interface
from model_tinyllama import TinyLlama11b
from status_led import LED
from button import Button
from audio_interface import AudioInterface
from translater import Translater

class Program:

    def __init__(self):
        self.tinyllama: TinyLlama11b = TinyLlama11b()
        # TODO: pins
        self.status_led: LED = LED()
        self.button: Button = Button(1)
        self.audio: AudioInterface = AudioInterface()
        self.translater: Translater = Translater()

    def main(self):
        print("test")

        self.audio.speak("audios/warning.mp3")

       # print(self.tinyllama.send("why is the sky blue"))



if __name__ == '__main__':
    program: Program = Program()
    program.main()


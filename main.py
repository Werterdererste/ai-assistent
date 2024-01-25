import audio_interface
from model_tinyllama import TinyLlama11b
from status_led import LED
from button import Button
from audio_interface import AudioInterface
from translater import Translater

class Program:
    def main(self):
        audio_interface: AudioInterface = AudioInterface()
        audio_interface.speak("audios/warning.mp3")

        tinyllam: TinyLlama11b = TinyLlama11b()
        print(tinyllam.send("why is the sky blue"))



if __name__ == '__main__':
    program: Program = Program()
    program.main()


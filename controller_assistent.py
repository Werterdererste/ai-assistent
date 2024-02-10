from status_led import LED
from button import Button
from audio_interface import AudioInterface
from modelTest import ModelTest


class ControllerAssistent:

    def __init__(self, led: LED, button: Button, audio: AudioInterface, model: ModelTest):
        self.led = led
        self.button = button
        self.audio = audio
        self.model = model
        self.active = True

    def speak_assistent(self):
        """
        startet einen einfachen sprach assistenten

        :return:
        """

        try:
            while self.active:

                self.led.green()
                if self.button.press():

                    self.led.blue()
                    query = self.audio.listen()
                    print(query)

                    self.led.yellow()
                    response = self.model.send(query)
                    print(response)

                    self.led.white()
                    self.audio.speak(response)

        except KeyboardInterrupt:
            print("exit")
            self.active = False
        finally:
            self.led.clean()
            self.button.clean()

    def web_assistent(self):
        raise NotImplementedError

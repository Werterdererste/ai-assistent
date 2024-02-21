import time

from status_led import LED
from button import Button
from audio_interface import AudioInterface
from models import IModels
from web_interface import WebInterface


class ControllerAssistent:

    def __init__(self, led: LED, button: Button, audio: AudioInterface, model: IModels, web_interface: WebInterface):
        self.led = led
        self.button = button
        self.audio = audio
        self.model = model
        self.web_interface = web_interface

        self.active = True

    def speak_assistent(self):
        """
        startet einen einfachen sprach assistenten

        :return:
        """

        try:
            self.led.green()

            while self.active:

                if self.button.press():

                    self.led.blue()
                    query = self.audio.listen()
                    print(query)

                    if query is not None:
                        self.led.yellow()
                        response = self.model.send(query)
                        print(response)

                        self.led.white()
                        self.audio.speak(response)
                        self.led.green()

                    else:
                        self.led.red()
                        self.audio.speak("Sorry but i can't understand you.")

                        time.sleep(5)
                        self.led.green()

        except KeyboardInterrupt:
            print("exit")
            self.active = False
        except:
            self.led.red()
        finally:
            self.led.clean()
            self.button.clean()

    def cat_assistent(self):
        try:
            self.led.green()
            while self.active:
                query = input("How is you question? ")

                self.led.yellow()
                response = self.model.send(query)

                print(response)
                self.led.green()
        except KeyboardInterrupt:
            print("exit")
            self.active = False
        finally:
            self.led.clean()
            self.button.clean()

    def web_assistent(self):
        self.web_interface.start()

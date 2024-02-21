from status_led import LED
from button import Button
from audio_interface import AudioInterface
from controller_assistent import ControllerAssistent
from models import IModels, TestModel, TinyLlama11b
from web_interface import WebInterface

from time import sleep
import argparse
import ollama


class Program:

    def __init__(self, model: str, system_prompt: str, port: int, gpopPin_R: int, gpopPin_G: int, gpopPin_B: int,
                 gpioPin_button: int):

        self.model: IModels = TinyLlama11b()

        self.status_led: LED = LED(gpioPin_R=22, gpioPin_G=24, gpioPin_B=26)
        self.button: Button = Button(gpioPin=37)
        self.audio: AudioInterface = AudioInterface()
        self.webInterface = WebInterface(port)

        self.controller = ControllerAssistent(self.status_led, self.button, self.audio, self.model, self.webInterface)

    def main(self, mode):
        if mode == "speak":
            self.controller.speak_assistent()
        elif mode == "text":
            self.controller.cat_assistent()
        elif mode == "templates":
            self.controller.web_assistent()
        elif mode == "speak_web":
            pass

    @staticmethod
    def list():
        models = ollama.list()
        print(models)

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
    parser = argparse.ArgumentParser(
        prog='AI Assistent',
        description='A simple ai chat for the raspberry pi',
        epilog='Roses are Red, Violets are Blue, if you read this now can helps you')

    method = parser.add_argument_group(title="Methods",
                                       description="Run modes for the ai or print all possible ai-models")
    methode = method.add_mutually_exclusive_group()
    methode.add_argument('-s', '--speak_chat', help="a simple speak chat", action='store_true')
    methode.add_argument('-c', '--text_chat', help="a simple text chat", action='store_true')
    methode.add_argument('-w', '--web', help="a simple templates chat interface", action='store_true')
    methode.add_argument('-sw', '--speak_web', help="a simple speak and templates chat runs in multithreading",
                         action='store_true')
    methode.add_argument('-l', '--list', help="list all possible models that can be used", action='store_true')

    run_options = parser.add_argument_group(title="Settings", description="configs can be set to run")
    run_options.add_argument('-p', '--port', help="port number of webserver", type=int, default=9080)
    run_options.add_argument('-m', '--model', help="change default model", type=str)
    run_options.add_argument('-Sp', '--system_prompt', help="set custom system prompt", type=str)

    raspi = parser.add_argument_group(title="Raspberry Pi ports", description="change the default prot number for the" +
                                      " Raspberry Pi ports use fromm the led and Button")
    raspi.add_argument('-Lr', '--led_red', help="pin for red led", type=int, default=22)
    raspi.add_argument('-Lg', '--led_green', help="pin for red led", type=int, default=24)
    raspi.add_argument('-Lb', '--led_blue', help="pin for red led", type=int, default=26)
    raspi.add_argument('-b', '--button', help="pin for button", type=int, default=37)

    args = parser.parse_args()
    if args.list:
        print("list")
        # prüfen ob anderes angegeben ist
        Program.list()

    else:
        program: Program = Program(args.model, args.system_prompt, args.port, args.led_red, args.led_green, args.led_blue
                                   , args.button)

        if args.speak_chat:
            program.main("speak")
        elif args.text_chat:
            program.main("text")
        elif args.web:
            program.main("templates")
        elif args.speak_web:
            program.main("speak_web")
        else:
            parser.print_help()
            
"""
-h help show help menü

mode
-s speak_chat speak chat
-c text_chat text chat
-w web_chat templates platform to chat
-sw web_and_speak_chat templates and speak multithreading

model customization
-l list list all models
-m model change default model (default tinyllama1.1b) (later)
-Sp give a system Promt for a custom model (later)

options 
-p port port for templates (default 8089)
-L log /path/to/log (later

-Lr led_red pin for red led (22)
-Lg led_green pin for green led (24)
-Lb led_blue pin for blue led (26)
-b led_button pin for button (37)

must
-l or -s or -c or -w or -sw
optional if not -l
-m -Sp
-p if -w or -sw
-L 
[-Lr -Lg -Lb -b]
"""
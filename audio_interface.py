import pyttsx3


class AudioInterface:

    def listen(self):
        raise NotImplementedError

    def speak(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.4)

        engine.say(text)
        engine.runAndWait()

from playsound import playsound

class AudioInterface:
    def __init__(self):
        raise NotImplementedError

    def listen(self):
        raise NotImplementedError

    def speak(self, sound):
        playsound(sound)

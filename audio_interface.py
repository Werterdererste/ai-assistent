from playsound import playsound

class AudioInterface:

    def listen(self):
        raise NotImplementedError

    def speak(self, sound):
        playsound(sound)

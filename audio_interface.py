
class AudioInterface:
    def __init__(self, audioIn, audioOut):
        self.audioIn = audioIn
        self.audioOut = audioOut
        raise NotImplementedError

    def listen(self):
        raise NotImplementedError

    def speak(self):
        raise NotImplementedError

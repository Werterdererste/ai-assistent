import pyttsx3


class AudioInterface:
    """
    ist die Schnittstelle zum nutzer über Sprche.
    """
    def listen(self):
        raise NotImplementedError

    def speak(self, text):
        """
        Wandelt den übergebenen text in sprache um und gibt ihn aus.

        :param text:
        :return:
        """
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.4)

        engine.say(text)
        engine.runAndWait()

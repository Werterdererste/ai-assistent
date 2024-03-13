import pyttsx3
#from pocketsphinx import LiveSpeech
import speech_recognition as sr


class AudioInterface:
    """
    ist die Schnittstelle zum nutzer über Sprche.
    """

    def listen(self) -> str:
        """
        hört über ein mikro mit, wenn aufgehört zu sprechen wird die sprache zu text umgewandelt.
        Und zurück gegeben.
        :return:
        """
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:

            recognizer.dynamic_energy_threshold = True
            recognizer.energy_threshold = 8000
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")

            audio_data = recognizer.listen(source)
            print("Processing...")

            try:
                text = recognizer.recognize_whisper(audio_data)
                return text

            except sr.UnknownValueError:
                print("Speech API could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Speech API; {0}".format(e))

    def speak(self, text: str):
        """
        Wandelt den übergebenen text in sprache um und gibt ihn aus.

        :param text:
        :return:
        """
        engine = pyttsx3.init()
        engine.setProperty('rate', 160)
        engine.setProperty('volume', 0.4)

        engine.say(text)
        engine.runAndWait()


if __name__ == '__main__':
    """
    audio test
    """
    audio = AudioInterface()
    audio.speak("test")
    test = audio.listen()
    print(test)

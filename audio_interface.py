import pyttsx3
from pocketsphinx import LiveSpeech
import speech_recognition as sr


class AudioInterface:
    """
    ist die Schnittstelle zum nutzer über Sprche.
    """

    def listen(self):

        recognizer = sr.Recognizer()

        with sr.Microphone() as source:

            recognizer.dynamic_energy_threshold = True
            recognizer.energy_threshold = 8000

            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio_data = recognizer.listen(source)
            print("Processing...")

            try:
                # Using Google Web Speech API to recognize speech
                text = recognizer.recognize_google(audio_data)
                return text
            except sr.UnknownValueError:
                print("Google Web Speech API could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Web Speech API; {0}".format(e))

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

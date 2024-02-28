from abc import ABC, abstractmethod
import ollama


class IModels(ABC):
    """
    Abstract classe da als vorlage für alle models
    """
    @abstractmethod
    def send(self, prompt: str):
        """
        sendet ein prompt an das model und gibt eine rückgabe heraus
        :param prompt:
        :return:
        """
        pass


class TestModel(IModels):
    """
    Ein einfaches FAKE Model das zu test zwecken benutzt wird.
    """
    def send(self, prompt: str):
        return "You ask " + prompt + "i wouldn't dont answer it"


class TinyLlama11b(IModels):
    """
    Tinyllama model
    """

    def send(self, prompt: str) -> str:
        """
        sendet Antwort vom model

        :param prompt:
        :return:
        """
        response = ollama.chat(
            model='tinyllama:1.1b',
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                },
            ]
        )
        return str(response['message']['content'])

from abc import ABC, abstractmethod
import ollama


class IModels(ABC):
    """
    Abstract classe da als vorlage für alle models
    """

    @abstractmethod
    def __init__(self, model: str = None, systemprompt: str = None):
        """
        konstruktor
        ein model und ein systemprompt kann gesetzt weden wenn benötigt

        :param prompt:
        :param model:
        :param systemprompt:
        """
        pass

    @abstractmethod
    def send(self, prompt: str) -> str:
        """
        sendet ein prompt an das model und gibt eine rückgabe heraus

        :param prompt:
        :param model:
        :param systemprompt:
        :return:
        """
        pass


class TestModel(IModels):
    """
    Ein einfaches FAKE Model das zu test zwecken benutzt wird.
    """

    def __init__(self, model: str = None, systemprompt: str = None):
        pass

    def send(self, prompt: str, ):
        return "You ask " + prompt + "i wouldn't dont answer it"


class TinyLlama11b(IModels):
    """
    Tinyllama model
    """

    def __init__(self, model: str = None, systemprompt: str = None):
        pass

    def send(self, prompt: str, model: str = None, systemprompt: str = None) -> str:
        """
            sendet prompt an TinyLlama gibt antwort zurück
            ignor model and systemprompt
        :param prompt:
        :param model:
        :param systemprompt:
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


class CustomModel(IModels):
    """
    customisable model
    """

    def __init__(self, model: str = None, systemprompt: str = None):
        self.model = model
        self.systemprompt = systemprompt
        pass

    def send(self, prompt: str) -> str:
        """
        wahl eines eigenen models mit System prompt
        sendet prompt ans model und gibt antwort zurück

        :param systemprompt:
        :param model:
        :param prompt:
        :return:
        """
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    'role': 'system',
                    'content': self.systemprompt,
                },
                {
                    'role': 'user',
                    'content': prompt,
                },
            ]
        )
        return str(response['message']['content'])

import ollama


class TinyLlama11b:
    """
    Tinyllama model
    """
    def send(self, prompt: str) -> str:
        """
        sendet Andwort vom model

        :param prompt:
        :return:
        """
        response = ollama.chat(model='tinyllama:1.1b', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
        ])
        return str(response['message']['content'])

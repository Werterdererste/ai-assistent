import ollama


class TinyLlama11b:

    def send(self, prompt: str) -> str:
        response = ollama.chat(model='tinyllama:1.1b', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
        ])
        output: str = str(response['message']['content'])
        return "output"

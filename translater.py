
class Translater:
    def audio_to_text(self) -> str:
        raise NotImplementedError

    def text_to_audio(self, text: str):
        raise NotImplementedError

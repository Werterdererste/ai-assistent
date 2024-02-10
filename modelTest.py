

class ModelTest:
    """
    fake model
    """
    def send(self, prompt: str) -> str:
        """
        ein einfaches FAKE Model das zu testzecken benutzt wird.
        :param prompt:
        :return:
        """
        if prompt != None:
            return "You ask " + prompt + "i wouldn't dont answer it"
        else:
            return "I can't understand you."
import re

WORDS = ["SPECIAL","CASE"]


def handle(text, mic, profile):
    text = text.replace("SPECIAL","").replace("CASE","")
    mic.say(text)

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bSPECIAL CASE\b', text, re.IGNORECASE))


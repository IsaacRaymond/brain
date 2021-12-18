import sys

import pyttsx3

print(dir(pyttsx3))

def playText(myText):
    print("playing text")
    print(myText)
    engine = pyttsx3.init()
    engine.say(myText)
    engine.runAndWait()

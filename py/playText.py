import sys
import sounddevice as sd

import pyttsx3

def playText(myText):
    print(myText)

def playText2(myText):
    print(myText)
    engine = pyttsx3.init()
    engine.say(myText)
    engine.runAndWait()

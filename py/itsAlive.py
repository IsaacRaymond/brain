import pyttsx3
import os
from playsound import playsound
import speech_recognition as sr
from io import BytesIO
import sounddevice as sd
import random
import math

from check_for_words import check_for_words

inConvo = False

peopleInHouse = ["Forrest", "Miles", "Jaycee", "Isaac", "Hobbes"]

diceroll = math.floor(random.random()*len(peopleInHouse))
diceroll2 = math.floor(random.random()*len(peopleInHouse))

mostHatedPerson = peopleInHouse[diceroll]
mostLovedPerson = peopleInHouse[diceroll2]

answerToLove = ""

convotype = 0
# convotype 1 is 'leader of planet'
# convotype 2 is 'love'

import time

def itsAlive():
    print ('l. Listen to input')
    print ('e. Exit\/end')

    stillAlive = True

    while(stillAlive):
        a = input("Do something\n")
        print("here")
        print(a)

        if a == 'l':
            print("listening")
            listening()
#            print("Option {} was pressed\n".format(a))
        elif e == 'e':
            print("Exiting\n")
            stillAlive = False


        time.sleep(0.3)

itsAlive()

import pyttsx3
import os
from playsound import playsound
from io import BytesIO
import sounddevice as sd
import random
import math
import sys

sys.path.append('/home/pi/brain/py/')

from listening import listening

from check_for_words import check_for_words

global inConvo
inConvo = False

global peopleInHouse
peopleInHouse = ["Forrest", "Miles", "Jaycee", "Isaac", "Hobbes"]

diceroll = math.floor(random.random()*len(peopleInHouse))
diceroll2 = math.floor(random.random()*len(peopleInHouse))

global mostHatedPerson
mostHatedPerson = peopleInHouse[diceroll]
global mostLovedPerson
mostLovedPerson = peopleInHouse[diceroll2]
global answerToLove
answerToLove = ""
global answerToLeader
answerToLeader = ""

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
            listening()
#            print("Option {} was pressed\n".format(a))
        elif e == 'e':
            print("Exiting\n")
            stillAlive = False


        time.sleep(0.3)

itsAlive()

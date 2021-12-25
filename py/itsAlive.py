import pyttsx3
import os
from playsound import playsound
from io import BytesIO
import sounddevice as sd
import random
import math
import sys
import RPi.GPIO as gpio
import time

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


def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    
def initRight():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    
def initLeft():
    gpio.setmode(gpio.BCM)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    
def forward(tf):
    init()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(tf)
    gpio.cleanup()
    
def left(tf):
    initLeft()
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(tf)
    gpio.cleanup()
    
def right(tf):
    initRight()
    gpio.output(17, False)
    gpio.output(22, True)
    time.sleep(tf)
    gpio.cleanup()

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
        elif a == 'exit':
            print("Exiting\n")
            stillAlive = False
            
        elif a == "w":
            forward(2)
            
        elif a == "q":
            left(1)
            
        elif a == "e":
            right(1)


        time.sleep(0.3)

itsAlive()

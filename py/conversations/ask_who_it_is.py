import random
import math
import sys

import json

sys.path.append('/home/pi/brain/py/')
sys.path.append('/home/pi/brain/py/commands/')
sys.path.append('D:/Developer/brain/py/')
sys.path.append('D:/Developer/brain/py/commands/')

from check_for_words import check_for_words

data = {}

data_file_path = 'D:/Developer/brain/py/conversations/data.txt'
#data_file_path = '/home/pi/brain/py/conversations/data.txt'

def ask_who_it_is():
    global data

    diceroll = math.floor(random.random()*3)

    if diceroll == 0:
        playText("Who are you?")
        response = listening3()

    elif diceroll == 1:
        playText("Who is speaking to me?")
        response = listening3()

    else:
        playText("What is your name?")
        response = listening3()

    if ( check_for_words(response.lower(), ["forest"]) ):
        playText("Hello forrest")
        return "forrest"

    elif ( check_for_words(response.lower(), ["mile"]) or check_for_words(response.lower(), ["miles"])):
        playText("Hello miles")
        return "miles"

    elif ( check_for_words(response.lower(), ["jay"]) or check_for_words(response.lower(), ["sea"]) or check_for_words(response.lower(), ["jaycee"])):
        playText("Hello jaycee")
        return "jaycee"

    elif ( check_for_words(response.lower(), ["isaac"]) or check_for_words(response.lower(), ["sack"])):
        playText("Hello isaac")
        return "isaac"




def listening3():
    userInput = input("type your voice words")
    return userInput

def listening():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        user_input =  r.recognize_google(audio)
        print(user_input)
        processSpeaking(user_input.lower())

    except sr.UnknownValueError:
        diceroll = math.floor(random.random()*3)
        if diceroll == 0:
            playText("Don't hit me, but I don't know what you said.")
        elif diceroll == 1:
            playText("What did you say? I don't know.")
        else:
            playText("I didn't understand.")
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        playText("Google screwed up.  AGAIN.")
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

import random
import math
import sys
sys.path.append('/home/pi/brain/py/')
sys.path.append('/home/pi/brain/py/commands/')
sys.path.append('/home/pi/brain/py/games/tic-tac-toe/')
from playMeme import playMeme
from playSomething import playSomething
from check_for_words import check_for_words
from shutUp import shutUp
from checkConvoStatus import checkConvoStatus
from startConvo import startConvo
from tic_tac_toe import startGame

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

def processStatement(user_input):
    #if (inConvo):
    #    checkConvoStatus(user_input)
    #    print('in convo')

    if (False):
        print('yes')
        
    elif (check_for_words(user_input, ["play", "tic"]) or check_for_words(user_input, ["play", "toe"])):
        startGame()

    elif (check_for_words(user_input,["play"])):
        playSomething(user_input)

    elif (check_for_words(user_input,["dance"])):
        dance()

    elif (check_for_words(user_input,["how","are","you"]) or (check_for_words(user_input, ["what","up"]) and len(user_input) < 16) or (check_for_words(user_input, ["what's","up"]) and len(user_input) < 16) or (check_for_words(user_input, ["what","doing"])) ):
        inConvo = True
        startConvo()

    else:
        shutUp()


#    try:
#        if isItQuestion(r.recognize_google(audio)):
#            print("You asked a question")
#            playText("You asked a question")
#            continue
#        else:
#            print("You made a statement")
#            print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
#            playText("You made a statement.")
#            playText("You said " + r.recognize_google(audio))
#            continue
#    except sr.UnknownValueError:
#            print("Google Speech Recognition could not understand audio")
#            playText("I didn't understand what you said.")
#    except sr.RequestError as e:
#            print("Could not request results from Google Speech Recognition service; {0}".format(e))
#            playText("There's probably something wrong.")

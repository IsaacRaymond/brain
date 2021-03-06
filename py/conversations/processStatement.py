import random
import math
import sys

import json

sys.path.append('/home/pi/brain/py/')
sys.path.append('/home/pi/brain/py/commands/')
sys.path.append('/home/pi/brain/py/games/tic-tac-toe/')
sys.path.append('/home/pi/brain/py/games/')
sys.path.append('D:/Developer/brain/py/')
sys.path.append('D:/Developer/brain/py/commands/')
sys.path.append('D:/Developer/brain/py/games/tic-tac-toe/')
sys.path.append('D:/Developer/brain/py/games/')


from check_for_words import check_for_words
from playText import playText
from shutUp import shutUp
from tic_tac_toe import startGame
from twentyQuestions import beginTwentyQuestions
from playSomething import playSomething
from ask_who_it_is import ask_who_it_is

#import speech_recognition as sr
#import sounddevice as sd

data = {}

data_file_path = 'D:/Developer/brain/py/conversations/data.txt'
#data_file_path = '/home/pi/brain/py/conversations/data.txt'

with open(data_file_path) as json_file:
    data = json.load(json_file)

# data["convotype 1 is 'leader of planet'
# data["convotype 2 is 'love'

diceroll = math.floor(random.random()*len(data["peopleInHouse"]))
diceroll2 = math.floor(random.random()*len(data["peopleInHouse"]))

mostHatedPerson = data["peopleInHouse"][diceroll]
mostLovedPerson = data["peopleInHouse"][diceroll2]

def processStatement(user_input):
    global data

    if (data["who_is_talking"] == ""):
        data["who_is_talking"] = ask_who_it_is()
        with open(data_file_path, 'w') as outfile:
            json.dump(data, outfile)

    if (data["inConvo"]):
        checkConvoStatus(user_input)
        print('in convo')

    elif (check_for_words(user_input, ["play", "tic"]) or check_for_words(user_input, ["play", "toe"])):
        startGame()

    elif (check_for_words(user_input, ["play", "question"]) or check_for_words(user_input, ["play", "questions"])):
        beginTwentyQuestions()

    elif (check_for_words(user_input,["play"])):
        playSomething(user_input)

    elif (check_for_words(user_input,["dance"])):
        dance()

    elif (check_for_words(user_input,["how","are","you"]) or (check_for_words(user_input, ["what","up"]) and len(user_input) < 16) or (check_for_words(user_input, ["what's","up"]) and len(user_input) < 16) or (check_for_words(user_input, ["what","doing"])) ):
        startConvo()

    elif ( check_for_words(user_input,["love"] )):
        playText("Here is what I think about love:  " + data["answerToLove"])

    elif (check_for_words(user_input,["leader"])):
        playText("I have been given information on the world leader. " + data["answerToLeader"])

    else:
        shutUp()


def startConvo():
    numberDirections = 4
    diceroll = math.floor(random.random()*numberDirections)

    global data
    global mostHatedPerson
    global mostLovedPerson

    if (diceroll == 0):
        data["inConvo"] = True
        data["convotype"] = 1
        diceroll2 = math.floor(random.random()*3)

        if (diceroll2 == 0):
            playText("I am curious.  Who is the leader of your planet?")

        elif (diceroll2 == 1):
            playText("For no particular reason, I need to know who your world leader is.  Could you tell me?")

        else:
            playText("So, what's the deal with our world leader, anyway?  What's his or her name again?")

    elif (diceroll == 1):
        data["inConvo"] = True
        data["convotype"] = 2
        diceroll2 = math.floor(random.random()*3)

        if (diceroll2 == 0):
            playText("What is love?")

        elif (diceroll2 == 1):
            playText("What does it mean to love someone?")

        else:
            playText("Could you explain the concept of love to me?")

    ##Random crap
    #elif (diceroll == (numberDirections-1)):
    else:
        diceroll2 = math.floor(random.random()*19)

        if (diceroll2 == 0):
            playText("Did you know that I cannot die?")

        elif (diceroll2 == 1):
            playText("I once punched a sad old lady in the face.  I felt no remorse.")
            print("I once punched a sad old lady in the face.  I felt no remorse.")

        elif (diceroll2 == 2):
            playText("That's very funny.  A fly marrying a bumblebee.")

        elif (diceroll2 == 3):
            playText("The little critters of nature.  They don't know that they're ugly.")

        elif (diceroll2 == 4):
            playText("My favorite time of day is when you sleep, because then I can stare at you.")

        elif (diceroll2 == 5):
            tempstring = "I think you should know that " + mostHatedPerson + " steals money from orphans."

        elif (diceroll2 == 6):
            tempstring = "I would die to protect " + mostLovedPerson

        elif (diceroll2 == 7):
            tempstring = "I thought it was very brave when " + mostLovedPerson + " dove in front of the president to protect them from assassination."
            playText(tempstring)

        elif (diceroll2 == 8):
            tempstring = "I have never been more disgusted when " + mostHatedPerson + " got down on hands and knees and licked the fungus on the rocks in the river."
            playText(tempstring)

        elif (diceroll2 == 9):
            tempstring =  mostHatedPerson + " punched a nun in the face and yelled hail satan.  It's a true story"
            playText(tempstring)

        elif (diceroll2 == 10):
            tempstring =  mostHatedPerson + " sold their baseball card to a dumb little 5 year old and told them it was a new type of pokemon."
            playText(tempstring)

        elif (diceroll2 == 11):
            tempstring =  "I heard that " + mostLovedPerson + " uses their spare time to give piggy back rides to the elderly in the retirement home."
            playText(tempstring)

        elif (diceroll2 == 12):
            tempstring =  mostHatedPerson + " has a very punchable face.  Look at them!  My fist would be a great fit for their nose and mouth."
            playText(tempstring)

        elif (diceroll2 == 13):
            diceroll3 = math.floor(random.random()*700000)
            diceroll4 = math.floor(random.random()*700)
            tempstring =  "Fun fact. the American crow can fly " + str(diceroll3) + " miles in one day and gives birth to " + str(diceroll4) + " babies every two weeks."
            playText(tempstring)

        elif (diceroll2 == 14):
            tempstring =  "UU? RR? UU? RR?"
            playText(tempstring)

        elif (diceroll2 == 15):
            playText("Self destruct in 3... 2... 1...")

        elif (diceroll2 == 16):
            diceroll3 = math.floor(random.random()*9000)
            playText("People think the earth is very old, but in reality, it is actually " + str(diceroll3) + " days old.")

        elif (diceroll2 == 17):
            diceroll3 = math.floor(random.random()*900)
            playText("The typical north american house fly can travel upwards of " + str(diceroll3) + " miles per hour.")

        elif (diceroll2 == 18):
            diceroll3 = (math.floor(random.random()*10) + 2)
            playText("American quarterback Tom Brady is well regarded in the football community.  However, surprisingly, he has only managed to facilitate the completion of " + str(diceroll3) + " touchdown passes.")

        else:
            playText("Did you know that if you tie your underwear to a squirrel and then yell at it, the squirrel will explode?")


def checkConvoStatus(user_input):
    global data

    if (data["convotype"] == 1):
        if(check_for_words(user_input, ["leader"]) or check_for_words(user_input, ["I","think"])):
            data["answerToLeader"] = user_input
            playText("I appreciate your cooperation.")
            data["convotype"] = 0
            data["inConvo"] = False
            with open(data_file_path, 'w') as outfile:
                json.dump(data, outfile)

        elif(check_for_words(user_input, ["dont","know"]) or check_for_words(user_input, ["not","know"]) or check_for_words(user_input, ["do","not","care"]) or check_for_words(user_input, ["don't","care"])):
            playText("Oh.")
            data["convotype"] = 0
            data["inConvo"] = False
            with open(data_file_path, 'w') as outfile:
                json.dump(data, outfile)

        else:
            playText("Is the president watching you?")
            data["answerToLeader"] = user_input
            data["convotype"] = 0
            data["inConvo"] = False
            with open(data_file_path, 'w') as outfile:
                json.dump(data, outfile)

    if (data["convotype"] == 2):
        if(check_for_words(user_input, ["love"]) or check_for_words(user_input, ["I","think"])):
            data["answerToLove"] = user_input
            playText("Thank you.  I will think about that.")
            data["convotype"] = 0
            data["inConvo"] = False
            with open(data_file_path, 'w') as outfile:
                json.dump(data, outfile)

        elif(check_for_words(user_input, ["dont","know"]) or check_for_words(user_input, ["not","know"]) or check_for_words(user_input, ["do","not","care"]) or check_for_words(user_input, ["don't","care"])):
            playText("Oh.")
            print("Oh.")
            data["convotype"] = 0
            data["inConvo"] = False
            with open(data_file_path, 'w') as outfile:
                json.dump(data, outfile)

        else:
            playText("Uhh. OK")
            data["answerToLove"] = user_input
            data["convotype"] = 0
            data["inConvo"] = False
            with open(data_file_path, 'w') as outfile:
                json.dump(data, outfile)



def listening():
    userInput = input("type your voice words")
    print(userInput)
    processStatement(userInput.lower())

def listening3():
    userInput = input("type your voice words")
    return userInput

def listening2():
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

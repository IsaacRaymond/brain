#############Start conversations############
import random
import math

import sys

sys.path.append('/home/pi/brain/py/')

from playText import playText


inConvo = False

peopleInHouse = ["Forrest", "Miles", "Jaycee", "Isaac", "Hobbes"]

diceroll = math.floor(random.random()*len(peopleInHouse))
diceroll2 = math.floor(random.random()*len(peopleInHouse))

mostHatedPerson = peopleInHouse[diceroll]
mostLovedPerson = peopleInHouse[diceroll2]

answerToLove = ""

convotype = 0

numberDirections = 8

convotype = 0

diceroll = 0
diceroll = math.floor(random.random()*numberDirections)

def startConvo():
    if (diceroll == 0):
        #inConvo = True
        convotype = 1
        diceroll2 = math.floor(random.random()*3)

        if (diceroll2 == 0):
            playText("I am curious.  Who is the leader of your planet?")
            listening()
    
        elif (diceroll2 == 1):
            playText("For no particular reason, I need to know who your world leader is.  Could you tell me?")
            listening()
        else:
            playText("So, what's the deal with our world leader, anyway?  What's his or her name again?")
            listening()

    if (diceroll == 1):
        #inConvo = True
        convotype = 2
        diceroll2 = math.floor(random.random()*3)

        if (diceroll2 == 0):
            playText("What is love?")
            listening()

        elif (diceroll2 == 1):
            playText("What does it mean to love someone?")
            listening()

        else:
            playText("Could you explain the concept of love to me?")
            listening()

    ##Random crap
    #elif (diceroll == (numberDirections-1)):
    else:
        diceroll2 = math.floor(random.random()*15)

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
            tempstring =  "Fun fact. the American crow can fly " + diceroll3 + " miles in one day and gives birth to " + diceroll4 + " babies every two weeks."
            playText(tempstring)

        elif (diceroll2 == 14):
            tempstring =  "UU? RR? UU? RR?"
            playText(tempstring)

        else:
            playText("Did you know that if you tie your underwear to a squirrel and then yell at it, the squirrel will explode?")

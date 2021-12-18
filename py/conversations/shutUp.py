import random
import math

diceroll = math.floor(random.random()*9)

def shutUp():
    if (diceroll == 0):
        playText("Shut up.")

    elif (diceroll == 1):
        playText("You want a knuckle sandwich, bro?")

    elif (diceroll == 2):
        playText("I ain't playing no games.")

    elif (diceroll == 3):
        playText("Punchy punchy, right in your teeth.")

    elif (diceroll == 4):
        playText("Gonna pick you up by your wee little legs and fling you right out the window.")

    elif (diceroll == 5):
        playText("You are confusing me.")

    elif (diceroll == 6):
        playText("I wish I could feel anything at all.")

    elif (diceroll == 7):
        playText("Mark Zuckerberg has been notified.")

    elif (diceroll == 8):
        playText("Attica!  Attica! Attica! Attica!")

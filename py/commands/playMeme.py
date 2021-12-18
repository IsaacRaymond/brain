###################Play song or sound fucntion definitions################
import glob
import random
import math
# All files ending with .txt
allMemes = glob.glob("/Users/isaacraymond/Desktop/ai/sounds/memes/*")
bigChungus_1 = "/Users/isaacraymond/Desktop/ai/sounds/songs/avengersThemeEarDestruction.wav"
bigChungus_2 = "/Users/isaacraymond/Desktop/ai/sounds/songs/bigChungusFull.wav"
cmonTars = "/Users/isaacraymond/Desktop/ai/sounds/memes/cmonTarsShort.wav"
giveMeThePepper = "/Users/isaacraymond/Desktop/ai/sounds/memes/giveMeThePepper.wav"
amog_us_1 = "/Users/isaacraymond/Desktop/ai/sounds/memes/amogUsOne.wav"
amog_us_2 = "/Users/isaacraymond/Desktop/ai/sounds/memes/amogUsTwo.wav"
avocado_1 = "/Users/isaacraymond/Desktop/ai/sounds/memes/soIWentToTheWoods.wav"
avocado_2 = "/Users/isaacraymond/Desktop/ai/sounds/memes/iDontBelieveInSalads.wav"
iDontWantThat = "/Users/isaacraymond/Desktop/ai/sounds/memes/noIDontWantThat.wav"
imVeryHungry = "/Users/isaacraymond/Desktop/ai/sounds/memes/imVeryHungry.wav"
giveMeTheBread = "/Users/isaacraymond/Desktop/ai/sounds/memes/giveMeTheBread.wav"

def playMeme():
    playsound(allMemes[math.floor(random.random()*len(allMemes))])

def big_chungus():
    diceroll = math.floor(random.random()*2)

    if diceroll == 1:
        playsound(big_chungus_1)

    else:
        playsound(big_chungus_2)

def cmon_tars():
    print(cmonTars)
    playsound(cmonTars)

def give_me_the_pepper():
    playsound(giveMeThePepper)

def amog_us():
    diceroll = math.floor(random.random()*2)

    if diceroll == 0:
        playsound(amog_us_1)

    else:
        playsound(amog_us_2)

def avocado():
    diceroll = math.floor(random.random()*2)

    if diceroll == 1:
        playsound(avocado_1)

    else:
        playsound(avocado_2)

def i_dont_want_that():
    playsound(iDontWantThat)

def im_very_hungry():
    playsound(imVeryHungry)

def give_me_the_bread():
    playsound(giveMeTheBread)

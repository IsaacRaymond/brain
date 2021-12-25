import sys
sys.path.append('/home/pi/brain/py/')
from check_for_words import check_for_words
import glob
import random
import math
import pygame

def playSomething(user_input):
    pygame.mixer.init()
        #######Playing specific sounds
    if (check_for_words(user_input,["chungus"]) or check_for_words(user_input,["big"])):
        big_chungus()

    elif ( check_for_words(user_input,["come","on","tars"]) or check_for_words(user_input,["come","on"]) or check_for_words(user_input,["come","tars"]) or check_for_words(user_input,["tires"]) ):
        cmon_tars()

    elif ( check_for_words(user_input, ["give","pepper"]) ):
        give_me_the_pepper()

    elif ( check_for_words(user_input, ["meme"])):
        playMeme()

    elif ( check_for_words(user_input, ["us", "mug"]) or check_for_words(user_input, ["Among"]) or check_for_words(user_input, ["among"]) ):
        amog_us()
        
    elif ( check_for_words(user_input, ["calling"])):
        im_calling_corporate()

    elif ( check_for_words(user_input, ["avocado"]) ):
        avocado()

    elif ( check_for_words(user_input, ["I","want","that"])):
        i_dont_want_that()

    elif ( check_for_words(user_input, ["very","hungry"])):
        im_very_hungry()

    elif ( check_for_words(user_input, ["give","bread"])):
        give_me_the_bread()

    else:
        print("nothing")

###################Play song or sound fucntion definitions################
# All files ending with .txt
allMemes = glob.glob("/home/pi/brain/sounds/memes/*")
big_chungus_1 = "/home/pi/brain/sounds/songs/avengers_theme_ear_destruction.wav"
big_chungus_2 = "/home/pi/brain/sounds/songs/big_chungus_full.wav"
cmonTars = "/home/pi/brain/sounds/memes/cmonTarsShort.wav"
giveMeThePepper = "/home/pi/brain/sounds/memes/giveMeThePepper.wav"
amog_us_1 = "/home/pi/brain/sounds/memes/amogUsOne.wav"
amog_us_2 = "/home/pi/brain/sounds/memes/amogUsTwo.wav"
avocado_1 = "/home/pi/brain/sounds/memes/soIWentToTheWoods.wav"
avocado_2 = "/home/pi/brain/sounds/memes/iDontBelieveInSalads.wav"
iDontWantThat = "/home/pi/brain/sounds/memes/noIDontWantThat.wav"
imVeryHungry = "/home/pi/brain/sounds/memes/imVeryHungry.wav"
giveMeTheBread = "/home/pi/brain/sounds/memes/giveMeTheBread.wav"
imCallingCorporate = "/home/pi/brain/sounds/memes/imCallingCorporate.wav"

def playMeme():
    play_wav_file(allMemes[math.floor(random.random()*len(allMemes))])

def big_chungus():
    diceroll = math.floor(random.random()*2)

    if diceroll == 1:
        play_wav_file(big_chungus_1)

    else:
        play_wav_file(big_chungus_2)

def cmon_tars():
    print(cmonTars)
    play_wav_file(cmonTars)

def give_me_the_pepper():
    play_wav_file(giveMeThePepper)

def amog_us():
    diceroll = math.floor(random.random()*2)

    if diceroll == 0:
        play_wav_file(amog_us_1)

    else:
        play_wav_file(amog_us_2)

def avocado():
    diceroll = math.floor(random.random()*3)

    if diceroll == 1:
        play_wav_file(avocado_1)
        
    elif diceroll == 2:
        im_calling_corporate()

    else:
        play_wav_file(avocado_2)

def i_dont_want_that():
    play_wav_file(iDontWantThat)

def im_very_hungry():
    play_wav_file(imVeryHungry)

def give_me_the_bread():
    play_wav_file(giveMeTheBread)
    
def im_calling_corporate():
    play_wav_file(imCallingCorporate)
    
def play_wav_file(name_of_file):
    pygame.mixer.music.load(name_of_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
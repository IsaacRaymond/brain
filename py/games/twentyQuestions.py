import sys
sys.path.append('/home/pi/brain/py')
from playText import playText
import sounddevice as sd
import numpy as np
import speech_recognition as sr
import sys
import random
import math


def askQ(prompt, func_1, func_2,):
    playText(prompt)
    response = listening()

    if response == 'yes':
        func_1()

    elif response == 'no':
        func_2()

    else:
        playText("I didn't get that.")
        askQ(prompt, func_1, func_2)


def listening():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        user_input =  r.recognize_google(audio)
        print(user_input)
        return (user_input.lower())

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


def beginTwentyQuestions():
    askQ("Does your animal have a backbone?", vertebrate, invertebrate)        

def invertebrate():
    askQ("Is it a bug?", bug, tentacles)

def tentacles():
    askQ("Does it have tentacles?",bigTentacle, noTentacles)

def bigTentacle():
    askQ("Does it have an antenna in front of its head?", mosquito, grasshopper)

def mosquito():
    playText("It is a mosquito")

def grasshopper():
    playText("It is a grasshopper")

def bug():
    askQ("Does it have large wings?", butterfly, smallWingBug)

def butterfly():
    playText("It is a butterfly")

def smallWingBug():
    askQ("Does your animal have long rear legs?", longRearLegs, shortRearLegs)

def shortRearLegs():
    askQ("Does it have a head with big claws in the front?", beetle, noBigClaws())

def beetle():
    playText("It is a beetle or I should be destroyed")

def noBigClaws():
    askQ("Does it have small eyes?", ant, ladybugOrSpider())

def ant():
    playText("It is an ant")

def ladybugOrSpider():
    askQ("Is it a ladybug?", ladybug, spider)

def ladybug():
    playText("It is a ladybug.")

def spider():
    playText("It is a spider")

def longRearLegs():
    askQ("Does your bug have an antenna in front of its head?", mosquito, grasshopper)

def mosquito():
    playText("It is a mosquito")

def grasshopper():
    playText("It is a grasshopper")

def vertebrate():
    playText("Is it a mammal?")
    response= listening()

    if (response == "yes"):
        mammal()

    elif response == "no":
            playText("Does it have feathers?")
            response= listening()

            if response=="yes":
                bird()

            elif response=="no":
                playText("does it have dry skin?")
                response= listening()

                if response == "yes":
                    reptile()

                elif response == "no":
                    playText("does it live in the ocean?")
                    response= listening()

                    if response == "yes":
                        ocean()

                    elif response == "no":
                        playText("It is a frog or a toad, or I'm just dumb")

                    else:
                        playText("I didn't get that.")
                        vertebrate()

                else:
                    playText("I did not hear you correctly")
                    vertebrate()

            else:
                playText("I did not understand")
                vertebrate()

    else:
        playText("I did not understand")
        vertebrate()

def bird():
    askQ("Is it smaller or equal size to a seagull?", smallBird, largeBird)

def smallBird():
    askQ("Does it have webbed feet?", webbedFeet, noWebbedFeet)

def largeBird():
    askQ("Do people eat it a lot?", chicken, notChicken)

def chicken():
    playText("It is a chicken.")

def notChicken():
    askQ("Would you find it at a lake in Northern America?", lake, notLake)

def notLake():
    askQ("Is it pink?", flamingo, notFlamingo)

def flamingo():
    playText("It is a flamingo")

def notFlamingo():
    askQ("Does it live in a cold climate?", penguin, ostrich)

def penguin():
    playText("It is a penguin")

def ostrich():
    playText("It is an ostrich")

def lake():
    askQ("Does it go hoo hoo whoo whoo?", owl, notOwl)

def owl():
    playText("It is an owl")

def notOwl():
    askQ("Does it spend most of its feeding time floating on the water?", duckOrLoon, falconOrEagle)

def duckOrLoon():
    askQ("Is it a duck?", duck, loon)

def duck():
    playText("It is a duck")

def loon():
    playText("It is a loon")

def falconOrEagle():
    askQ("Is it a symbol of freedom?", eagle, falcon)

def eagle():
    playText("It is an eagle")

def falcon():
    playText("It is a falcon")

def webbedFeet():
    askQ("Does it have grey wings?", gull, crow) 
    
def gull():
    playText("It is a seagull")

def crow():
    playText("It is a crow")

def reptile():
    askQ("Does it scare people?", scaryReptile, notScaryReptile)

def scaryReptile():
    askQ("Does this animal have no legs?", snake, alligator)

def notScaryReptile():
    askQ("Does it have a hard shell?", turtle, notTurtle)

def turtle():
    playText("It is a turtle")

def notTurtle():
    playText("It is a lizard, a gecko, or an iguana or something")

def snake():
    playText("It is a snake")

def alligator():
    playText("It is an alligator or crocodile")
    
def ocean():
    askQ("Does it have tentacles?", tentacles, noTentacles)
    
def noTentacles():
    askQ("Do people eat it a lot?", shrimp, notShrimp)

def shrimp():
    playText("It is a shrimp")

def notShrimp():
    askQ("Does it eat fish?", eatFish, starfish)

def starfish():
    playText("It is a starfish")

def eatFish():
    askQ("Is it one of the biggest creatures on earth?", whale, notWhale)

def whale():
    playText("It is a whale")

def notWhale():
    askQ("Is it big and fat?", seal, penguinSharkDolphin)

def seal():
    playText("It is a seal or sea lion")

def penguinSharkDolphin():
    askQ("Did it punch mahatma gandhi in the face?", penguin, sharkDolphin)

def penguin():
    playText("It is a dolphin")

def sharkDolphin():
    askQ("Does it have a high level of intelligence?", dolphin, notDolphin)

def dolphin():
    playText("It is a dolphin.")

def notDolphin():
    askQ("Does it show up in nightmares?", shark, otter)

def shark():
    playText("It is a shark")

def otter():
    playText("It is an otter")

def tentacles():
    askQ("Does it sometimes sting people?", sting, noSting)
    
def noSting():
    askQ("Does it have big, meaty claws?", lobster, octopus)

def lobster():
    playText("It is a crab or lobster of some sort.")

def octopus():
    playText("It is an octopus")

def sting():
    askQ("Does it go great on toast?", jellyfish, stingrayEel)

def jellyfish():
    playText("It is a jellyfish")

def stingrayEel():
    askQ("Does it have a stinger in the back?", stingray, eel)

def stingray():
    playText("It is a stingray")

def eel():
    playText("It is an eel")

def mammal():
    askQ("Does it lay eggs?", smoothFur, notSmoothFur)

def notSmoothFur():
    askQ("Does it keep young in its pouch?", liveInGround, haveWings)

def haveWings():
    askQ("Does it have wings?", bats, monkeyOrHuman)

def bats():
    playText("It is a bat")

def monkeyOrHuman():
    askQ("Is it capable of creating computer programs?", human, monkeysOrSomething)

def human():
    playText("It is a human")

def monkeysOrSomething():
    askQ("Does it fling poop or swing in trees?", monkeys, nonMonkeys)

def monkeys():
    askQ("Did we shoot one of these guys injustly?", gorilla, otherMonkey)

def gorilla():
    playText("It is a gorilla")

def otherMonkey():
    playText("It is a spider monkey, a chip, an orangutan or something like that")

def liveInGround():
    askQ("Does it live in burrows in the ground?", kangarooWallaby, koala)

def kangarooWallaby():
    playText("It is a Kangaroo or Wallaby")

def koala():
    playText("It is a Koala")

def smoothFur():
    askQ("Does it have smooth fur?", platypus, anteater)

def platypus():
    playText("It is a platypus")

def anteater():
    playText("It's an anteater")

def nonMonkeys():
    askQ("Does it walk on four legs?", manualLabor, eatFish)

def manualLabor():
    askQ("Is it used for manual labor?", horseDonkeyMule, producing)

def horseDonkeyMule():
    askQ("Do people also call this animal a swear word?", donkey, horse)

def donkey():
    playText("It's a donkey or a mule")

def horse():
    playText("It is a horse")

def producing():
    askQ("Do people use this animal to produce food or clothing?", domesticated, predator)

def domesticated():
    askQ("Is it often used to produce cheese?", cowOrGoat, pigOrSheep)

def cowOrGoat():
    askQ("Is it a cow?", cow, goat)

def cow():
    playText("It is a cow.")

def goat():
    playText("It is a goat.")

def pigOrSheep():
    playText("Is it a pig?", pig, sheep)

def pig():
    playText("It is a pig")

def sheep():
    playText("It is a sheep")

def predator():
    askQ("Is it a predator?", liveAroundHerePredator, pest)

def liveAroundHerePredator():
    askQ("Does it live around here?", foxBearWolf, spots)

def spots():
    askQ("Does it have spots?", jaguarLeopardHyenaCheetah, tigerLionCougar)

def jaguarLeopardHyenaCheetah():
    askQ("Do these laugh uncontrollably?", hyena, jaguarLeopardCheetah)

def hyena():
    playText("It is a hyena")

def jaguarLeopardCheetah():
    askQ("Is it also a car?", jaguar, leopardCheetah)

def jaguar():
    playText("It is a jaguar")

def leopardCheetah():
    askQ("Is it a leopard?", leopard, cheetah)

def leopard():
    playText("It is a leopard")

def cheetah():
    playText("It is a cheetah")

def foxBearWolf():
    askQ("Is it a fox?", fox, bearWolf)

def fox():
    playText("It is a fox")

def bearWolf():
    askQ("Is it a bear?", bear, wolf)

def bear():
    playText("It is a bear")

def wolf():
    playText("It is a wolf")

def pest():
    askQ("Is it a pest?", doesItKnowKungFu, livesAroundHere)

def livesAroundHere():
    askQ("Does it live around here?", pet, hugeAfrican)

def pet():
    askQ("Is it a pet?", catDog, rabbitMooseDeer)

def rabbitMooseDeer():
    askQ("Does Hobbes eat its poop?", deer, rabbitMoose)

def deer():
    playText("It is a deer")

def rabbitMoose():
    playText("It is a rabbit or a moose.")

def catDog():
    askQ("Does it bark at nothing and poop out giant tootsie rolls?", dog, cat)

def dog():
    playText("It is a dog")

def cat():
    playText("it is a cat")

def doesItKnowKungFu():
    askQ("Does it know kung fu?", rat, miceSquirrel)

def rat():
    playText("It is a rat")

def miceSquirrel():
    askQ("Do these animals like nuts?", squirrel, mice)

def squirrel():
    playText("It is a squirrel")

def mice():
    playText("It is a mouse")

def hugeAfrican():
    askQ("Is it bigger than a deer?", bigAfrican, smallerAfrican)

def bigAfrican():
    askQ("Does it have tusks?", rhinoElephantHippo, isItFat)

def isItFat():
    askQ("Is it fat?", buffaloBisonYak, impalaAntelopeZebra)

def buffaloBisonYak():
    playText("Its a buffalo, a bison, or a yak.")

def impalaAntelopeZebra():
    askQ("Does it have spots?", zebra, antelopeImpala)

def zebra():
    playText("It is a zebra")

def antelopeImpala():
    playText("It is an antelope or an impala")

def rhinoElephantHippo():
    askQ("Does it have really good memory?", elephant, rhinoHippo)

def rhinoHippo():
    askQ("Is it a rhino?", rhino, hippo)

def elephant():
    playText("It is an elephant")

def rhino():
    playText("It is a rhino")

def hippo():
    playText("It is a hippo")

def iDontKnow():
    playText("I don't know")







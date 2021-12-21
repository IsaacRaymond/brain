import sys
import sounddevice as sd
import speech_recognition as sr

sys.path.append('/home/pi/brain/py/')

import time
import random
import os
import math
import numpy as np
from check_for_words import check_for_words
from playText import playText


users_move = ""
board = [[0,0,0],[0,0,0],[0,0,0]]
gameIsActive = True
#1 is the computer.  2 is player.

def set_users_move(stuff):
    users_move = stuff

def get_users_move():
    return users_move

def listening2():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        user_input =  r.recognize_google(audio)
        print(user_input)
        return user_input.lower()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def startGame():
    diceroll = math.floor(random.random()*2)

    if diceroll == 0:
        playText("I will start.  I will be 'x'.  Key words are bottom, center, up, left, right")
        #playText("When it is your turn, I will tell you.  State your move like this:  bottom left, or center, or center right.  The key words are left, right, top, bottom, and center.")
        computerMove()

    else:
        playText("You go first.  Key words are bottom, center, up, left, right")
        getHumanInput()



def computerMove():
    diceroll1 = int(math.floor(random.random()*3))
    diceroll2 = int(math.floor(random.random()*3))

    if board[diceroll1][diceroll2] != 0:
        computerMove()

    else:
        playText("I am choosing the " + str(wordValueOfMove([diceroll1,diceroll2])) + " square")
        board[diceroll1][diceroll2] = 1
        if checkForWin():
            playText("the game is over")

        else:
            getHumanInput()

def checkIfOccupied(givenMove):
    if board[givenMove[0]][givenMove[1]] == 0:
        return False

    else:
        return True




def wordValueOfMove(locationChoice):

    if locationChoice[0]==0 and locationChoice[1]==0:
        return "top left"

    elif locationChoice[0]==0 and locationChoice[1]==1:
        return "top center"

    elif locationChoice[0]==0 and locationChoice[1]==2:
        return "top right"

    elif locationChoice[0]==1 and locationChoice[1]==0:
        return "center left"

    elif locationChoice[0]==1 and locationChoice[1]==1:
        return "center"

    elif locationChoice[0]==1 and locationChoice[1]==2:
        return "center right"

    elif locationChoice[0]==2 and locationChoice[1]==0:
        return "bottom left"

    elif locationChoice[0]==2 and locationChoice[1]==1:
        return "bottom center"

    elif locationChoice[0]==2 and locationChoice[1]==2:
        return "bottom right"

def checkForWin():
    if board[0][0] != 0 and board[0][0] == board[0][1] == board[0][2]:
        playText("winner")
        gameIsActive = False
        return True

    elif board[1][0] != 0 and board[1][0] == board[1][1] == board[1][2]:
        playText("winner")
        gameIsActive = False
        return True

    elif board[2][0] != 0 and board[2][0] == board[2][1] == board[2][2]:
        playText("winner")
        gameIsActive = False
        return True

    elif board[0][1] != 0 and board[0][1] == board[1][1] == board[2][1]:
        playText("winner")
        gameIsActive = False
        return True

    elif board[0][2] != 0 and board[0][2] == board[1][2] == board[2][2]:
        playText("winner")
        gameIsActive = False
        return True

    elif board[0][0] != 0 and board[0][0] == board[1][0] == board[2][0]:
        playText("winner")
        gameIsActive = False
        return True

    elif board[0][0] != 0 and board[0][0] == board[1][1] == board[2][2]:
        playText("winner")
        gameIsActive = False
        return True

    elif board[0][2] != 0 and board[0][2] == board[1][1] == board[2][0]:
        playText("winner")
        gameIsActive = False
        return True

def getHumanInput():
    playText("What is your move?")
    

    print("getting move")
    move = listening2()
    print(move)

    if(check_for_words(move, ["top","left"])):
        if checkIfOccupied([0,0]):
            playText("That space currently is occupied.")
            getHumanInput()

        else:
            board[0][0] = 2
            if checkForWin():
                playText("the game is over")

            else:
                computerMove()

    elif(check_for_words(move, ["stop"])):
        gameIsActive = False

    elif(check_for_words(move, ["top","center"])):
        if checkIfOccupied([0,1]):
            playText("That space currently is occupied.")
            getHumanInput()

        else:
            board[0][1] = 2
            if checkForWin():
                playText("the game is over")

            else:
                computerMove()

    elif(check_for_words(move, ["top","right"])):
        if checkIfOccupied([0,2]):
            playText("That space currently is occupied.")
            getHumanInput()

        else:
            board[0][2] = 2
            if checkForWin():
                playText("the game is over")

            else:
                computerMove()

    elif(check_for_words(move, ["center","left"])):
        if checkIfOccupied([1,0]):
            playText("That space currently is occupied.")
            getHumanInput()

        else:
            board[1][0] = 2
            if checkForWin():
                playText("the game is over")

            else:
                computerMove()

    elif(check_for_words(move, ["center","right"])):
        if checkIfOccupied([1,2]):
            playText("That space currently is occupied.")
            getHumanInput()

        else:
            board[1][2] = 2
            if checkForWin():
                playText("the game is over")

            else:
                computerMove()

    elif(check_for_words(move, ["bottom","left"])):
        if checkIfOccupied([2,0]):
            playText("That space currently is occupied.")
            getHumanInput()

        else:
            board[2][0] = 2
            if checkForWin():
                playText("the game is over")

            else:
                computerMove()

    elif(check_for_words(move, ["bottom","center"])):
        if checkIfOccupied([2,1]):
            playText("That space currently is occupied.")
            getHumanInput()

        else:
            board[2][1] = 2
            if checkForWin():
                playText("the game is over")

            else:
                computerMove()

    elif(check_for_words(move, ["bottom","right"])):
        if checkIfOccupied([2,2]):
            playText("That space currently is occupied.")
            getHumanInput()

        else:
            board[2][2] = 2
            if checkForWin():
                playText("the game is over")

            else:
                computerMove()

    else:
        if checkIfOccupied([1,1]):
            playText("That space currently is occupied.")
            getHumanInput()

        else:
            board[1][1] = 2
            if checkForWin():
                playText("the game is over")

            else:
                computerMove()


import sounddevice as sd
import numpy as np
import speech_recognition as sr
import sys
import random
import math

sys.path.append('/home/pi/brain/')
sys.path.append('/home/pi/brain/py')

from processSpeaking import processSpeaking

def listening():
    userInput = input("type your voice words")
    print(userInput)
    processSpeaking(userInput.lower())

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

#def listening():
#    with sd.Stream(callback=print_sound):
#        sd.sleep(2000)
#        print("done sleeping")

#def print_sound(indata, outdata, frames, time, status):
#    volume_norm = np.linalg.norm(indata)*10
#    print("print_sound called")

    #if volume_norm > 30:
     #   print("loud enough")
      #  r = sr.Recognizer()
       # with sr.Microphone() as source:
        #    audio = r.listen(source)

        #try:
         #   user_input = lower( r.recognize_google(audio) )
          #  print(user_input)
           # processSpeaking(user_input)

        #except:
         #   print('couldnt detect audio')

import sounddevice as sd
import numpy as np
import speech_recognition as sr
import sys

sys.path.append('''C:/Developer/brain/py''')

from processSpeaking import processSpeaking

def listening():
    with sd.Stream(callback=print_sound):
        sd.sleep(2000)
        print("done sleeping")

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    print("print_sound called")

    if volume_norm > 30:
        print("loud enough")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            user_input = lower( r.recognize_google(audio) )
            print(user_input)
            processSpeaking(user_input)

        except:
            print('couldnt detect audio')

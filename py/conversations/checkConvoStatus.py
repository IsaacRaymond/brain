import sys

sys.path.append('/home/pi/brain/py/')

from playText import playText

def checkConvoStatus(user_input):
    if (convotype == 1):
        if(check_for_words(user_input, ["leader"]) or check_for_words(user_input, ["I","think"])):
            answerToLove = user_input
            playText("I appreciate your cooperation.")
            convotype = 0
            inConvo = False

        elif(check_for_words(user_input, ["dont","know"]) or check_for_words(user_input, ["not","know"]) or check_for_words(user_input, ["do","not","care"]) or check_for_words(user_input, ["don't","care"])):
            playText("Oh.")
            print("Oh.")
            convotype = 0
            inConvo = False

        else:
            playText("Is the president watching you?  Is that why you don't want to talk about it?")
            print("Is the president watching you?  Is that why you don't want to talk about it?")
            convotype = 0
            inConvo = False

    if (convotype == 2):
        if(check_for_words(user_input, ["love"]) or check_for_words(user_input, ["I","think"])):
            answerToLove = user_input
            playText("Thank you.  I will think about that.")
            convotype = 0
            inConvo = False

        elif(check_for_words(user_input, ["dont","know"]) or check_for_words(user_input, ["not","know"]) or check_for_words(user_input, ["do","not","care"]) or check_for_words(user_input, ["don't","care"])):
            playText("Oh.")
            print("Oh.")
            convotype = 0
            inConvo = False

        else:
            playText("I guess you don't want to talk about love anymore.")
            print("I guess you don't want to talk about love anymore.")
            convotype = 0
            inConvo = False

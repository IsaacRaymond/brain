def processQuestion(user_input):
    if (False):
        print('yes')

    elif (check_for_words(user_input,["play"])):
        playSomething(user_input)

    elif (check_for_words(user_input,["dance"])):
        dance()

    elif (check_for_words(user_input,["how","are","you"]) or (check_for_words(user_input, ["what","up"]) and len(user_input) < 16) or (check_for_words(user_input, ["what's","up"]) and len(user_input) < 16) or (check_for_words(user_input, ["what","doing"])) ):
        inConvo = True
        startConvo()

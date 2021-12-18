def playSomething(user_input):
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

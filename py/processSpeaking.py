def processSpeaking(user_input):

    #Check to see if it's overwhelmingly positive or negative
    #Check who is speaking
    #If Forrest is saying mean words, drop how much we like him

    if (itIsAQuestion(user_input)):
        processQuestion(user_input)

    else:
        processStatement(user_input)

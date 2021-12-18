def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    print("print_sound called")

    if volume_norm > 4:
        print("hey")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            user_input = lower( r.recognize_google(audio) )
            print(user_input)
            processSpeaking(user_input)

        except:
            print('couldnt detect audio')

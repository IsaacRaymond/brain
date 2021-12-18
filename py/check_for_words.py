#########Important function - check_for_words###############
def check_for_words(user_input, check_for_words_list):
    for i in range(len(check_for_words_list)):
        if check_for_words_list[i] in user_input:
            continue
        else:
            return False

    return True

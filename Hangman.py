import random

def hang_man():
    from Hangman_words import word_list
    chosen= random.choice(word_list)

    display=[]
    word_length= len(chosen)

    lives=6
    from Hangman_Art import logo

    # for letter in chosen:
    #     if letter==guess:
    #         print('Right')
    #     else:
    #         print('wrong')

    for letter in range(word_length):
        display+= "_"
    print(display)

    end_of_game= False

    while not end_of_game:
        inp= input('Guess a letter and input the same: ')
        guess= inp.lower()

        for i in range(0,word_length):
            letter= chosen[i]
            if letter==guess:
                display[i]=letter

        if guess not in chosen:
            lives-=1
            if lives== 0:
                end_of_game= True
                print("You lose")
                print("The given word was: ", chosen)

        print(display)

        if "_" not in display:
            end_of_game= True
            print("You Win!")

        from Hangman_Art import stages
        print(stages[lives])

    

if __name__ == '__main__':
    hang_man()

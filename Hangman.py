import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def hang_man():
    word_list= ["banana", "hyundai", "mountains", "sheep", "awestruck", "cantaloupe"]
    chosen= random.choice(word_list)

    display=[]
    word_length= len(chosen)

    lives=6

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

        print(display)

        if "_" not in display:
            end_of_game= True
            print("You Win!")

    

if __name__ == '__main__':
    hang_man()
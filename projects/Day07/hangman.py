import random

animal_list = [
    'dog',
    'cat',
    'horse',
    'lion',
    'tiger',
    'snake',
    'bear',
    'turtle',
    'goat',
    'raccoon',
    'deer',
    'sheep',
    'koala',
    'donkey',
    'frog',
    'ferret',
    'shark',
    'gorilla',
    'giraffe',
    'axolotl',
    'leopard',
    'cheetah',
    'sloth',
    'otter',
    'hippopotamus',
    'spider',
    'orca'
]

chosen_word = random.choice(animal_list)

chosen_letter = ""

lives = 8 # lives - hangman stage go up for every live lost

chosen_set_pile = []



def still_going(): # return bool; basically did we win yet?
    if bool(chosen_set_pile) and all(char in chosen_set_pile for char in chosen_word):
        return False
    else:
        return True

# both functions serve as the win/lose screen
def win():
    pass
def lose():
    pass

# define intial hidden word length with '_'
for i in range(len(chosen_word)):
    print('_',end="")
print()

while lives > 0 and still_going():

    chosen_letter = input('Choose letter: ')

    if chosen_letter in chosen_word and chosen_letter != "":
        if chosen_letter not in chosen_set_pile:
            chosen_set_pile.append(chosen_letter)
    else:
        lives -= 1

    for letter in chosen_word:
        if letter in chosen_set_pile:
            print(letter, end="")

        else:
            print('_',end="")

    print()
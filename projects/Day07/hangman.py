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

good_count = 0

chosen_list_pile = []

def still_going(): # return bool; basically did we win yet?
    if good_count == len(chosen_word):
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

print(chosen_word) # test

while lives > 0 and still_going():

    chosen_letter = input('Choose letter: ')

    chosen_list_pile.append(chosen_letter)

    not_there = True

    for letter in chosen_word:
        if letter in chosen_list_pile:
            print(letter, end="")
            if not_there:
                good_count += 1
            

        else:
            print('_',end="")

    print(good_count)

    print()
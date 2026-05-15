# MVP: 
# starts off with asking user if they want to play easy mode or hard mode. easy mode allows for unlimited lives
# while hard mode gives user a max of 5 lives. if their lives are used up, program will be prompt stuff (introduced later)
# prompted to guess a number, when you guess some number, program will tell you if the number you chose is
# higher or lower than the number needed to be guessed, if you get it correct, the program will then prompt you
# to play again or ultimately end. 

# stuff i learned: 
# - r"" will use the raw characters. will not process any escape sequences
# -  random.random()    Return the next random floating-point number in the range 0.0 <= X < 1.0



import random

def start_game():
    artwork = r"""

     _______               ___.                    ________                            .__                   ________                       
     \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
     /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
    /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
    \____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
            \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 

"""
    print(artwork)
    print('Welcome to the number guessing game!')

def ask_difficulty(answer):
    match answer.lower().replace(" ",""):
        case 'e':
            return True, int(random.random()*100)
        case 'h':
            return 6, int(random.random()*1000)

def check_high_low(answer, lives, rn):
    match rn:
        case num if num < answer and num != answer:
            print("Too high! Try again!")
            if type(lives) == type(67):
                return lives-1
            elif type(lives) == type(True):
                return True
        case num if num > answer and num != answer:
            print("Too Low! Try again!")
            if type(lives) == type(67):
                return lives-1
            elif type(lives) == type(True):
                return True
        case num if num == answer:
            print(f"{rn} and {answer} are the same, you win!")
            return False

start_game()
lives, rn = ask_difficulty(input('Easy: 1-100 ; Unlimited lives\nHard: 1-1000 ; 6 lives\nTo start off- what difficulty do you want to play on? Easy [e] / Hard [h]: '))
alive = "y"

while lives or lives > 0 and alive == 'y':
    answer=int(input("Guess a number: "))
    lives = check_high_low(answer,lives,rn)
    if type(67) == type(lives):
        if lives == 0:
            print(f"\nThe number was {rn}")
            print("Thanks for playing!")
        if lives == False or lives == 0:
            alive = input("Play again? [y] [n]: ").lower().replace(" ","")
            if alive == 'y':
                lives, rn = ask_difficulty(input('To start off- what difficulty do you want to play on? Easy [e] / Hard [h]: '))
import gamedata as gd
import gameart
import random

score = 0
keep_going = True

def showLogo():
    print(gameart.logo)

def showVS():
    print(gameart.vs)

def showScore(score):
    print(f"You're right! Current score: {score}")

def showOptions():
    option_A = generateOption()
    print(f"Compare A: {option_A['name']}, a {option_A['description']}, from {option_A['country']}")
    showVS()
    option_B = generateOption()
    print(f"Against B: {option_B['name']}, a {option_B['description']}, from {option_B['country']}")
    return checkWhichOptionHigher(option_A, option_B)

def generateOption(gamedata=gd):
    return random.choice(gamedata.data)

def askUserOption():
    answer = input("Who has more followers? Type 'A' or 'B': ").upper().replace(" ", "")
    return answer

def checkWhichOptionHigher(option_A, option_B):
    if option_A['follower_count'] > option_B['follower_count']:
        return 'A'
    else:
        return 'B'

def decideOutcome(higher_option, userOption, score):
    if higher_option == userOption:
        return score + 1, True
    else:
        print(f"Sorry, that's not right. Final score: {score}")
        return score, False

# main code
showLogo()
while keep_going:
    if score >= 1:
        showScore(score)
    higher_option = showOptions()
    score, keep_going = decideOutcome(higher_option, askUserOption(), score)

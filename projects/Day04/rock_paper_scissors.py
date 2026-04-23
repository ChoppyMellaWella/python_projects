# making rock paper scissors
# Notes:
    # looks like i need to learn how lists work
    # oh okay i need to import a random module
# Stuff I learned:
    # lists?
    # using random

import random

def you_win():
    print(f"Computer chose {robot_choice}. You Win!")

def you_lose():
    print(f"Computer chose {robot_choice}. You Lose!")

def you_tie():
    print(f"Computer chose {robot_choice}. It's a Tie!")

robot_choices = ["rock", "paper", "scissors"]

print("Welcome to rock paper scissors!")

user_choice = input("Choose an option! ('rock', 'paper', 'scissors'): ").strip().lower()

print(f"You chose {user_choice}!")
print("Computer is thinking...")

robot_choice = random.choice(robot_choices)

match user_choice:
    case 'rock':
        if robot_choice == 'scissors':
            you_win()
        elif robot_choice == 'paper':
            you_lose()
        else:
            you_tie()
    case 'paper':
        if robot_choice == 'rock':
            you_win()
        elif robot_choice == 'scissors':
            you_lose()
        else:
            you_tie()
    case 'scissors':
        if robot_choice == 'paper':
            you_win()
        elif robot_choice == 'rock':
            you_lose()
        else:
            you_tie()
    case _:
        print(f"Computer chose {robot_choice}! Though... you made an invalid choice- Computer wins!")

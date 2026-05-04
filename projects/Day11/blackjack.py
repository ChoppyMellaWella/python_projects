import random

cards = [1,2,3,4,5,6,7,8,9,10]

dealer_cards = []
user_cards = []

continue_game = True

def set_up_dealer(dealer_cards):
    for i in range(2):
        dealer_cards.append(random.choice(cards))
    return dealer_cards[1]
def set_up_user(user_cards):
    for i in range(2):
        user_cards.append(random.choice(cards))
    return user_cards

def choose_hit():
    user_cards.append(random.choice(cards))
    if sum(user_cards) > 21:
        lose()
def choose_stand():
    while sum(dealer_cards) <= 16:
        dealer_cards.append(random.choice(cards))
    if sum(dealer_cards) > 21:
        win()
    elif sum(dealer_cards) == sum(user_cards):
        draw()
    elif sum(dealer_cards) > sum(user_cards):
        lose()
    else:
        win()
    
def win():
    global continue_game
    print(f"Dealer cards: {dealer_cards} {sum(dealer_cards)}\nYour cards: {user_cards} {sum(user_cards)}\nYou win!")
    ask_user()
def lose():
    global continue_game
    print(f"Dealer cards: {dealer_cards} {sum(dealer_cards)}\nYour cards: {user_cards} {sum(user_cards)}\nYou lose!")
    ask_user()  
def draw():
    global continue_game
    print(f"Dealer cards: {dealer_cards} {sum(dealer_cards)}\nYour cards: {user_cards} {sum(user_cards)}\nIt's a draw!")
    ask_user()

def ask_user():
    global continue_game
    answer = input("Would you like to play again? (y) (n): ")
    if answer == 'y':
        set_up_game()
    elif answer == 'n':
        print("Thank you for playing!")
        continue_game = False
    else:
        print('invalid option')
        continue_game = False

def decide(hit_or_stand):
    if hit_or_stand == 'h':
        choose_hit()
    elif hit_or_stand == 's':
        choose_stand()
    else:
        print("invalid option")

def set_up_game():
    dealer_cards.clear()
    user_cards.clear()
    set_up_dealer(dealer_cards)
    set_up_user(user_cards)
    global continue_game
    continue_game = True

set_up_game()

while continue_game:
    print()
    print(f"The dealer's card: {dealer_cards[1]}")
    print(f"Your cards: {user_cards} {sum(user_cards)}")
    hit_or_stand = input("Do you wish to hit (h) or stand (s)?: ")
    decide(hit_or_stand)
    hit_or_stand = ''
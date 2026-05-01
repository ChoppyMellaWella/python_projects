# stuff i learned:
# - if not variable_name can help identify emtpy lists

import random

cards = [1,2,3,4,5,6,7,8,9,10,11]
user_cards = []
dealer_cards = []
keep_going = 'y'
decision = ""

def adding_cards(user_cards, dealer_cards):
    if not dealer_cards: # if nothing inside the list,
        dealer_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
    else:
        dealer_cards.append(random.choice(cards))
    if not user_cards:
        user_cards.append(random.choice(cards))
        user_cards.append(random.choice(cards))
    else:
        user_cards.append(random.choice(cards))

def compare(user_cards, dealer_cards):
    if sum(dealer_cards)-21 > sum(user_cards)-21:
        print('you lose')
    else:
        print('you win!')

def reveal_dealer_and_choose(user_cards, dealer_cards):
    print(f"One card of dealer's hand: {dealer_cards[1]}")
    print(f"dealer hand: {dealer_cards}") # only test. remove later
    print(f"your hand: {user_cards}")
    decision = input("hit [y] / stand [n]: ")
    if decision.lower().replace(" ", "") == 'y':
        user_cards.append(random.choice(cards))
    elif decision.lower().replace(" ", "") == 'n':
        compare(user_cards, dealer_cards)
        

while keep_going == 'y':
    adding_cards(user_cards, dealer_cards)
    reveal_dealer_and_choose(user_cards, dealer_cards)
    

    keep_going = input("keep going?: ")
    
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COINS = {
    'quarter': 0.25,
    'dime': 0.10,
    'nickel': 0.05,
    'penny': 0.01,
}

profit = 0
resources = {
    "water": 300,
    "milk": 200, 
    "coffee": 100, 
}

# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def ask_user():
    answer = input("What would you like? (espresso/latte/cappuccino): ")
    return answer.lower().replace(" ", "")

# TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
is_up = True
def turn_off():
    print('Shutting down...')
    return False

# TODO 3: Print report
def print_report(resources=resources, profit=profit):
    ## add money later
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${profit}")

# TODO 4: Check resources sufficient?
def check_resources(user_choice,resources=resources):
    # check if machine has sufficient resources for user's choice of drink
    good_counter = 0
    for ingredient in MENU[user_choice]['ingredients']:
        if resources[ingredient] >= MENU[user_choice]['ingredients'][ingredient]:
            good_counter += 1
    if good_counter == len(MENU[user_choice]['ingredients']):
        return True
    else: return False

# TODO 5: Process coins
def process_coins(COINS=COINS):
    total = 0
    for coin in COINS:
        amount_of_coin = float(input(f"Enter amount of {coin}s: "))
        total += float(amount_of_coin * COINS[coin])
    return total

# TODO 6: Check transaction successful?
def check_transaction(coin_total,user_choice,MENU=MENU):
    if MENU[user_choice]['cost'] < coin_total:
        print(f"Here is ${coin_total-MENU[user_choice]['cost']:.2f} in change.")
        return True
    elif MENU[user_choice]['cost'] == coin_total:
        return True
    else:
        print('Sorry that\'s not enough money. Money refunded.')
        return False

# TODO (Extra): process the transaction. add money to machine profit
def process_transaction(user_choice,MENU=MENU):
    return MENU[user_choice]['cost']

# TODO 7: Make Coffee
def make_coffee(user_choice, MENU=MENU, resources=resources):
    for ingredient in MENU[user_choice]['ingredients']:
        resources[ingredient] = resources[ingredient] - MENU[user_choice]['ingredients'][ingredient]

# TODO (Extra): Give Coffee
def give_coffee(user_choice):
    print(f"Here is your {user_choice} ☕️. Enjoy!")

while is_up:
    user_choice = ask_user()
    if user_choice == 'off':
        is_up = turn_off()
    elif user_choice == 'report':
        print_report(resources=resources, profit=profit)
    elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        if check_resources(user_choice):
            coin_total = process_coins() # returns float
            if check_transaction(coin_total, user_choice):
                profit += process_transaction(user_choice) # returns float
                make_coffee(user_choice)
                give_coffee(user_choice)
        else:
            print(f"Error: Unable to buy {user_choice}. Not enough resources")
    else:
        print(f"Error: '{user_choice}': Unknown item")
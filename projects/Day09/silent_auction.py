import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

name_to_bid = {}

answer = "y"

highest_bid = 0
highest_bidder = ""

while answer == 'y':
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    name_to_bid[name] = bid
    answer = input("Are there any more bidders?: ").lower().replace(" ","")
    if answer == 'y':
        name = None
        bid = None
        clear_console()

for name in name_to_bid:
    if highest_bid < name_to_bid[name]:
        highest_bid = name_to_bid[name]
        highest_bidder = name

print(f"The highest bidder is {highest_bidder} at ${highest_bid}")

# main idea: make password generator
# topology: duckblock -> symbols,letters,numbers -> manipulate guys randomly somehow -> print out password
"""

what did i learn?:
- reading docs 
- random.randint(a, b) -> return integer N where a <= N <= b
- random.shuffle() -> shuffle some sequence ie. list tuple set
- print("something", end="") -> replaces end of print with whatever end is assigned
"""

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['!','@','#','$','%','&','(',')','+','?','^','*','-','_','=','[',']','{','}',':',';',',','.','<','>','/','~']

print('Hello! This program will generate a random password for you')
num_letters = int(input('How many letters do you want in your password?: '))
num_numbers = int(input('How many numbers do you want in your password?: '))
num_symbols = int(input('How many symbols do you want in your password?: '))
og_num_letters = num_letters
og_num_numbers = num_numbers
og_num_symbols = num_symbols


# random order process: 
    # take l,n,s ; 
    # choose random number of times (rn) l or n or s is placed; save to variables
    # rn take away from number of times l,n,s printed and save to left_to_print or something like that
    # place l,n,s rn amnt of times; cycle through?
# random order topology: 
    # for loop
    # variables outside scope?
    # choose random index where 0 <= choice <= len(list)

rn_letters = 0
rn_numbers = 0
rn_symbols = 0

letters_check = True
numbers_check = True
symbols_check = True

successful_counter = 0
choice = None
keep_going = True
user_answer = ""

while keep_going:
    while successful_counter < 3:
        choice = random.randint(0,2)
        match choice:
            case 0:
                if letters_check:
                    rn_letters = random.randint(1,num_letters)
                    for i in range(rn_letters):
                        print(letters[random.randint(0, len(letters)-1)], end="")
                    num_letters -= rn_letters
                    if num_letters == 0:
                        successful_counter += 1
                        letters_check = False
                    rn_letters = 0
            case 1:
                if numbers_check:
                    rn_numbers = random.randint(1,num_numbers)
                    for i in range(rn_numbers):
                        print(numbers[random.randint(0, len(numbers)-1)], end="")
                    num_numbers -= rn_numbers
                    if num_numbers == 0:
                        successful_counter += 1
                        numbers_check = False
                    rn_numbers = 0
            case 2:
                if symbols_check:
                    rn_symbols = random.randint(1,num_symbols)
                    for i in range(rn_symbols):
                        print(symbols[random.randint(0, len(symbols)-1)], end="")
                    num_symbols -= rn_symbols
                    if num_symbols == 0:
                        successful_counter += 1
                        symbols_check = False
                    rn_symbols = 0
    user_answer = input("\nReroll/Change Values/Exit [(Enter)/c/n]: ").lower().replace(" ","")
    match user_answer:
        case "":
            keep_going = True
            letters_check = True
            numbers_check = True
            symbols_check = True
            num_letters = og_num_letters
            num_numbers = og_num_numbers
            num_symbols = og_num_symbols
            successful_counter = 0
        case 'c':
            num_letters = int(input('How many letters do you want in your password?: '))
            num_numbers = int(input('How many numbers do you want in your password?: '))
            num_symbols = int(input('How many symbols do you want in your password?: '))
            og_num_letters = num_letters
            og_num_numbers = num_numbers
            og_num_symbols = num_symbols
        case 'n':
            keep_going = False
        case _:
            print('ERROR: invalid input')
            keep_going = False
            break
# while num_letters > 0:
#     rn_letters = random.randint(1,num_letters)
#     for i in range(rn_letters):
#         print(letters[random.randint(0, num_letters)], end="")
#     num_letters -= rn_letters

    
# for i in range(rn_letters):
#     print(f"{i}", end="")


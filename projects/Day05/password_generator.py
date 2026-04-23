# main idea: make password generator
# topology: duckblock -> symbols,letters,numbers -> manipulate guys randomly somehow -> print out password
"""
what do i wanna try?:
- make the duckblock
what i did:
- made the interacts
what did i learn?:
- reading docs 
- random.randint(a, b) -> return integer N where a <= N <= b
"""

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['!','@','#','$','%','&','(',')','+','?']

print('Hello! This program will generate a random password for you')
num_letters = int(input('How many letters do you want in your password?: '))
num_numbers = int(input('How many numbers do you want in your password?: '))
num_symbols = int(input('How many symbols do you want in your password?: '))

# random order process: 
    # take l,n,s ; 
    # choose random number of times (rn) l or n or s is placed; save to variables
    # rn take away from number of times l,n,s printed and save to left_to_print or something like that
    # place l,n,s rn amnt of times; cycle through?
# random order topology: 
    # for loop
    # variables outside scope?

rn_letters = None
rn_numbers = None
rn_symbols = None

print(random.randint(0,9))
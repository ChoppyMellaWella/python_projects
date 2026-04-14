"""
time for exercises now

"""

# 1
print('thirty' + 'days' + 'of' + 'python') 

# 2 
print('coding' + 'for' + 'all')


# 3
company = "Coding For All"

# 4
print(company)

# 5
print(len(company))

# 6: uppercase everything 
print(company.upper())

# 7: lowercase everything
print(company.lower())

# 8: use capital() title() swapcase() to format value of string 'Coding For All'
print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company.lower())

# 9: cut(slice) out the first word of Coding For All string
print(company[7:])

# 10: Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find("Coding") != -1 ) # this is the method i used

# 11: replace 'Coding' with 'Python'
print(company.replace('Coding', 'Python'))

# 12: Change "Python for Everyone" to "Python for All" using the replace method or other methods.
change_this_string = 'Python for Everyone'
print(change_this_string.replace('Everyone', 'All')) # method 1

python_for = change_this_string[0:11] # method 2
print(python_for + 'All')

# 13: Split the string 'Coding For All' using space as the separator (split())
print(company.split())

# 14: "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

the_big_guys = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(the_big_guys.split(', ' ))

# 15: What is the character at index 0 in the string Coding For All.
print(company[0])

# 16: What is the last index of the string Coding For All.
print(company[-1]) # going backwards from 0

# 17: What character is at index 10 in "Coding For All" string.
print(company[10]) # ??
print(len(company)) # okay seems like a space

# 18: Create an acronym or an abbreviation for the name 'Python For Everyone'.
python_for_everyone = 'Python For Everyone'
print(python_for_everyone[0] + python_for_everyone[7] + python_for_everyone[11])

# 19: Create an acronym or an abbreviation for the name 'Coding For All'.
coding_for_all = 'Coding For All'
it_be_split = coding_for_all.split()
print((it_be_split[0])[0] + (it_be_split[1])[0] + it_be_split[2][0])

# 20: Use index to determine the position of the first occurrence of C in Coding For All.
print(coding_for_all.index('C'))

# 21: Use index to determine the position of the first occurrence of F in Coding For All.
print(coding_for_all.index('F'))

# 22: Use rfind to determine the position of the last occurrence of l in Coding For All People.
all_people = 'Coding For All People'
print(all_people.rfind('l'))

# 23: Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence_1 = 'You cannot end a sentence with because because because is a conjunction'
print(sentence_1.find('because'))
print(sentence_1.index('because')) # essentially either of these give the same output in the end

# 24: Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence_1.rindex('because'))

# 25: Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# okay i understand the point of this, we used both index and rindex to find the beginning and end of phrase and then slice it out with either substring 
print(sentence_1.replace('because because because ', ''))
print(sentence_1[0:31] + sentence_1[55:(len(sentence_1))])

# 26: Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence_1.find('because'))

# 27: Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# same as question 25

# 28: Does 'Coding For All' start with a substring Coding?
print(coding_for_all.startswith('Coding'))

# 29: Does 'Coding For All' end with a substring coding?
print(coding_for_all.endswith('coding'))

# 30: '   Coding For All      '  , remove the left and right trailing spaces in the given string.
space = '   Coding For All      '
print(space.replace(" ", ""))

# 31: Which one of the following variables return True when we use the method isidentifier():
#
#    30DaysOfPython
#    thirty_days_of_python
#
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 32: The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
stuff = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(stuff)) # interesting- ' ' is the delimiter. so basically delimits based off of what string is after being passed a list 

"""
33: Use the new line escape sequence to separate the following sentences.

I am enjoying this challenge.
I just wonder what is next.

"""
print()
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34: Use a tab escape sequence to write the following lines. 
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

"""
35:     Use the string formatting method to display the following:

radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.

"""

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with a radius of {radius} is {area} meters square")

"""

36: Make the following using string formatting methods:

8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144

"""

num1 = 8
num2 = 6

print('Hello. I\'m going to play around with numbers %d and %d' %(num1, num2))
print('Hello. I\'m going to play around with numbers {} and {}'.format(num1, num2))
print(f"Hello. I\'m going to play around with numbers {num1} and {num2}\n")

# old formatting
print('%d + %d = %d' %(num1, num2, num1+num2))
print('%d - %d = %d' %(num1, num2, num1-num2))
print('%d * %d = %d' %(num1, num2, num1*num2))
print('%d / %d = %f' %(num1, num2, num1/num2))
print(f"{num1} % {num2} = {num1%num2}")
print('%d // %d = %d' %(num1, num2, num1//num2))
print('%d ** %d = %d\n' %(num1, num2, num1**num2))

# newer formatting
print('{} + {} = {}'.format(num1, num2, num1+num2))
print('{} - {} = {}'.format(num1, num2, num1-num2))
print('{} * {} = {}'.format(num1, num2, num1*num2))
print('{} / {} = {}'.format(num1,num2,num1/num2))
print("{} % {} = {}".format(num1,num2,num1%num2))
print('{} // {} = {}'.format(num1,num2,num1//num2))
print('{} ** {} = {}'.format(num1,num2,num1**num2))

# the rest with print fs

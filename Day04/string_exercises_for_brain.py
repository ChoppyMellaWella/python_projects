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



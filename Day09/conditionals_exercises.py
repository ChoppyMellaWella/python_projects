"""

Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.

"""

user_age = int(input('Enter your age: '))
if user_age <= 18:    
    print(f'you need {18-user_age} more year(s) to go until you can drive, bud.')
else:
    print('You are old enough to drive')

"""

Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me.

"""
my_age = 40
your_age = int(input('How old are you?: '))

if your_age < my_age:
    print(f'you are {my_age-your_age} year(s) younger than i am')
elif your_age > my_age:
    print(f'you are {your_age-my_age} year(s) older than i am')
else:
    print('we are the same age')


"""

    Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3

"""

a=int(input('input value of A: '))
b=int(input('input value of B: '))
if a < b:
    print(f'{a} is less than {b}')
elif a > b:
    print(f'{a} is greater than {b}')
else:
    print(f'{a} and {b} are equal')

"""

    Write a code which gives grade to students according to theirs scores:

```sh
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
```

"""

user_grade = int(input('what was your grade for one class: '))

match user_grade:
    case user_grade if user_grade >= 90 and user_grade <= 100:
        print('you have an A in that class')
    case user_grade if user_grade >= 80 and user_grade <= 89:
        print('you have a B in that class')
    case user_grade if user_grade >= 70 and user_grade <= 79:
        print('you have a C in that class')
    case user_grade if user_grade >= 60 and user_grade <= 69:
        print('you have a D in that class')
    case user_grade if user_grade >= 0 and user_grade <= 59:
        print('you have an F in that class')
    case _:
        print('invalid grade option')


"""
Get the month from user input then check if the season is Autumn, Winter, 
Spring or Summer. If the user input is: September, October or November, the season is 
Autumn. December, January or February, the season is Winter. March, April or May, 
the season is Spring June, July or August, the season is Summer
"""

user_month = input('what is your favorite month?: ').lower().replace(" ", "")

match user_month:
    case user_month if user_month.find('september') != -1 or user_month.find('october') != -1 or user_month.find('november') != -1:
        print('the season is autumn')
    case user_month if user_month.find('december') != -1 or user_month.find('january') != -1 or user_month.find('february') != -1:
        print('the season is winter')
    case user_month if user_month.find('march') != -1 or user_month.find('april') != -1 or user_month.find('may') != -1:
        print('the season is spring')
    case user_month if user_month.find('june') != -1 or user_month.find('july') != -1 or user_month.find('august') != -1:
        print('the season is summer')
    case _:
        print('type the correct month')

"""
    The following list contains some fruits:

```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

"""

fruits = ['banana', 'orange', 'mango', 'lemon']

print(fruits)

user_fruit = input('whats a fruit that you want added to our list?: ').lower().replace(" ", "")

if user_fruit in fruits:
    print(f'try again, there already is {user_fruit} in there')
else:
    fruits.append(user_fruit)
    print(fruits)

"""
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, 
   Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, 
   Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 
 * If the person is married and if he lives in Finland, print the information in the following format:

"""

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
    }

if person['skills']:
    print(person['skills'][(len(person['skills']))//2])
if 'Python' in person['skills']:
    print('this person has Python skills')


if 'MongoDB' and 'Node' and 'React' in person['skills']:
    print('He is a full stack developer')
elif 'JavaScript' and 'React' in person['skills']:
    print('He is a front end dev')
elif 'Node' and 'Python' and 'MongoDB' in person['skills']:
    print('He is a backend dev')
else:
    print('please put appropriate values in skills list')
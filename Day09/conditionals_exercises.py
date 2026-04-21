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



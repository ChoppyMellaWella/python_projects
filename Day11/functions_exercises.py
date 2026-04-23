# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1,num2):
    return num1+num2
print(add_two_numbers(2,2)) # should return 4

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that 
# calculates area_of_circle.
def area_of_circle(r):
    pi = 3.14159
    area = pi * r**2
    return area
print(f"{area_of_circle(5)}^2")

# 3. Write a function called add_all_nums which takes arbitrary number of arguments 
# and sums all the arguments. Check if all the list items are number types. If not do 
# give a reasonable feedback.
def add_all_nums(*args):
    sum = 0
    for i in args:
        if type(i) == type(0):
            sum += i
        else:
            print('ERROR: integer expected')
            print('Printing sum before unexpected character: ', end="")
            break
    return sum

print(add_all_nums(1,2,3,4,5,6,'F'))

# 4. Temperature in °C can be converted to °F using this formula: 
# °F = (°C x 9/5) + 32. Write a function which converts °C to °F, 
# convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit
print(f"{convert_celsius_to_fahrenheit(89.2)} degrees fahrenheit")

# 5. Write a function called check-season, it takes a month 
# parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    match month:
        case month if month.find('september') != -1 or month.find('october') != -1 or month.find('november') != -1:
            print('the season is autumn')
        case month if month.find('december') != -1 or month.find('january') != -1 or month.find('february') != -1:
            print('the season is winter')
        case month if month.find('march') != -1 or month.find('april') != -1 or month.find('may') != -1:
            print('the season is spring')
        case month if month.find('june') != -1 or month.find('july') != -1 or month.find('august') != -1:
            print('the season is summer')
        case _:
            print('type the correct month')
check_season('june')

# 6. Write a function called calculate_slope 
# which return the slope of a linear equation

# y2 - y1 / x2 - x1
# given points (x1,y1) (x2,y2)
def calculate_slope(x1,y1,x2,y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(f"slope is: {calculate_slope(3,4,5,7)}")

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic 
# equation, solve_quadratic_eqn.

# using the quadratic formula
def solve_quadratic_eqn(a,b,c):
    solution1 = (-b + ((b**2)-(4*a*c))**0.5)/(2*a)
    solution2 = (-b - ((b**2)-(4*a*c))**0.5)/(2*a)
    return solution1,solution2
print(solve_quadratic_eqn(5,2,3))

# 8. Declare a function named print_list. It takes a list as a 
# parameter and it prints out each element of the list.
example_list = ['apple','banana','kiwi','strawberry','mango','orange','pear','cherry']
def print_list(lst):
    for item in lst:
        print(item)
print_list(example_list)

# 9. Declare a function named reverse_list. It takes an array as 
# a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
    new_list = []
    for i in range((len(lst)-1),-1,-1):
        new_list.append(lst[i])
    return new_list
print(f"before: {example_list}")
print(f"after: {reverse_list(example_list)}")

# 10. Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a 
# capitalized list of items
def capitalize_list_items(lst):
    capital_list = []
    for item in lst:
        capital_list.append(item.upper())
    return capital_list
print(capitalize_list_items(example_list))

# 11. Declare a function named add_item. It takes a 
# list and an item parameters. It returns a list 
# with the item added at the end.
def add_item(lst, item):
    new_list = lst
    new_list.append(item)
    return new_list
print(add_item(example_list,'BROOOO'))

"""
12. 
    Declare a function named remove_item. It takes a list and an item parameters. 
    It returns a list with the item removed from it.

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
"""
def remove_item(lst, item):
    new_list = lst
    new_list.remove(item)
    return new_list

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

"""
13. 
    Declare a function named sum_of_numbers. It takes a 
    number parameter and it adds all the numbers in that range.

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
"""
def sum_of_numbers(n):
    sum = 0
    for i in range(0,n+1,1):
        sum += i
    return sum
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# 14. Declare a function named sum_of_odds. It 
# takes a number parameter and it adds all the 
# odd numbers in that range.
def sum_of_odds(n):
    sum = 0
    for i in range(n):
        if i%2 == 1:
            sum += i
    return sum

print(sum_of_odds(5)) 
print(sum_of_odds(10))
print(sum_of_odds(100))

# 15. Declare a function named sum_of_even. It takes a 
# number parameter and it adds all the even numbers in 
# that - range.
def sum_of_even(n):
    sum = 0
    for i in range(0,n+2,2):
        sum += i 
    return sum

print(sum_of_even(5)) 
print(sum_of_even(10))
print(sum_of_even(100))

# Exercises: LEVEL 2

"""
1. 
    Declare a function named evens_and_odds . It takes 
    a positive integer as parameter and it counts number 
    of evens and odds in the number.

    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
"""
def evens_and_odds(n): # postitive integer n
    odds = 0
    evens = 0
    for i in range(n):
        if i%2 == 1:
            odds += 1
    for i in range(0,n+2,2):
        evens += 1
    return odds, evens

print(evens_and_odds(100))
# The number of odds are 50.
# The number of evens are 51.

# 2. Call your function factorial, it takes a whole number 
# as a parameter and it return a factorial of the number
def factorial(n):
    fctl = 1
    for i in range(1,n+1):
        fctl *= i
    return fctl
print(factorial(10))
print(factorial(15))

# 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(emptiness='Function is empty'):
    if emptiness != 'Function is empty':
        return "There is something here"
    return emptiness

print(is_empty('java sucks, c+ sucks'))

# 4. Write different functions which take lists. They should calculate_mean, 
# calculate_median, calculate_mode, calculate_range, calculate_variance, 
# calculate_std (standard deviation).
random_nums = [3,10,9,2,1,6,5,8,7,4]
random_nums.sort()
def calculate_mean(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum/len(lst)
def calculate_median(lst):
    return lst[(len(lst))//2]
def calculate_mode(lst):
    # 1. keep track of how many times we see certain number - dictionary
    # 2. check within that list; get the number first store into our storage and increment times we see it afterwards - forloop
    # 3. get the highest # count of the all the numbers - check the dictionary
    # 4. return the number with the most amount of appearences - return

    tracker = {}

    for n in lst:
        if n in tracker:
            tracker[n] += 1
        else:
            tracker[n] = 1
    
    max_count = max(tracker.values()) 

    for num, count in tracker.items():
        if count == max_count:
            return num

def calculate_range(lst):
    pass
def calculate_variance(lst):
    pass
def calculate_std(lst):
    pass

print(calculate_mean(random_nums))
print(calculate_median(random_nums))
print(calculate_mode(random_nums))
print(calculate_range(random_nums))
print(calculate_variance(random_nums))
print(calculate_std(random_nums))


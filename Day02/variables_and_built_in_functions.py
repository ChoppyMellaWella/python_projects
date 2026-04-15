"""

python file and contents following exercises for day 2

"""
first_name = 'gabuki'
last_name = 'yayay'
full_name = 'gabuki yayay'
country = 'japan'
city = 'niigata city'
age = 19
year = 2000
is_maried = True
is_true = False
is_light_on = True

ip, gateway, hostname, make = '192.168.20.246', '192.168.20.128', 'gabuki', 'linux'

print(len(first_name)) # num
print(len(last_name)) # num
print(f"length of first name {len(first_name)}\nlength of last name {len(last_name)}")
print(type(age)) # int
print(type(is_maried)) # bool

num_one, num_two = 5,4

total = num_one + num_two

print(total) # 9

diff = num_two - num_one

print(diff) # -1

product = num_one * num_two

print(product) # 20

remainder = num_two % num_one

print(remainder) # 1

exp = num_one ** num_two

print(exp) # 625

# floor division is just division but rounding to the nearest integer
floor_division = num_one // num_two

print(floor_division) # 1

# Radius of a circle is 30 meters
area_of_circle = 3.14159 * 30**2

circumference_of_circle = 2 * 3.14159 * 30

print(area_of_circle, circumference_of_circle)


print('lets get stuff from you')

user_first_name = input('What is your first name?: ')
user_last_name = input('What is your last name?: ')
user_country = input('What country are you from?: ')
user_age = int(input('What is your age?: '))

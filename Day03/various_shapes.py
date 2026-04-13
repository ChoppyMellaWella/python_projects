"""

various shapes and doing fun stuff with those shapes

"""

print('rectangle')

rec_length = int(input('what is the length of the rectangle?: '))

rec_width = int(input('what is the width of the rectangle?: '))

rec_area = rec_length * rec_width
rec_perimeter = (rec_length + rec_width) * 2

print('rectangle area: ', rec_area, 'rectanagle perimeter: ', rec_perimeter)

print('circle')

cir_radius = float(input('what is radius of circle?: '))
pi = 3.14159

cir_area = pi * (cir_radius**2) 
cir_perimeter = 2 * cir_radius * pi

print('circle area: ', cir_area, 'circle perimeter: ', cir_perimeter)

print('slope/euclidian distance')

def euclidian_distance(p1, p2):
    diff1 = p1[1] - p1[0]
    diff2 = p2[1] - p2[0]
    sum = diff1**2 + diff2**2
    total = sum** 0.5
    return total

p1 = [2,2]
p2 = [6,10]
 
# euclidian_distance

print(euclidian_distance(p1,p2))

print('find output value')

user_x = int(input('what is x going to be?: '))

y_function = user_x**2 + 6 * user_x + 9

print(y_function)

print('logic/boolean logic')

print(f"length of \'python\' is {len("python")} and length of \'dragon\' is {len("dragon")}")

python_length = len('python')
dragon_length = len('dragon')

print("character length of dragon and python are not the same: ", python_length != dragon_length)

complex = 1 + 2j

print('on' in 'python' and 'on' in 'dragon')

print('jargon' in 'i hope this course is not full of jargon')

print('on' not in 'dragon' and 'on' not in 'python')

print(str(float(len('python'))))

print('finding even or odd numbers')

num1 = 67
num2 = 42

print(f'67 mod 2 is {num1%2}, so 67 odd number')
print(f'42 mod 2 {num2%2} so 42 is even')

print(7//3 == 2.7)

print(type('10') == type(10))

print(int(9.8) == 10)

def calculate(first_number, operator, second_number):
    """ Calculates with user's first number, second number, and operator"""
    match operator:
        case '+':
            return first_number + second_number
        case '-':
            return first_number - second_number
        case '*':
            return first_number * second_number
        case '/':
            return first_number / second_number
        case _:
            return "invalid operator"

answer = 'y'

result = None

while answer.lower().replace(" ","") == 'y':
    
    if result == None:
        result = calculate(int(input("What is the first number: ")), input("What is the operator: "), int(input("What is the second number?: ")))
    else:
        result = calculate(result, input("What is the operator: "), int(input("What is the second number?: ")))
    print(result)  
    answer = input("Do you wish to continue the operation with your result? Type 'y' or 'n': ")
    if answer.lower().replace(" ", "") == 'koyuki':
        print("Hey- that's my gf- and I love her!")

    

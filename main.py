a = int(input('Enter the first number'))
b = int(input('Enter the second number'))
sign = input('+,-,*,/,**,// ')

def calculator(number1,number2,action):
    if action == '+':
        addition = number1 + number2
        return addition

    if action == '-':
        subtraction = number1 - number2
        return subtraction

    if action == '*':
        multiplication = number1 * number2
        return multiplication

    if action == '/':
        division = number1 / number2
        return division

    if action == '**':
        exponentiation = number1 ** number2
        return exponentiation

    if action == '//':
        division_full = number1 // number2
        return division_full



print(calculator(a,b,sign))
from art import logo
# from replit import clear

print(logo)


def add(n1, n2):
    return (n1 + n2)


def sub(n1, n2):
    return (n1 - n2)


def multiply(n1, n2):
    return (n1 * n2)


def devide(n1, n2):
    return (n1 / n2)


operations = {'+': add, '-': sub, '*': multiply, '/': devide}


def calculator():
    num1 = float(input("What's your first number? "))
    calculation_end = False
    while not calculation_end:
        for symbol in operations:
            print(symbol)
        operation_symbol = input('Pick an operation from the line above: ')
        num2 = float(input("What's your next number? "))
        calculation_function = operations[operation_symbol]
        answer = round(calculation_function(num1, num2), 2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')
        continue_calculation = input(
            'Type y if you want to use the answer else type n to start a new calculation, and type exit to exit the calculation: ')
        if continue_calculation == 'y':
            num1 = answer
            # clear()
        elif continue_calculation == 'n':
            calculator()
        elif continue_calculation == 'exit':
            calculation_end = True


calculator()


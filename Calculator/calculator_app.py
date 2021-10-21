from art import logo
# Calculator

# Add


def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(logo)


def calculator():
    """[summary]
    Do basic math functions with the ability to chain math functions on the previous result
    """
    num1 = float(input("What is the first number?: "))
    for operation in operations.keys():
        print(operation)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What is the second number?: "))
    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    contin = True

    while contin:
        contin_calculations = input(
            f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation, or type 'e' to exit: ")
        if contin_calculations == "y":
            operation_symbol = input("Pick an another operation: ")
            num3 = float(input("What is the second number?: "))
            calculation_function = operations[operation_symbol]
            second_answer = calculation_function(first_answer, num3)
            print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
        elif contin_calculations == "n":
            contin = False
            calculator()
        else:
            contin = False


calculator()

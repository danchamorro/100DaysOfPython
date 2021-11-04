from art import logo
print(logo)


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


def calculator():
   # Do basic math functions with the ability to chain math functions on the previous result
    while True:
        try:
            # Get user input
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
            # Disply the operations
            for operation in operations.keys():
                print(operation)
            # Get user input
            op = input("Pick an operation from the line above: ")

            # Check if operation is valid
            if op not in operations:
                print("Invalid operation")
                continue

            # Calculate result
            result = operations[op](n1, n2)
            print(result)

        except ValueError:
            print("Invalid input")
            continue

        # Ask if user wants to continue
        cont = input("Continue? (y/n): ")
        if cont.lower() == "n":
            print("Bye!")
            break


calculator()

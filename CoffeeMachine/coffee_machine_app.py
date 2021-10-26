MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Process coins.
COINS = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "penny": 0.01,
}


# TODO1: Machine makes 3 flavors
# TODO2: Machine is coin operated
# TODO3: Print a report that shows how many resources are left in the machine.
# TODO4: Check if the resources are sufficient enough to make the coffee.
# TODO5: Machine take coins as a payment. Check if coins provided are enough for the coffee.
# TODO6: Make the coffee and deduct the resources.

# Show prices of each coffee.


def cost():
    """Show prices of each coffee"""
    for k, v in MENU.items():
        print("{}, cost: ${}".format(k.title(), v["cost"]))


# Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
choice = input("What would you like? (espresso/latte/cappuccino): ")


# Turn off the Coffee Machine by entering “off” to the prompt.


# Print report.
def report():
    for k, v in resources.items():
        print("{}: {}ml".format(k.title(), v))

# Check resources sufficient?


# Check transaction successful?


# Make Coffee.


# Machines bank
machine_bank = 0

# User coins
user_coins = 0.0

# Ask how many of each coin.
quarter = float(input("How many quarters?: "))
dime = float(input("How many dimes?: "))
nickle = float(input("How many nickles?: "))
penny = float(input("How many pennies?: "))

# Get money from user.


def user_money(quarter=0, dime=0, nickle=0, penny=0):
    global user_coins
    q = COINS["quarter"] * quarter
    d = COINS["dime"] * dime
    n = COINS["nickle"] * nickle
    p = COINS["penny"] * penny
    for coin in q, d, n, p:
        user_coins += coin


user_money(quarter, dime, nickle, penny)

print(user_coins)

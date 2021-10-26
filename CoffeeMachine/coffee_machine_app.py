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


cont = True


# Show prices of each coffee.
def cost():
    """Show prices of each coffee"""
    for k, v in MENU.items():
        print("{}, cost: ${}".format(k.title(), v["cost"]))


# Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
user_choice = input(
    "What would you like? (espresso/latte/cappuccino): ").lower()
if user_choice == "report":
    pass

# Turn off the Coffee Machine by entering “off” to the prompt.
if user_choice == "off":
    pass

# Print report.


def report():
    """Generate report of remaining resources"""
    for k, v in resources.items():
        print("{}: {}ml".format(k.title(), v))

# Check transaction successful?

# Make Coffee.


# Machines bank.
machine_bank = 0

# User coins.
user_coins = 0.0


# Ask how many of each coin.
#! This is working
quarter = float(input("How many quarters?: "))
dime = float(input("How many dimes?: "))
nickle = float(input("How many nickles?: "))
penny = float(input("How many pennies?: "))


# Get money from user.
#! This is working
def user_money(quarter=0, dime=0, nickle=0, penny=0):
    """Calculate the total amount of coins by user"""
    global user_coins
    q = COINS["quarter"] * quarter
    d = COINS["dime"] * dime
    n = COINS["nickle"] * nickle
    p = COINS["penny"] * penny
    for coin in q, d, n, p:
        user_coins += coin
    return user_coins


# Machines money.
def machine_money():
    global machine_bank
    machine_bank += user_money()


user_money(quarter, dime, nickle, penny)

print(user_coins)

machine_money()
print(machine_bank)


# Check resources sufficient.
def check_resources(coffee):
    """Check if machine has enough resources for coffee"""
    coffee = MENU[coffee]["ingredients"]
    if coffee["water"] > resources["water"] and resources["water"] <= 0:
        print("Not enough water")
        if coffee["milk"] > resources["milk"] and resources["milk"] <= 0:
            print("Not enough milk")
            if coffee["coffee"] > resources["coffee"] and resources["coffee"] <= 0:
                print("Not enough coffee")


# check_cost(user_choice)

check_resources(user_choice)

# Compare if user coins can make a purchase


# def check_cost(user_choice):
#     coffee = MENU["latte"]["ingredients"]
#     if user_choice == "latte":
#         if user_money() >= MENU["latte"]["cost"]:
#             print("Here is your latte")
#             if user_money() > MENU["latte"]["cost"]:
#                 change = user_money() - MENU["latte"]["cost"]
#                 print("Here is ${} in change.".format(change))
#     elif user_choice == "espresso":
#         if user_money() >= MENU["espresso"]["cost"]:
#             print("Here is your espresso")
#             if user_money() > MENU["espresso"]["cost"]:
#                 change = user_money() - MENU["espresso"]["cost"]
#                 print("Here is ${} in change.".format(change))
#     elif user_choice == "cappuccino":
#         if user_money() >= MENU["cappuccino"]["cost"]:
#             print("Here is your cappuccino")
#             if user_money() > MENU["cappuccino"]["cost"]:
#                 change = user_money() - MENU["cappuccino"]["cost"]
#                 print("Here is ${} in change.".format(change))

#     resources["water"] = resources["water"] - coffee["water"]
#     resources["milk"] = resources["milk"] - coffee["milk"]
#     resources["coffee"] = resources["coffee"] - coffee["coffee"]

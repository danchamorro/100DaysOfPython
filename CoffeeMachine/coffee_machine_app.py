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


def main():
    cont = True
    while cont:
        # Print report.
        def report():
            """Generate report of remaining resources"""
            for k, v in resources.items():
                print("{}: {}ml".format(k.title(), v))

        # Turn off machine ie: exit program.
        def turn_off():
            """Exit the program"""
            cont = False
            return cont

        # Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
        user_choice = ""
        while user_choice not in MENU.keys():
            user_choice = input(
                "What would you like? (espresso/latte/cappuccino): ").lower()
        # Show a report of current resources.
            if user_choice == "report":
                print(report())
        # Turn off the Coffee Machine by entering “off” to the prompt.
            if user_choice == "off":
                return turn_off()

        print("Please insert coins.")

        # Ask how many of each coin.
        #! This is working.
        while True:
            try:
                quarter = float(input("How many quarters?: "))
                dime = float(input("How many dimes?: "))
                nickle = float(input("How many nickles?: "))
                penny = float(input("How many pennies?: "))
            except ValueError:
                print("Sorry, I didn't understand that. Please type a number.")
                continue
            else:
                break

        # Get money from user.
        #! This is working.
        def user_money(quarter=0, dime=0, nickle=0, penny=0):
            """Calculate the total amount of coins by user"""
            user_coins = 0
            quarter = COINS["quarter"] * quarter
            dime = COINS["dime"] * dime
            nickle = COINS["nickle"] * nickle
            penny = COINS["penny"] * penny
            for coin in quarter, dime, nickle, penny:
                user_coins += coin
            return round(user_coins, 2)

        # Check resources.
        #! This is working.
        def check_resources(user_choice):
            """Check if machine has enough resources for coffee"""
            user_choice = MENU[user_choice]["ingredients"]
            if resources["water"] >= user_choice["water"]:
                return True
            elif resources["milk"] >= user_choice["milk"]:
                return True
            elif resources["coffee"] >= user_choice["coffee"]:
                return True
            else:
                return False

        # Make Coffee.
        #! This is working.
        def make_coffee(user_choice):
            """Make the coffee"""
            coffee = MENU[user_choice]["ingredients"]
            if user_choice == "latte":
                resources["water"] = resources["water"] - coffee["water"]
                resources["milk"] = resources["milk"] - coffee["milk"]
                resources["coffee"] = resources["coffee"] - coffee["coffee"]
            elif user_choice == "cappuccino":
                resources["water"] = resources["water"] - coffee["water"]
                resources["milk"] = resources["milk"] - coffee["milk"]
                resources["coffee"] = resources["coffee"] - coffee["coffee"]
            elif user_choice == "espresso":
                resources["water"] = resources["water"] - coffee["water"]
                resources["coffee"] = resources["coffee"] - coffee["coffee"]

        # Refund money.
        #! This is working.
        def refund(change):
            """Refund any over payment"""
            change = user_money(quarter, dime, nickle, penny) - \
                MENU[user_choice]["cost"]
            return round(change, 2)

        if user_choice == "latte" and user_money(quarter, dime, nickle, penny) >= MENU[user_choice]["cost"] and check_resources(user_choice):
            make_coffee(user_choice)
            print("Enjoy your: {}".format(user_choice))
            if user_money(quarter, dime, nickle, penny) > MENU[user_choice]["cost"]:
                print("You have a refund of: ${}".format(refund(user_money)))
        elif user_choice == "cappuccino" and user_money(quarter, dime, nickle, penny) >= MENU[user_choice]["cost"] and check_resources(user_choice):
            make_coffee(user_choice)
            print("Enjoy your: {}".format(user_choice))
            if user_money(quarter, dime, nickle, penny) > MENU[user_choice]["cost"]:
                print("You have a refund of: ${}".format(refund(user_money)))
        elif user_choice == "espresso" and user_money(quarter, dime, nickle, penny) >= MENU[user_choice]["cost"] and check_resources(user_choice):
            make_coffee(user_choice)
            print("Enjoy your: {}".format(user_choice))
            if user_money(quarter, dime, nickle, penny) > MENU[user_choice]["cost"]:
                print("You have a refund of: ${}".format(refund(user_money)))
        else:
            print("Sorry that's not enough money. Money refunded.")

        # Machines money.
        #! This is working.
        def machine_money(machine_bank):
            """Returns the amount of money the machine has collected"""
            machine_bank = user_money(quarter, dime, nickle, penny)
            return round(machine_bank, 2)


main()

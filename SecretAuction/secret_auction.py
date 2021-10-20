import os
from art import logo


def clearConsole():  # Clear the console so the next bidder doesn't see the previous bit.
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


print("Welcome to the secret auction program.")

auction = [
    {
        "name": "name",
        "bid": 0
    },
]

print(logo)


def auction_game():
    other_bidders = True
    highest_bid = 0
    highest_bidder = ""

    while other_bidders:
        name = input("What is your name? ")
        bid = int(input("What is your bid? "))

        new_bids = {
            "name": name,
            "bid": bid,
        }

        auction.append(new_bids)
        contin = input("Are there other bidders? Type 'yes' or 'no'. \n")
        if contin == "yes":
            clearConsole()
            continue
        elif contin == "no":
            other_bidders = False
            clearConsole()
    for num in auction:
        if num["bid"] > highest_bid:
            highest_bid = num["bid"]
            highest_bidder = num["name"]
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")


auction_game()

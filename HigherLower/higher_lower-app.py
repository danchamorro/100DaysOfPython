"""
//TODO1: Choose two random element from list of dictionaries in game_data.py
//TODO2: Compare both elements based on how many followers they have. 
//TODO3: User will guess who they think have the most followers. If correct the move on to a new random set of choices or loose.  
//TODO4: Implement game art. 
"""

import random
from game_data import data
from art import logo, vs
import os


def clearConsole():  # Clear the console so the next bidder doesn't see the previous bit.
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# for name in data:
#     print(name["name"])


# Get random element
def rand_select():
    """Randomly select a person or entity from the game data list

    Returns:
        Dictionary
    """
    influencer = random.choice(data)
    return influencer


score = 0


def high_low():
    """
    Choose a entity or person you think has more followers
    """
    score = 0
    correct = True
    while correct:
        print(logo)
        rand_a = rand_select()
        rand_b = rand_select()
        print(
            f"Compare A: {rand_a['name']}, a {rand_a['description']}, from {rand_a['country']}.")
        print(vs)
        print(
            f"Compare B: {rand_b['name']}, a {rand_b['description']}, from {rand_b['country']}.")
        # User guess
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        clearConsole()

        if user_guess == "a":
            if rand_a["follower_count"] > rand_b["follower_count"]:
                score += 1
                continue
            else:
                print(f"That was wrong. Your final score was: {score}")
                break
        elif user_guess == "b":
            if rand_b["follower_count"] > rand_a["follower_count"]:
                score += 1
                continue
            else:
                print(f"That was wrong. Your final score was: {score}")
                break


high_low()

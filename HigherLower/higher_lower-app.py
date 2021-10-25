"""
//TODO1: Choose two random element from list of dictionaries in game_data.py
TODO2: Compare both elements based on how many followers they have. 
TODO3: User will guess who they think have the most followers. If correct the move on to a new random set of choices or loose.  
TODO4: Implement game art. 
"""

import random
from game_data import data

# for name in data:
#     print(name["name"])


# User guess
# user_guess = input("Who has more followers? Type 'A' or 'B': ")

# Get random element
def rand_select():
    influencer = random.choice(data)
    return influencer


contin = True

# while contin:
rand_a = rand_select()
rand_b = rand_select()
print(
    f"Compare A: {rand_a['name']}, a {rand_a['description']}, from {rand_a['country']}.")
print(
    f"Compare B: {rand_b['name']}, a {rand_b['description']}, from {rand_b['country']}.")

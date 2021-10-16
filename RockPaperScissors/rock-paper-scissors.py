import random
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print('Welcome to Rock, Paper, Scissors.')

rpc = ["Rock", "Paper", "Scissors"]
rpc_image = [rock, paper, scissors]
user_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
cpu_choice = random.randint(0, len(rpc)-1)


if user_choice == 0 and cpu_choice == 2:
    print(rpc_image[user_choice])
    print("The Computer Chose: \n", rpc_image[cpu_choice])
    print(f"You choose: {rpc[user_choice]}. You win!")
elif user_choice == 2 and cpu_choice == 1:
    print(rpc_image[user_choice])
    print("The Computer Chose: \n", rpc_image[cpu_choice])
    print(f"You choose: {rpc[user_choice]}. You win!")
elif user_choice == 1 and cpu_choice == 0:
    print(rpc_image[user_choice])
    print("The Computer Chose: \n", rpc_image[cpu_choice])
    print(f"You choose: {rpc[user_choice]}. You win!")
elif user_choice == cpu_choice:
    print(rpc_image[user_choice])
    print("The Computer Chose: \n", rpc_image[cpu_choice])
    print("Its a tie")
else:
    print(rpc_image[user_choice])
    print("The Computer Chose: \n", rpc_image[cpu_choice])
    print("You lost!")

import random

# Rock
rpcimage = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
            """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
            """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

print('Welcome to Rock, Paper, Scissors.')

rpc = ["Rock", "Paper", "Scissors"]
user_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
cpu_choice = random.choice(rpc)
cpu_image_index = cpu_choice.index(cpu_choice)


if rpc[user_choice] == "Rock" and cpu_choice == "Scissors":
    print(rpc[user_choice], cpu_choice)
    print(f"You choose: {rpc[user_choice]}. You win!")
elif rpc[user_choice] == "Scissors" and cpu_choice == "Paper":
    print(rpc[user_choice], cpu_choice)
    print(f"You choose: {rpc[user_choice]}. You win!")
elif rpc[user_choice] == "Paper" and cpu_choice == "Rock":
    print(rpc[user_choice], cpu_choice)
    print(f"You choose: {rpc[user_choice]}. You win!")
elif rpc[user_choice] == cpu_choice:
    print(rpc[user_choice], cpu_choice)
    print("Its a tie")
else:
    print(rpc[user_choice], cpu_choice)
    print("You lost!")

# Guessing Game
import random
from art import logo

numbers = list(range(1, 101))


cpu_pick = random.choice(numbers)

print(logo)
level = input("Choose a difficulty. Type 'easy' or 'hard': ")


def easy_level():  # Guess game base on easy level

    easy = 10
    while easy != 0:
        print("You have {} attempts to guess the number".format(easy))
        try:
            user_guess = int(input("Make a guess: "))
        except:
            user_guess = 0
            print("🚨 🚨 You must type a valid number, you loose a turn. 🚨🚨")

        if user_guess != cpu_pick:
            easy = easy - 1
            print("Guess again. ")
            if user_guess > cpu_pick:
                print("Too high.")
            else:
                print("Too low.")
        elif user_guess == cpu_pick:
            print("You guessed it!")
            break
        if easy == 0:
            print("You ran out fo guesses. Try again.")


def hard_level():  # Guess game base on hard level

    hard = 5
    while hard != 0:
        print("You have {} attempts to guess the number".format(hard))
        try:
            user_guess = int(input("Make a guess: "))
        except:
            user_guess = 0
            print("🚨 🚨 You must type a valid number, you loose a turn. 🚨🚨")

        if user_guess != cpu_pick:
            hard = hard - 1
            print("Guess again. ")
            if user_guess > cpu_pick:
                print("Too high.")
            else:
                print("Too low.")
        elif user_guess == cpu_pick:
            print("You guessed it!")
            break
        if hard == 0:
            print(
                f"You ran out of guesses. The computer picked {cpu_pick}. Try again.")


if level == "easy":
    easy_level()
elif level == "hard":
    hard_level()
else:
    print("You must type either 'easy' or 'hard'.")

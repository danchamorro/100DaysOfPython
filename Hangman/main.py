import random
from hangman_art import stages, logo
from hangman_words import word_list


def hangman():
    print(logo)

    chosen_word = random.choice(word_list)

    # Number of player live's.
    lives = 6

    print(stages[-1])

    display = []

    for _ in chosen_word:
        display.append("_")

    print(display)

    while lives > 0:  # Check for number of lives
        guess = input("Choose a letter: ").lower()
        if guess not in chosen_word:  # reduce lives in guess not on chosen_word
            lives -= 1
            print(stages[lives])
        if lives == 0:
            print("You have no more lives try again")
        # If index of letter in word matches the index of display replace display index with letter
        for index, elem in enumerate(chosen_word):
            if elem == guess:
                display[index] = guess
        print(display)
        # When "_" is no longer present in display than you win.
        if "_" not in display:
            lives = 0
            print(" Yay you win!")
            break

    print("The answer was: ", chosen_word)

    # Ask if player wants to play again
    play_again = input("Do you want to play again? (y/n) ").lower()
    if play_again == "y":
        hangman()
    else:
        print("Bye!")


hangman()

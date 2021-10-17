import random


word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for letter in chosen_word:
    display.append("_")

print(display)

while "_" in display:  # if the the display still has bank lines continue
    guess = input("Choose a letter: ").lower()
    if guess not in chosen_word:  # Break out if letter not present in chosen_word
        print("You lost for now.")
        break

    # for letter in chosen_word:
    #     if letter == guess:
    #         display[chosen_word.index(letter)] = letter
    #         print(letter, "Right")
    #     else:
    #         print(letter, "Wrong")

    # Matching the index of the letter in the word to the index of the display
    for index, elem in enumerate(chosen_word):
        if elem == guess:
            display[index] = guess
            print(f"{guess} is found at index {index}")
    print(display)

print(display)
print(chosen_word)

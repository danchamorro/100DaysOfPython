alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


def encrypt(inp_text, inp_shift):
    cipher_text = ""
    for letter in inp_text:
        index = alphabet.index(letter)
        # This will prevent index out of range durring the shift. Instead the list will get extended by the inp_shift number
        if index > len(alphabet) or index < len(alphabet):
            alphabet.extend(alphabet * index)
        cipher_letter = alphabet[index + inp_shift]
        cipher_text = cipher_text + cipher_letter
        print("Original Index", index)
        print("Altered Index", index + inp_shift)
        print(cipher_letter)
    print(f"The encoded text is {cipher_text}.")


encrypt(inp_text=text, inp_shift=shift)

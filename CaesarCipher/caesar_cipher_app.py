# How to... Run the code and pick encode, then choose the a number by which you want to shift by. You will not get a encoded message
# To decode the message run program again and type decode. Then put the encoded message with the same shift numnber and your origial
# message will appear.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(inp_text, inp_shift):
    cipher_text = ""
    for letter in inp_text:
        index = alphabet.index(letter)
        # This will prevent index out of range durring the shift. Instead the list will get extended by the inp_shift number
        if index > len(alphabet) or index < len(alphabet):
            alphabet.extend(alphabet * index)
        cipher_letter = alphabet[index + inp_shift]
        cipher_text = cipher_text + cipher_letter
    print(f"The encoded text is {cipher_text}.")


def decrypt(cipher_text, inp_shift):
    plain_text = ""
    for letter in cipher_text:
        index = alphabet.index(letter)
        cipher_letter = alphabet[index - inp_shift]
        plain_text = plain_text + cipher_letter
    print(f"The encoded text is {plain_text}.")


if direction == "encode":
    encrypt(inp_text=text, inp_shift=shift)
elif direction == "decode":
    decrypt(cipher_text=text, inp_shift=shift)

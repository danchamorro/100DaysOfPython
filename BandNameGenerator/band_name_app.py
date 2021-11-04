# 1. Create a greeting for your program.
# 2. Ask the user for the city that they grew up in.
# 3. Ask the user for the name of a pet.
# 4. Combine the name of their city and pet and show them their band name.
# 5. Make sure the input cursor shows on a new line, see the example at:


# print("Welcome to the Band Name Generator")

# city = input("What's the name of the city you gre up in? \n")
# pet = input("What's your pets name? \n")

# print(f"Your band name could be {city} {pet} ")

def band_name_generator():
    cont = True
    while cont:
        city = input("What's the name of the city you grew up in? \n")
        pet = input("What's your pets name? \n")
        print(f"Your band name could be {city} {pet} ")
        cont = input("Would you like to generate another band name? (y/n) \n")
        if cont == "y":
            cont = True
        else:
            cont = False


band_name_generator()

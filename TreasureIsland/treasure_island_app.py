from art import art


def treasure_island():
    print(art)
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    option1 = input(
        "What direction do you want to move, Left or Right? ").lower()
    if option1 == "left":
        option2 = input("Swim or Wait? ").lower()
        if option2 == "wait":
            option3 = input("Which door? ").lower()
            if option3 == "yellow":
                print("You win")
            else:
                print("GAME OVER")
        else:
            print("GAME OVER")
    else:
        print("GAME OVER")


treasure_island()

# Blackjack
import random
from art import logo

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


player_cards = []

cpu_cards = []


def random_card():
    rand_card = random.choice(cards)
    player_cards.append(rand_card)


def deal_player_card():
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    player_cards.append(card1)
    player_cards.append(card2)


def deal_cpu_card():
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    cpu_cards.append(card1)
    cpu_cards.append(card2)


print(logo)


def blackjack():
    """[summary]
    Blackjack game. 
    """
    contin = True
    print("==================================")
    while contin:
        deal_player_card()
        print("Your cards:", player_cards)
        deal_cpu_card()
        print("Computer's first card:", cpu_cards[0])

        new_card = input("Type 'y' for another card, type 'n' to pass: ")

        if new_card == "n":
            print(player_cards)
        elif new_card == "y":
            random_card()
            print(player_cards)

        print("Your final hand:", player_cards)
        print("Computers final hand:", cpu_cards)

        if sum(player_cards) <= 21 and sum(player_cards) > sum(cpu_cards):
            print("You win!")
        else:
            print("Dealer wins!")

        new_game = input(
            "Do you want to play again? Type 'y' for yes and 'n' for no: ")

        if new_game == "n":
            contin = False
            break
        elif new_game == "y":
            player_cards.clear()
            cpu_cards.clear()
            blackjack()
    print("==================================")


blackjack()

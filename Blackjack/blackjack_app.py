# Blackjack
import random

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


deal_cpu_card()
deal_player_card()
print(player_cards)
print(cpu_cards)

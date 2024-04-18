# Blackjack, also known as 21, is a card game where players try to get a card total as close to 21 as possible without going over.
# The dealer and the player are both dealt two cards initially, with one of the dealer's cards facing down. Players then choose to "hit" (take another card) or "stand" (keep their current total), aiming to beat the dealer's hand.

# Here's a basic outline of what we'll do:

# Setup the Deck: We'll create a standard deck of 52 cards.
# Deal Cards: Both the dealer and the player will be dealt two cards at the beginning.
# Player's Turn: The player can choose to hit or stand.
# Dealer's Turn: The dealer must hit if their total is below 17.
# Determine the Winner: Compare the hands to see who wins.

import random

# Define the deck of cards
suits = ("Hearts", "Spades", "Clubs", "Diamonds")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)


# Create and shuffle a deck of cards
def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


# Calculate the value of a hand
def calculate_hand_value(hand):
    total = 0


def has_blackjack(hand):
    return calculate_hand_value(hand) == 21


def play_blackjack():
    deck = create_deck()
    print(len(deck))


def main():
    print("---------------------------------------------------")
    print("Welcome to Blackjack")
    print("---------------------------------------------------")
    play_blackjack()


main()

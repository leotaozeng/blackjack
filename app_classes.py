# Introduction:
# Blackjack, also known as 21, is a card game where players try to get a card total as close to 21 as possible without going over.
# The dealer and the player are both dealt two cards initially, with one of the dealer's cards facing down.
# Players then choose to "hit" (take another card) or "stand" (keep their current total), aiming to beat the dealer's hand.

# Here's a basic outline of what we'll do:
# 1. Setup the Deck: We'll create a standard deck of 52 cards.
# 2. Deal Cards: Both the dealer and the player will be dealt two cards at the beginning.
# 3. Player's Turn: The player can choose to hit or stand.
# 4. Dealer's Turn: The dealer must hit if their total is below 17.
# 5. Determine the Winner: Compare the hands to see who wins.

import random


suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
ranks = [
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
]
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    ("Ten", "Jack", "Queen", "King"): 10,
    "Ace": 11,
}


# a standard Deck means a pack of 52 unique playing cards
def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((suit, rank))
    random.shuffle(deck)
    return deck


create_deck()


class BlackjackGame:
    pass


game = BlackjackGame()

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
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}


def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def has_blackjack(hand):
    return calculate_hand_value(hand) == 21


def calculate_hand_value(hand):
    total = 0
    num_aces = 0

    for card in hand:
        rank = card[0]
        total += values[rank]
        if rank == "Ace":
            num_aces += 1

    # Adjust ace value from 11 to 1 if necessary (11 + 11 = 22)
    while total > 21 and num_aces:
        total -= 10
        num_aces -= 1

    return total


def show_hand(hand, player_name, hide_second_card=False):
    print(f"{player_name}'s hand:")
    for i, card in enumerate(hand):
        if i == 1 and hide_second_card:
            print("2. Hidden Card")
        else:
            print(f"{i + 1}. {card[0]}({values[card[0]]}) of {card[1]}")
    if hide_second_card:
        print(f"Total value: {values[hand[0][0]]} + ?")
    else:
        print(f"Total value: {calculate_hand_value(hand)}")
    print()


def check_for_blackjack(dealer_hand, player_hand):
    result = None

    if has_blackjack(dealer_hand) and has_blackjack(player_hand):
        result = "push"
    elif has_blackjack(dealer_hand):
        result = "dealer"
    elif has_blackjack(player_hand):
        result = "player"

    if result:
        show_hand(dealer_hand, "Dealer")
        show_hand(player_hand, "Player")
        if result == "push":
            print("Both player and dealer have blackjack. It's a push!")
        elif result == "dealer":
            print("Dealer has blackjack! Dealer wins!")
        elif result == "player":
            print("Player has blackjack! Player wins!")
    return result


def play_blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Check for blackjack
    if check_for_blackjack(dealer_hand, player_hand) != None:
        return

    # If no one has blackjack, continue the game
    # Dealer's turn
    show_hand(dealer_hand, "Dealer", hide_second_card=True)

    # Player's turn
    show_hand(player_hand, "Player")
    while calculate_hand_value(player_hand) < 21:
        action = input("Do you want to hit or stand? (h/s): ").lower()
        print()
        if action == "h":
            player_hand.append(deck.pop())
            show_hand(player_hand, "Player")
        elif action == "s":
            break

    # Dealer's turn
    show_hand(dealer_hand, "Dealer")
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        show_hand(dealer_hand, "Dealer")

    # Determine the winner
    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand)

    print("Player's total value:", player_total)
    print("Dealer's total value:", dealer_total)
    print()

    if player_total > 21:
        print("Player busts! Dealer wins.")
    elif dealer_total > 21:
        print("Dealer busts! Player wins.")
    elif player_total == dealer_total:
        print("It's a push!")
    elif player_total > dealer_total:
        print("Player wins!")
    else:
        print("Dealer wins!")


def main():
    print("---------------------------------------------------")
    print("Welcome to Blackjack")
    print("---------------------------------------------------")
    play_blackjack()


main()

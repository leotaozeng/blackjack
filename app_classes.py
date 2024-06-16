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
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}


# a standard Deck means a pack of 52 unique playing cards
def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


# 计算手牌总值
def calculate_hand_value(hand):
    total = 0
    num_aces = 0

    for card in hand:
        rank = card[0]
        total += values[rank]
        if rank == "Ace":
            num_aces += 1

    # In Blackjack, Aces can be worth either 1 or 11 points.
    # 如果总值超过 21，则将 Ace 的值从 11 改为 1
    if total > 21 and num_aces:
        total -= 10
        num_aces -= 1
    return total


def has_blackjack(hand):
    return calculate_hand_value(hand) == 21


def display_hand(hand, player_name, hide_second_card=False):
    print(f"{player_name}'s hand:")
    for count, card in enumerate(hand):
        if count == 1 and hide_second_card:
            print("Hidden Card")
        else:
            print(f"{count + 1}. {card[0]}({values[card[0]]}) of {card[1]}")
    if hide_second_card:
        print(f"Total value: {hand[0][0]}({values[card[0]]}) + ?")
    else:
        print(f"Total value: {calculate_hand_value(hand)}")
    print()


class BlackjackGame:
    def __init__(self):
        self.deck = create_deck()  # 创建并洗牌

    # 抽牌
    def pop_card(self):
        return self.deck.pop()

    # 发放初始手牌
    def deal_initial_hands(self):
        player_hand = [self.pop_card(), self.pop_card()]
        dealer_hand = [self.pop_card(), self.pop_card()]
        return player_hand, dealer_hand

    # 检查
    def check_for_blackjack(self, player_hand, dealer_hand):
        result = None
        if has_blackjack(player_hand) and has_blackjack(dealer_hand):
            result = "tie"
        elif has_blackjack(dealer_hand):
            result = "dealer"
        elif has_blackjack(player_hand):
            result = "player"
        return result

    # 进行一轮游戏
    def play_round(self):
        player_hand, dealer_hand = self.deal_initial_hands()
        blackjack_result = self.check_for_blackjack(player_hand, dealer_hand)
        if blackjack_result:
            display_hand(player_hand, "Player")
            display_hand(dealer_hand, "Dealer")
            if blackjack_result == "tie":
                print("Both player and dealer have blackjack. It's a tie!")
            elif blackjack_result == "player":
                print("Player has blackjack! Player wins!")
            elif blackjack_result == "dealer":
                print("Dealer has blackjack! Dealer wins!")
            return

        display_hand(dealer_hand, "Dealer", True)

        # Player's turn 玩家回合
        display_hand(player_hand, "Player")
        while calculate_hand_value(player_hand) < 21:
            action = input("Do you want to hit or stand? (h/s): ").low()
            if action == "h":
                player_hand.append(self.pop_card())
                display_hand(player_hand, "Player")
            elif action == "s":
                break

        # Dealer's turn 庄家回合
        display_hand(dealer_hand, "Dealer")


# Main function to start the game
def main():
    game = BlackjackGame()
    game.play_round()


if __name__ == "__main__":
    main()

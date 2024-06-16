# Introduction:
# Blackjack, also known as 21, is a card game where players try to get a card total as close to 21 as possible without going over.
# The dealer and the player are both dealt two cards initially, with one of the dealer's cards facing down.
# Players then choose to "hit" (take another card) or "stand" (keep their current total), aiming to beat the dealer's hand.

# * Here's a basic outline of what we'll do:
# * 1. Setup the Deck: We'll create a standard deck of 52 cards.
# * 2. Deal Cards: Both the dealer and the player will be dealt two cards at the beginning.
# * 3. Player's Turn: The player can choose to hit or stand.
# * 4. Dealer's Turn: The dealer must hit if their total is below 17.
# * 5. Determine the Winner: Compare the hands to see who wins.

# Playing cards - 扑克牌

import random


suits = ["Clubs", "Spades", "Hearts", "Diamonds"]  # 花色
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
]  # 等级
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
}  # 牌值


# a standard Deck means a pack of 52 unique playing cards
# 创建一副标准扑克牌并洗牌
def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    random.shuffle(deck)  # 洗牌
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

    # In Blackjack, Aces can be worth either 1 or 11 points
    # 如果总值超过 21，则将 Ace 的值从 11 改为 1
    if total > 21 and num_aces:
        total -= 10
        num_aces -= 1
    return total


# 显示手牌
def display_hand(hand, player_name, hand_name=None, hide_second_card=False):
    print(f"{player_name}'s {hand_name or 'hand'}:")

    for count, card in enumerate(hand):
        if count == 1 and hide_second_card:
            print("2. Hidden Card")
        else:
            print(f"{count + 1}. {values[card[0]]} of {card[1]}")

    if hide_second_card:
        print(f"Total value: {values[hand[0][0]]} + ?")
    else:
        print(f"Total value: {calculate_hand_value(hand)}")
    print()


def has_blackjack(hand):
    return calculate_hand_value(hand) == 21


class BlackjackGame:
    def __init__(self):
        self.deck = create_deck()  # 创建并洗牌 | Create and shuffle the deck

    # 抽牌
    def pop_card(self):
        return self.deck.pop()

    # 发放初始手牌
    def deal_initial_hands(self):
        player_hand = [self.pop_card(), self.pop_card()]
        dealer_hand = [self.pop_card(), self.pop_card()]
        return player_hand, dealer_hand

    def check_for_blackjack(self, player_hand, dealer_hand):
        result = None
        if has_blackjack(player_hand) and has_blackjack(dealer_hand):
            result = "tie"
        elif has_blackjack(dealer_hand):
            result = "dealer"
        elif has_blackjack(player_hand):
            result = "player"
        return result

    def handle_split(self, player_hand):
        player_hand1 = [player_hand[0], self.pop_card()]
        player_hand2 = [player_hand[1], self.pop_card()]
        return [player_hand1, player_hand2]

    def play_round(self):
        # * [(Two, Clubs), (Three, Spades)]
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

        # 隐藏庄家的第二张牌
        display_hand(dealer_hand, "Dealer", hide_second_card=True)

        # Player's turn
        display_hand(player_hand, "Player")
        # Check if split is possible
        if values[player_hand[0][0]] == values[player_hand[1][0]]:
            split_choice = input("Do you want to split your hand? (y/n): ").lower()
            print()
            if split_choice == "y":
                # * [[(Two, Clubs), (Three, Spades)], [(Two, Clubs), (Three, Spades)]]
                split_hands = self.handle_split(player_hand)
                for count, hand in enumerate(split_hands):
                    display_hand(hand, "Player", f"hand{count+1}")
                    self.play_hand(hand, "Player", f"hand{count+1}")
                self.play_hand(dealer_hand, "Dealer")
                self.compare_hands(split_hands, dealer_hand)
                return
        else:
            self.play_hand(player_hand, "Player")

        # Dealer's turn
        self.play_hand(dealer_hand, "Dealer")

        # Determine the outcome
        self.compare_hands(player_hand, dealer_hand)

    def play_hand(self, hand, player_name, hand_name=None):
        if player_name == "Player":
            while calculate_hand_value(hand) < 21:
                action = input("Do you want to hit or stand? (h/s): ").lower()
                print()
                if action == "h":
                    hand.append(self.pop_card())
                    display_hand(hand, "Player", hand_name)
                elif action == "s":
                    break
        elif player_name == "Dealer":
            while calculate_hand_value(hand) < 17:
                hand.append(self.pop_card())
                display_hand(hand, "Dealer")

    def compare_hands(self, player_hand, dealer_hand):
        dealer_total = calculate_hand_value(dealer_hand)

        if isinstance((player_hand[0]), list):
            for count, hand in enumerate(player_hand):
                player_total = calculate_hand_value(hand)

                print(f"Player's hand{count+1} total value:", player_total)
                print("Dealer's total value:", dealer_total)

                if player_total > 21:
                    print("Player busts! Dealer wins.")
                elif dealer_total > 21:
                    print("Dealer busts! Player wins.")
                elif player_total == dealer_total:
                    print("It's a tie!")
                elif player_total > dealer_total:
                    print("Player wins!")
                else:
                    print("Dealer wins!")
                print()
        else:
            player_total = calculate_hand_value(player_hand)

            print("Player's total value:", player_total)
            print("Dealer's total value:", dealer_total)

            if player_total > 21:
                print("Player busts! Dealer wins.")
            elif dealer_total > 21:
                print("Dealer busts! Player wins.")
            elif player_total == dealer_total:
                print("It's a tie!")
            elif player_total > dealer_total:
                print("Player wins!")
            else:
                print("Dealer wins!")
            print()


# Main function to start the game
def main():
    print("Welcome to Blackjack! \n")
    while True:
        game = BlackjackGame()
        game.play_round()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != "y":
            break


if __name__ == "__main__":
    main()

import random

# Constants for suits, ranks, and values
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


# Card class to represent a single card
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{values[self.rank]} of {self.suit}"

    @property
    def value(self):
        return values[self.rank]


# Hand class to represent a hand of cards
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def value(self):
        total = sum(card.value for card in self.cards)
        num_aces = sum(card.rank == "Ace" for card in self.cards)
        while total > 21 and num_aces:
            total -= 10
            num_aces -= 1
        return total

    def is_blackjack(self):
        return self.value() == 21

    def display(self, player_name, hand_name=None, hide_second_card=False):
        print(f"{player_name}'s {hand_name or 'hand'}:")
        for count, card in enumerate(self.cards):
            if count == 1 and hide_second_card:
                print("2. Hidden Card")
            else:
                print(f"{count + 1}. {card}")
        if hide_second_card:
            print(f"Total value: {self.cards[0].value} + ?")
        else:
            print(f"Total value: {self.value()}")
        print()


# Function to create and shuffle a deck of cards
# a standard Deck means a pack of 52 unique playing cards
# 创建一副标准扑克牌并洗牌
def create_deck():
    deck = [Card(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck


# BlackjackGame class to manage the game logic
class BlackjackGame:
    def __init__(self):
        self.deck = create_deck()

    def pop_card(self):
        return self.deck.pop()

    def deal_initial_hands(self):
        player_hand = Hand()
        dealer_hand = Hand()
        for _ in range(2):
            player_hand.add_card(self.pop_card())
            dealer_hand.add_card(self.pop_card())
        return player_hand, dealer_hand

    def check_for_blackjack(self, player_hand, dealer_hand):
        if player_hand.is_blackjack() and dealer_hand.is_blackjack():
            return "tie"
        elif dealer_hand.is_blackjack():
            return "dealer"
        elif player_hand.is_blackjack():
            return "player"
        return None

    def handle_split(self, player_hand):
        hand1 = Hand()
        hand2 = Hand()
        hand1.add_card(player_hand.cards[0])
        hand2.add_card(player_hand.cards[1])
        hand1.add_card(self.pop_card())
        hand2.add_card(self.pop_card())
        return [hand1, hand2]

    def play_round(self):
        player_hand, dealer_hand = self.deal_initial_hands()
        blackjack_result = self.check_for_blackjack(player_hand, dealer_hand)

        if blackjack_result:
            player_hand.display("Player")
            dealer_hand.display("Dealer")
            if blackjack_result == "tie":
                print("Both player and dealer have blackjack. It's a tie!")
            elif blackjack_result == "player":
                print("Player has blackjack! Player wins!")
            elif blackjack_result == "dealer":
                print("Dealer has blackjack! Dealer wins!")
            return

        dealer_hand.display("Dealer", hide_second_card=True)
        player_hand.display("Player")

        if player_hand.cards[0].rank == player_hand.cards[1].rank:
            split_choice = input("Do you want to split your hand? (y/n): ").lower()
            print()
            if split_choice == "y":
                split_hands = self.handle_split(player_hand)
                for count, hand in enumerate(split_hands):
                    hand.display("Player", f"hand{count + 1}")
                    self.play_hand(hand, "Player", f"hand{count + 1}")
                self.play_hand(dealer_hand, "Dealer")
                self.compare_hands(split_hands, dealer_hand)
                return
        else:
            self.play_hand(player_hand, "Player")

        self.play_hand(dealer_hand, "Dealer")
        self.compare_hands(player_hand, dealer_hand)

    def play_hand(self, hand, player_name, hand_name=None):
        if player_name == "Player":
            while hand.value() < 21:
                action = input("Do you want to hit or stand? (h/s): ").lower()
                print()
                if action == "h":
                    hand.add_card(self.pop_card())
                    hand.display(player_name, hand_name)
                elif action == "s":
                    break
        elif player_name == "Dealer":
            while hand.value() < 17:
                hand.add_card(self.pop_card())
                hand.display(player_name)

    def compare_hands(self, player_hand, dealer_hand):
        dealer_total = dealer_hand.value()
        if isinstance(player_hand, list):
            for count, hand in enumerate(player_hand):
                player_total = hand.value()
                print(f"Player's hand{count + 1} total value:", player_total)
                print("Dealer's total value:", dealer_total)
                self.determine_winner(player_total, dealer_total)
                print()
        else:
            player_total = player_hand.value()
            print("Player's total value:", player_total)
            print("Dealer's total value:", dealer_total)
            self.determine_winner(player_total, dealer_total)
            print()

    def determine_winner(self, player_total, dealer_total):
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

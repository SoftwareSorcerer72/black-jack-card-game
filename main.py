import random
# need to create a deck of cards a have player/dealer hands

# deal the cards
 
# program needs to calculate the value of each hand

# compare dealer hand to player hand to determine the winner

# and the game loop

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.suit_symbols = {'Hearts': '\u2665', 'Diamonds': '\u2666', 'Clubs': '\u2663', 'Spades': '\u2660'}

    def show(self):
        print(f" _______")
        print(f"|{self.rank:<2}     |")
        print(f"|   {self.suit_symbols[self.suit]}   |")
        print(f"|       |")
        print(f"|   {self.suit_symbols[self.suit]}   |")
        print(f"|_______|")

class Deck:
    def __init__(self):
        self.cards = []
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits= ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def deal(self, player):
        card = self.cards.pop()
        player.hand.append(card)

class Player:
    def __init__(self):
        self.hand = []

    def calculate_hand(self):
        value = 0
        for card in self.hand:
            if card.rank in ['J', 'Q', 'K']:
                value += 10
            elif card.rank == 'A':
                value += 11 if value <= 10 else 1
            else:
                value += int(card.rank)
        return value

class Dealer(Player):
    def should_hit(self):
        return self.calculate_hand() < 17

# Initialize playing to True
playing = True

while playing:
    #shuffles the deck 
    deck = Deck()
    random.shuffle(deck.cards)

    # creates player and dealer instances 
    player = Player()
    dealer = Dealer()

    # deals  initial cards with a throwaway variable 
    for _ in range(2):
        deck.deal(player)
        deck.deal(dealer)

    # players turn 
    while True:
        print("Your hand:")
        for card in player.hand:
            card.show()
        print(f"Total: {player.calculate_hand()}")
        if player.calculate_hand() > 21:
            print("You bust! The dealer wins.")
            break
        should_continue = input("Would you like to hit or stand? (h/s): ")
        if should_continue.lower().strip() == "h":
            deck.deal(player)
        else:
            break

    # dealers turn 
    if player.calculate_hand() <= 21:
        while dealer.should_hit():
            deck.deal(dealer)
        print("Dealer's hand:")
        for card in dealer.hand:
            card.show()
        print(f"Total: {dealer.calculate_hand()}")
        if dealer.calculate_hand() > 21 or dealer.calculate_hand() < player.calculate_hand():
            print("The Dealer Busts! You Win!")
        elif dealer.calculate_hand() > player.calculate_hand():
            print("The Dealer wins!")
        else:
            print("It's a tie")
    
    # ask to play again
    play_again = input("Would you like to play another round? (y/n): ")
    if play_again.lower().strip() != "y":
        playing = False
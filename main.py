# need to create a deck of cards a have player/dealer hands

# deal the cards
 
# program needs to calculate the value of each hand

# compare dealer hand to player hand to determine the winner

# and the game loop

class Card:
    def __init__(self, rank):
        self.rank = rank

class Deck:
    def __init__(self):
        self.cards = []
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for rank in ranks:
            self.card.append(Card(rank))

    def deal(self, player)
        card = self.cards.pop()
        player.hand.append(card)

class Player:
    def __init__(self):
        self.hand = []

    def calculate_hand(self):
        pass

class Dealer(Player):
    pass
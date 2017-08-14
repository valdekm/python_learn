import random

class Deck(object):
    cards = []
    def __init__(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(suit + " of " + rank)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def reveal_cards(self):
        for card in self.cards:
            print(card)



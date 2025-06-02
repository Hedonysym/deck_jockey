from card import Card
from deck import Deck

class Player:
    def __init__(self, name: str, deck: Deck):
        self.name = name
        self.deck = deck
        self.hand = []
        self.resources = 0
        self.production = 0

    def draw(self):
        self.hand.append(self.deck.draw())



from card import Card
from deck import Deck

class Player:
    def __init__(self, name: str, deck: Deck):
        self.name = name
        self.deck = deck
        self.hand = []
        self.trash = []
        self.resources = 0
        self.production = 0
        self.first_turn()

    def draw(self):
        self.hand.append(self.deck.draw())

    def first_turn(self):
        for i in range(5):
            self.draw()
        self.resources += 1
        self.show_hand()


    def show_hand(self, desc=False):
        print(f"{self.name}'s Hand:")
        for card in self.hand:
            card.show_card(desc)

    def turn_upkeep(self):
        self.resources += 1
        self.draw()
        print(f"{self.name} has {self.production} production so far")
        self.show_hand()
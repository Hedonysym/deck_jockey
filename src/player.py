from card import Card
from deck import Deck

class Player:
    def __init__(self, name: str, deck: Deck):
        self.name = name
        self.deck = deck
        self.hand = []
        self.trash = []
        self.max_resources = 0
        self.resources = 0
        self.production = 0
        self.turn_num = 0

    def draw(self):
        self.hand.append(self.deck.draw())


    def show_trash(self):
        print(f"{self.name}'s Trash: ")
        for card in self.trash:
            card.show_card()


    def show_hand(self, desc=False):
        print(f"{self.name}'s Hand:")
        for card in self.hand:
            card.show_card(desc)

    def turn_cycle(self):
        if self.turn_num == 0:
            for i in range(4):
                self.draw()
        self.max_resources += 1
        self.resources = self.max_resources
        self.draw()
        self.turn_num += 1
        print(f"{self.name}: Turn {self.turn_num}")
        print(f"{self.name} has {self.production} production and {self.max_resources} resources")
        self.show_hand()
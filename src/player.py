from card import Card
from deck import Deck

class Player:
    def __init__(self, name: str, deck: Deck):
        self.name = name
        self.deck = deck
        self.hand = []
        self.trash = []
        self.loops = []
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
        self.looper()
        print(f"{self.name} has {self.production} production and {self.resources}/{self.max_resources} resources")
        self.show_hand()
    
    def looper(self):
        for loop in self.loops:
            if loop.value is None or loop.value > 0:
                for card in loop.cards:
                    if card.type != "LOOP":
                        print(f"{card.name}")
                        card.play(self)
                    else:
                        print(f"{loop.name} {loop.value}")
                if loop.value is not None:
                    loop.value -= 1
            else:
                self.loops.remove(loop)
    
    def break_all(self):
        for loop in self.loops:
            self.loops.remove(loop)

    
    def play_card(self, card_name: str):
        for card in self.hand:
            if card.name == card_name:
                if self.cost_chk(card.cost) == True:
                    self.hand.remove(card)
                    match (card.type):
                        case "COMMAND":
                            card.play(self)
                            self.trash.append(card)
                        case "OPERATOR":
                            card.play(self)
                            self.trash.append(card)
                        case "LOOP":
                            card.play(self, card)
                        case _:
                            print("\nInvalid card type")
                    print(f"\n{self.resources}/{self.max_resources} remaining")
                    return
                else:
                    return
        print(f"\n{card_name} not in hand!")
    
    
    def create_loop(self, name, loopcard, value=None):
        while True:
            card_name = input("\nPick a command card\n")
            for card in self.hand:
                if card.name == card_name:
                    if card.type != "COMMAND":
                        print("\nNot a command card!")
                        continue
                    else: 
                        loop = Loop(name, loopcard, value)
                        loop.cards.append(card)
                        self.loops.append(loop)
                        return



    def cost_chk(self, value):
        if value > self.resources:
            print("\nInsufficient resources!")
            return False
        return True
    
    def recycle(self, value):
        for i in range(value):
            card_name = input("\nWhat card do you want to recycle?\n")
            for card in self.trash:
                if card.name == card_name:
                    self.trash.remove(card)
                    self.hand.append(card)
                    return
                else:
                    print("Card not in trash!")

    def discard(self, value):
        for i in range(value):
            card_name = input("\nWhat card do you want to discard?\n")
            for card in self.hand:
                if card.name == card_name:
                    self.hand.remove(card)
                    self.trash.append(card)
                    return



class Loop:
    def __init__(self, name, card, value=None):
        self.name = name
        self.cards = []
        self.cards.append(card)
        self.value = value

    def loop_cards(self):
        for card in self.cards:
            if card.type != "Loop":
                try:
                    print(f"{card.name}")
                    card.play(self, )
                except Exception as e:
                    print(e)
            else:
                print(f"{self.name} {self.value}")
        if self.value is not None:
            self.value -= 1
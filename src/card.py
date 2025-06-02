from enum import Enum

class CardType(Enum):
    COMMAND = 1
    LOOP = 2
    OPERATOR = 3


class Card:
    def __init__(self, name: str, type: CardType, desc: str):
        self.type = type
        self.name = name
        self.desc = desc

    def __repr__(self):
        return f"Card({self.type}, {self.name}, {self.desc})"
    
    
from enum import Enum
import colorama


class CardType(Enum):
    COMMAND = "COMMAND"
    LOOP = "LOOP"
    OPERATOR = "OPERATOR"


class Card:
    def __init__(self, name: str, type: CardType, desc: str, cost=0):
        self.type = type
        self.name = name
        self.desc = desc
        self.cost = cost

    def __repr__(self):
        return f"\nCard({self.type}, {self.name}, {self.desc})"
    
    def show_card(self, desc=False):
        match self.type:
            case "COMMAND":
                print(f"{colorama.Fore.RED}{self.name}: {self.cost}{colorama.Style.RESET_ALL}")
            case "LOOP":
                print(f"{colorama.Fore.BLUE}{self.name}: {self.cost}{colorama.Style.RESET_ALL}")
            case "OPERATOR":
                print(f"{colorama.Fore.GREEN}{self.name}: {self.cost}{colorama.Style.RESET_ALL}")
        if desc:
            print(self.desc)

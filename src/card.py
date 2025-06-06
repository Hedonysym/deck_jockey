from enum import Enum
import colorama

def _while(player, card):
    pass

def _for_3(player, card):
    pass

def _for_2(player, card):
    pass

def _increment(player):
    pass

def _decrement(player):
    pass

def _and(player):
    pass

def _coffee_break(player, arg=None):
    cost, value = 1, 1
    if arg == "increment":
        cost += 1 
        value += 1
    if arg == "decrement":
        cost -= 1
        value -= 1
    player.cost_chk(cost)
    loops = len(player.loops)
    player.break_all()
    player.max_resources += value + loops

def _lunch_break(player, arg=None):
    cost, value = 1, 1
    if arg == "increment":
        cost += 1 
        value += 1
    if arg == "decrement":
        cost -= 1
        value -= 1
    player.cost_chk(cost)

def _recycle(player, arg=None):
    cost, value = 1, 1
    if arg == "increment":
        cost += 1 
        value += 1
    if arg == "decrement":
        cost -= 1
        value -= 1
    player.cost_chk(cost)

def _zoom_call(player, arg=None):
    cost, value = 1, 1
    if arg == "increment":
        cost += 1 
        value += 1
    if arg == "decrement":
        cost -= 1
        value -= 1
    player.cost_chk(cost)

def _hotfix(player, arg=None):
    cost, value = 1, 1
    if arg == "increment":
        cost += 1 
        value += 1
    if arg == "decrement":
        cost -= 1
        value -= 1
    player.cost_chk(cost)

def _major_update(player, arg=None):
    cost, value = 1, 1
    if arg == "increment":
        cost += 1 
        value += 1
    if arg == "decrement":
        cost -= 1
        value -= 1
    player.cost_chk(cost)

def _minor_update(player, arg=None):
    cost, value = 1, 1
    if arg == "increment":
        cost += 1 
        value += 1
    if arg == "decrement":
        cost -= 1
        value -= 1
    player.cost_chk(cost)

card_actions = {
    "while" : _while,
    "for 3" : _for_3,
    "for 2" : _for_2,
    "++ increment" : _increment,
    "-- decrement" : _decrement,
    "&& and" : _and,
    "coffee break" : _coffee_break,
    "lunch break" : _lunch_break,
    "recycle" : _recycle,
    "zoom call" : _zoom_call,
    "hotfix" : _hotfix,
    "major update" : _major_update,
    "minor update" : _minor_update
}

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
    
    def play(self, player, args=None):
        action = card_actions.get(self.name)
        if action:
            action(player, args)
        else:
            print(f"Unimplemented card: {self.name}")

from enum import Enum
import colorama

def _while(card, player, none):
    player.resources -= card.cost
    player.create_loop("while", card, None)

def _for_3(card, player, none):
    player.resources -= card.cost
    player.create_loop("for", card, 3)

def _for_2(card, player, none):
    player.resources -= card.cost
    player.create_loop("for", card, 2)

def _increment(card, player, none):
    while True:
        card_name = input("\nPick a command card\n")
        for card in player.hand:
            if card.name == card_name:
                if card.type != "COMMAND":
                    print("\nNot a command card!")
                else:
                    card.play("increment")
                    break
            

def _decrement(card, player, none):
    while True:
            card_name = input("\nPick a command card\n")
            for card in player.hand:
                if card.name == card_name:
                    if card.type != "COMMAND":
                        print("\nNot a command card!")
                    else:
                        card.play("decrement")
                        break

def _and(card, player, arg=None):
    while True:
        if len(player.loops) == 0:
            print("\nNo loops")
            return
        loop_name = input("\nChoose an active loop!\n")
        for loop in player.loops:
            if loop_name == loop.name:
                while True:
                    card_name = input("\nPick a command card\n")
                    for card in player.hand:
                        if card.name == card_name:
                            if card.type != "COMMAND":
                                print("\nNot a command card!")
                            else:
                                loop.cards.append(card)
                                break
                
            else:
                print("\nNot valid")


def _coffee_break(card, player, arg=None):
    cost, value = 1, 1
    if arg == "increment":
        cost += 1 
        value += 1
    if arg == "decrement":
        cost -= 1
        value -= 1
    player.resources -= cost
    loops = len(player.loops)
    player.break_all()
    player.max_resources += value + loops

def _lunch_break(card, player, arg=None):
    cost, value = 2, 2
    if arg == "increment":
        cost += 1 
        value += 1
    if arg == "decrement":
        cost -= 1
        value -= 1
    player.resources -= cost
    loops = len(player.loops)
    player.break_all()
    for i in range(loops + value):
        player.draw()

def _recycle(card, player, arg=None):
    cost, value = 2, 2
    if arg == "increment":
        cost += 1 
        value += 1
    if arg == "decrement":
        cost -= 1
        value -= 1
    player.resources -= cost
    player.recycle(value)

def _zoom_call(card, player, arg=None):
    cost, value = 2, 2
    if arg == "increment":
        cost += 1 
        value += 1
    if arg == "decrement":
        cost -= 1
        value -= 1
    player.resources -= cost
    player.discard(1)
    player.production += value

def _hotfix(card, player, arg=None):
    cost, value = 3, 2
    if arg == "increment":
        cost += 1 
        value += 1
    if arg == "decrement":
        cost -= 1
        value -= 1
    player.resources -= cost
    player.production -= 1
    for i in range(value):
        player.draw()
    player.resources = player.max_resourses


def _major_update(card, player, arg=None):
    cost, value = 4, 4
    if arg == "increment":
        cost += 1 
        value += 1
    if arg == "decrement":
        cost -= 1
        value -= 1
    player.resources -= cost
    player.production += value


def _minor_update(card, player, arg=None):
    cost, value = 3, 3
    if arg == "increment":
        cost += 1 
        value += 1
    if arg == "decrement":
        cost -= 1
        value -= 1
    player.resources -= cost
    player.production += value

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
            action(self, player, args)
        else:
            print(f"Unimplemented card: {self.name}")

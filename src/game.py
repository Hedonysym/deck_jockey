import os
import cmd
from player import Player
from deck import Deck
import queue

class Game:
    def __init__(self):
        self.turn_order = queue.Queue()


    def game_start(self):
        print("How many players? (1-4)")
        num_players = int(input('\n'))
        if not isinstance(num_players, int) or num_players < 1 or num_players > 4:
            raise ValueError("Not a valid number, try again")
        for i in range(num_players):
            print(f"Ready, Player {i + 1}?")
            self.init_game_player()
        print("Everyone's ready. Game start!")

    def init_game_player(self):
        
        print("What's your name, gamer? ")
        name = input("\n")
        print("Choose a decklist.")
        while True:
            try:
                deck = self.decklist_select()
                break
            except Exception as e:
                print(e)
        listed_deck = deck.splitlines()
        final_deck = Deck(listed_deck)
        self.turn_order.put(Player(name, final_deck))
    
    def decklist_select(self):
        repo_dir = os.path.join(os.path.dirname(__file__), "..")
        decklist_dir = repo_dir + '/decklists/'
        for file in os.listdir(decklist_dir):
            print(file)
        deck_file_name = input("\n")
        if deck_file_name not in os.listdir(decklist_dir):
            raise ValueError("Decklist not found")
        with open(decklist_dir + deck_file_name, 'r') as file:
            deck = file.read()
        return deck
    
    def next_turn(self):
        turn = TurnMan(self, self.turn_order.get())
        turn.cmdloop()


class TurnMan(cmd.Cmd):
    def __init__(self, current_game: Game, turn_player: Player):
        super().__init__()
        self.game = current_game
        self.turn_player = turn_player
        self.prompt = f'{self.turn_player.name}: '
    
    def do_show(self, arg=None):
        if arg:
            match (arg):
                case 'hand':
                    self.turn_player.show_hand()
                case 'trash':
                    self.turn_player.show_trash()
                case _:
                    for card in self.turn_player.hand:
                        if card.name == arg:
                            card.show_card()
                    print(f"{arg} not in hand")
        else:
            print("Show what?")

    def do_pass(self, arg):
        print(f"{self.turn_player.name} ends their turn")
        self.game.turn_order.put(self.turn_player)
        self.game.next_turn()


    def do_quit(self, arg):
        print(f"{self.turn_player.name} conceeded!")
        quit()


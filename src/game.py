import os
import cmd
from player import Player
from deck import Deck
import queue

class Game:
    def __init__(self):
        self.turn_order = queue.Queue()


    def game_start(self):
        print("\nHow many players? (1-4)")
        num_players = int(input('\n'))
        if not isinstance(num_players, int) or num_players < 1 or num_players > 4:
            raise ValueError("\nNot a valid number, try again")
        for i in range(num_players):
            print(f"Ready, Player {i + 1}?")
            self.init_game_player()
        print("Everyone's ready. Game start!\n")

    def init_game_player(self):
        print("\nWhat's your name, gamer? ")
        name = input("\n")
        print("\nChoose a decklist.")
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
        decklist_dir = os.path.join(repo_dir, 'decklists')
        for file in os.listdir(decklist_dir):
            print(file)
        deck_file_name = input("\n")
        if deck_file_name not in os.listdir(decklist_dir):
            raise ValueError("Decklist not found\n")
        with open(os.path.join(decklist_dir, deck_file_name), 'r') as file:
            deck = file.read()
        return deck
    
    def next_turn(self):
        
        while True:
            player = self.turn_order.get()
            try:
                player.turn_cycle()
                break
            except Exception as e:
                print(f"{player.name} {e}")
                if self.turn_order.qsize() == 0:
                    quit()
                elif self.turn_order.qsize() == 1:
                    self.win(self.turn_order.get())
                    
        turn = TurnMan(self, player)
        turn.cmdloop()

    def win(self, player: Player):
        print(f"\n{player.name} Wins!")
        print(f"Final Turn Count: {player.turn_num}")
        quit()

class TurnMan(cmd.Cmd):
    def __init__(self, current_game: Game, turn_player: Player):
        super().__init__()
        self.game = current_game
        self.turn_player = turn_player
        self.prompt = f'\n{self.turn_player.name}: '
    
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
                            card.show_card(True)
                            return
                    print(f"\n{arg} not in hand")
        else:
            print("\nShow what?")
    
    def help_show(self):
        print("\nusage: show <argument>\n" \
        "show hand - lists cards in the hand of turn player\n" \
        "show trash - lists cards in the trash of turn player\n" \
        "show <card name> - detailed description of a card in hand")


    def do_pass(self, arg):
        print(f"\n{self.turn_player.name} ends their turn\n")
        self.game.turn_order.put(self.turn_player)
        self.game.next_turn()
        return True
    
    def help_pass(self):
        print("\nusage: pass\n" \
        "pass - turn player passes the turn")
   

    def do_quit(self, arg):
        print(f"\n{self.turn_player.name} quit!")
        if self.game.turn_order.qsize() == 1:
            self.game.win(self.game.turn_order.get())
        elif self.game.turn_order.qsize() == 0:
            quit()
        self.game.next_turn()
        return True
    
    
    def help_quit(self):
        print("\nusage: quit\n" \
        "quit - turn player condeeds the game, if there is only one more player, they win")


    


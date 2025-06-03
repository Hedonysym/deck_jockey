import sys
import os
from player import Player
from deck import Deck

def init_game_player():
    repo_dir = os.path.join(os.path.dirname(__file__), "..")
    decklist_dir = repo_dir + '/decklists/'
    print("What's your name, gamer? ")
    name = input("\n")
    print("Choose a decklist.")
    for file in os.listdir(decklist_dir):
        print(file)
    deck_file_name = input("\n")
    with open(decklist_dir + deck_file_name, 'r') as file:
        deck = file.read()
    listed_deck = deck.splitlines()
    final_deck = Deck(listed_deck)
    print("~~~~~~~~~~~")
    print("Game Start!")
    print("~~~~~~~~~~~")    
    return Player(name, final_deck)

def turn_wait(player: Player):
    print("What would you like to do?")
    cmd = input('\n')
    match cmd:
        case 'show hand':
            player.show_hand()
            turn_wait(player)
        case 'quit':
            print("Good-bye!")
            exit()

        case _:
            print("Not a command, you can use 'help' to see all valid commands")
            turn_wait(player)

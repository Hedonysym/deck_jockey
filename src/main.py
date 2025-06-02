import sys
import os
from player import Player
from deck import Deck

def init_game_player():
    repo_dir = os.path.join(os.path.dirname(__file__), "..")
    decklist_dir = repo_dir + '/decklists/'
    print("What's your name, gamer? ")
    name = input("")
    print("Choose a decklist.")
    for file in os.listdir(decklist_dir):
        print(file)
    deck_file_name = input("")
    with open(decklist_dir + deck_file_name, 'r') as file:
        deck = file.read()
    listed_deck = deck.splitlines()
    final_deck = Deck(listed_deck)
    return Player(name, final_deck)


def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to Deck Jockey!")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    player = init_game_player()
    for card in player.deck.cards:
        print(card)

if __name__ == "__main__":
    main()
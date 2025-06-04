import sys
import os
from player import Player
from deck import Deck
from game import Game

def init_game(game):
    while True:
        try:
            game.game_start()
            break
        except Exception as e:
            print(e)


def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to Deck Jockey!")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    game = Game()
    init_game(game)
    game.next_turn()


if __name__ == "__main__":
    main()
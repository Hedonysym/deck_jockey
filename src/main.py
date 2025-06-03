import sys
import os
from player import Player
from deck import Deck
from game import *


def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to Deck Jockey!")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    player = init_game_player()
    turn_wait(player)

if __name__ == "__main__":
    main()
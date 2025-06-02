import random
import json
from card import Card

class Deck:
    def __init__(self, decklist: list):
        self.cards = self.decklist_to_deck(decklist)
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)
        return self

    def draw(self):
        return self.cards.pop()
    
    def decklist_to_deck(self, decklist: list):
        try:
            with open('./src/card_data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print("Error: card_data.json file not found")
            return []
        except json.JSONDecodeError as e:
            print(f"Error: invalid JSON in card_data.json - {e}")
            return []

        cards = []
        for name in decklist:
            card_name = name.strip()
            if card_name in data:
                card_type = data[card_name][0]['type']
                card_desc = data[card_name][1]['desc']
                card = Card(card_name, card_type, card_desc)
                cards.append(card)
            else:
                print(f"Warning: unknown card {card_name}")

        return cards




class Trash:
    def __init__(self):
        self.trash = []

    def add_to_trash(self, card):
        self.trash.append(card)
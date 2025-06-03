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
                card_type = data[card_name]['type']
                card_desc = data[card_name]['desc']
                card_cost = data[card_name]['cost']
                card = Card(card_name, card_type, card_desc, card_cost)
                cards.append(card)
            else:
                print(f"Warning: unknown card {card_name}")

        return cards


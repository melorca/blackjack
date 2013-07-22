import random
from Card import *

class Deck:
    """Defines the deck of cards."""
    def __init__(self):
        """Creates a new deck of cards with one card of each.
        It is initialized in order."""
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        """Shuffles the deck to randomize it."""
        random.shuffle(self.cards)

    def deal_card(self):
        """Returns a card and removes it from the deck"""
        return self.cards.pop()
    
    def __str__(self):
        """Returns a string with all the cards in the deck
        separated by a ','."""
        result = ""
        for card in self.cards:
            result += str(card)+","
        return result[:-1]

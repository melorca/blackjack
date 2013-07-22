from Card import *

class Hand:
    """Defines a hand with cards."""
    def __init__(self):
        """Initializaes the hand with no cards."""
        self.cards = []

    def __str__(self):
        """Returns a string with all the cards in the hand 
        separated by a ','."""
        result = ""
        for card in self.cards:
            result += str(card)+","
        return result[:-1]
    
    def add_card(self, card):
        """Adds the given card to the hand."""
        self.cards.append(card)

    def get_value(self):
        """Returns the value as number of the hand"""
        has_ace = False
        value = 0
        for card in self.cards:
            has_ace = has_ace or card.rank == "A"
            value += VALUES[card.rank]
        if has_ace and value < 12:
            value += 10
        return value 
   
    def draw(self, canvas, pos):
        """Draws the hand in the canvas. 
        Needs to be implemented"""
        pass

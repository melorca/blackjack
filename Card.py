import Tkinter as Tk
"""Contains the Card class and cards definitions: SUITS, RANKS AND VALUES"""
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)

class Card:
    """Defines a card. Creates a new card with the provided suit and rank.
    Returns empty card if suit and rank doesn't match."""
    def __init__(self, suit, rank):
        """Creates a new card with the provided suit and rank.
        Returns empty card if suit and rank doesn't match."""
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        """Returns a string with the suit and the rank"""
        return self.suit + self.rank

    def get_suit(self):
        """Returns the suit as a string"""
        return self.suit

    def get_rank(self):
        """Returns the rank as a string"""
        return self.rank

    def draw(self, canvas, pos):
        """Draws the card in the given canvas.
        Returns the image and itemid on canvas. Image needs to be stored in a 
        variable to be displayed in the canvas"""
        spritesheet = Tk.PhotoImage(file="cards.jfitz.gif")
        #assigning location is working correctly
        l = CARD_SIZE[0] * RANKS.index(self.rank)
        r = l +  CARD_SIZE[0];
        t = CARD_SIZE[1] * SUITS.index(self.suit)
        b = t + CARD_SIZE[1]
        card_img = self.subimage(spritesheet, l, t, r, b)
        itemid = canvas.create_image(pos[0], pos[1], image = card_img)
        return card_img, itemid

    def subimage(self, img, l, t, r, b):
        """Returns the are defined by left, top, right and bottom
         of the given image as an image"""
        #print(l,t,r,b)
        dst = Tk.PhotoImage()
        dst.tk.call(dst, 'copy', img, '-from', l, t, r, b, '-to', 0, 0)
        return dst
    
def draw_back(canvas, pos):
    """Draws the back of the cards on the given canvas at the given position 
    tupple (x,y). Returns image and itemid on canvas."""
    card_back = Tk.PhotoImage(file = "card_back.gif")
    itemid = canvas.create_image(pos[0], pos[1], image = card_back)
    return card_back, itemid

if __name__ == "__main__":
    card = Card("S","K")
    print card
    m = Tk.Tk()
    w = Tk.Canvas(m, width = 400, height = 400)
    w.pack()
    out = card.draw(w, (100,100)) #the image
    out
    out[1]
    
    """Test subimage()
    spritesheet = Tk.PhotoImage(file="cards.jfitz.gif")
    img = card.subimage(spritesheet, 0, 196, 73, 294)
    w.create_image(300, 200, image = img)"""
    
    """card_back = Tk.PhotoImage(file = "card_back.gif")
    w.create_image(200, 200, image = card_back)"""
    
    cb = draw_back(w, (200,100))
    
    Tk.mainloop()
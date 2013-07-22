# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Welcome to Blackjack. "
score = 0
total_games = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, 
                    CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                    CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        result = ""
        for card in self.cards:
            result += str(card)+","
        return result[:-1]
    
    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        has_ace = False
        value = 0
        for card in self.cards:
            has_ace = has_ace or card.rank == "A"
            value += VALUES[card.rank]
        if has_ace and value < 12:
            value += 10
        return value 
   
    def draw(self, canvas, pos):
        i = 0
        for card in self.cards:
            card.draw(canvas, [pos[0]+i*(CARD_SIZE[0]+10),pos[1]])
            i += 1
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        result = ""
        for card in self.cards:
            result += str(card)+","
        return result[:-1]


#define event handlers for buttons
def deal():
    global outcome, in_play, dealer, player, deck, score, total_games
    if total_games != 0:
        outcome = ""
    if in_play:
        outcome = "Player dealed again, lost a point. "
        score -= 1
        in_play = False
    dealer = Hand()
    player = Hand()
    deck = Deck()
    deck.shuffle()
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    in_play = True
    outcome += "New Game! Hit or Stand?"
    if in_play and player.get_value() == 21:
        stand()
    if in_play and dealer.get_value() == 21:
        stand()

def hit():
    global in_play, outcome, score, total_games
    if in_play and player.get_value() < 21:
        player.add_card(deck.deal_card())
        outcome = "Hit or Stand?"
    if in_play and player.get_value() == 21:
        stand()
    if in_play and player.get_value() > 21:
        outcome = "Player Busted!! Deal Again."
        score -= 1
        in_play = False
        total_games += 1
           
def stand():
    global in_play, score, outcome, total_games
    total_games += 1
    while in_play and dealer.get_value() < 17:
        dealer.add_card(deck.deal_card())
    if in_play:
        if dealer.get_value() > 21:
            outcome = "Dealer Busted!! Deal Again."
            score += 1
        elif dealer.get_value() >= player.get_value():
            outcome = "Dealer Wins!! Deal Again."
            score -= 1
        else:
            outcome = "Player Wins!! Deal Again."
            score += 1
        in_play = False
       
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

def draw_back_card(canvas, pos):
    canvas.draw_image(card_back, CARD_BACK_CENTER, 
                    CARD_BACK_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                    CARD_SIZE)
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", (190, 60), 50, "Black")
    canvas.draw_text("Dealer", (220, 240), 30, "Black")
    canvas.draw_text("Player", (220, 450), 30, "Black")
    canvas.draw_text(str(player.get_value()),(220,475),20,"Black")
    canvas.draw_text(outcome,(100, 500),20,"Black")
    canvas.draw_text("Score: "+str(score),(466, 540),20,"Black")
    canvas.draw_text("Games Played: "+str(total_games),(400, 560),20,"Black")
    player.draw(canvas, [50+CARD_SIZE[0], 310])
    dealer.draw(canvas, [50+CARD_SIZE[0], 100])
    if in_play:
        draw_back_card(canvas, [50+CARD_SIZE[0],100])
    else:
        canvas.draw_text(str(dealer.get_value()),(220, 265), 20, "Black")
    draw_back_card(canvas, [8,100])
    draw_back_card(canvas, [11,100])
    draw_back_card(canvas, [14,100])
    draw_back_card(canvas, [17,100])
    draw_back_card(canvas, [20,100]) 


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()
deal()

# remember to review the gradic rubric
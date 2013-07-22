"""Main BlackJack game module."""

#from Card import *  # It's imported in deck and hand
from Deck import *
from Hand import *
from bj_gui import *

# initialize some useful global variables
in_play = False
outcome = "Welcome to Blackjack. "
score = 0
total_games = 0

def deal():
    """Generates a new round. Deals a hand to the dealer and player.
    Checks if either hand is a BlackJack"""
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
    """Hits a card to the player if the game is on. Checks if the player busted."""
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
    """Player stand and hits the dealer until his hand reaches 17.
    Checks who wins the game"""
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

def console():
    """Main Blackjack game when played in console."""
    your_play = 'deal'
    while your_play != 'End':
        if your_play in ['deal', 'Deal']:
            deal()
            print "player", player, player.get_value()
            print "dealer", str(dealer).split(',')[-1]
            your_play = raw_input(outcome)
        elif in_play and your_play in ['hit', 'Hit']:
            while in_play and your_play in ['hit', 'Hit']: 
                hit()
                print "player", player, player.get_value()
                print "dealer", str(dealer).split(',')[-1]
                your_play = raw_input(outcome)
        elif in_play and your_play in ['stand', 'Stand']:
            stand()
            print "player", player, player.get_value()
            print "dealer", dealer, dealer.get_value()
            your_play = raw_input(outcome)
        else:
            your_play = raw_input('Wrong play. ' + outcome)

def g_update():
    my_gui.canvas.itemconfig(my_gui.T, text = outcome)
    my_gui.canvas.itemconfig(my_gui.S, text = "Score : " + str(score))
    my_gui.canvas.itemconfig(my_gui.P, text = "Player : " + str(player))
    my_gui.canvas.itemconfig(my_gui.D, text = "Dealer : " + str(dealer))
    
def g_deal():
    deal()
    g_update()
def g_hit():
    hit()
    g_update()
def g_stand():
    stand()
    g_update()
def gui():
    deal()
    global my_gui
    my_gui = App()
    my_gui.dealButton.config(command = g_deal)
    my_gui.hitButton.config(command = g_hit)
    my_gui.standButton.config(command = g_stand)
    g_update()
    my_gui.mainloop()
    

#console()
gui()
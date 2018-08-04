
from Utility import *
class DeckOfCards:
    utility = Utility()
    deck_arr = utility.deck_of_cards()
    print "Player 1 : "
    for j in range(0, 9):
        print deck_arr[j]

    print "\nPlayer 2 : "
    for j in range(9, 18):
        print deck_arr[j]

    print "\nPlayer 3 : "
    for j in range(18, 27):
        print deck_arr[j]

    print "\nPlayer 4 : "
    for j in range(27, 36):
        print deck_arr[j]
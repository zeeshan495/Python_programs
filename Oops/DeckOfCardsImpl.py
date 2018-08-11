
from DeckOfCards import *
from Utility import *
class DeckOfCardsImpl:

    cards_obj = DeckOfCards()
    deck_arr = cards_obj.deck_of_cards()
    index = 0
    new_arr = []
    for x in range(4):
        new_arr.append([])
        for y in range(9):
            new_arr[x].append(deck_arr[index])
            index += 1

    for x in range(4):
        for y in range(9):
            print(new_arr[x][y])
        print("\n")

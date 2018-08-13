
from Utility import *
class DeckOfCards:

    def deck_of_cards(self):
        suit_list = ["Clubs", "Diamonds", "Hearts", "Spades"]
        rank_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        deck_arr = [None] * 52

        #   storing total cards
        for i in range(0, len(rank_list)):
            for j in range(0, len(suit_list)):
                deck_arr[len(suit_list) * i + j] = str(rank_list[i])+ " of "+ str(suit_list[j])

        #   shuffling the cards
        for i in range(0, len(deck_arr)):
            rand = i + int(random.random() * (len(deck_arr) - i))
            temp = deck_arr[rand]
            deck_arr[rand] = deck_arr[i]
            deck_arr[i] = temp
        return deck_arr

        #   sorting for each person
    def sort_cards(self,deck_arr):
        char_arr = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '1', 'J', 'Q', 'K']
        index = 0
        sort_arr = []
        for column in range(4):
            sort_arr.append([])
            for x in range(len(char_arr)):
                for y in range(9):
                    temp = deck_arr[column][y][0]
                    if (char_arr[x] == temp):
                        sort_arr[column].append(deck_arr[column][y])
                        # index = index + 1
        return sort_arr


from DataStructures.QueueLinkedList import *
from DeckOfCards import *
from Utility import *
class ExtendDeck:
    utility = Utility()
    cards_obj = DeckOfCards()
    queue = QueueLinkedList()
    deck_arr = cards_obj.deck_of_cards()

    index = 0
    new_arr = []
    for x in range(4):
        new_arr.append([])
        for y in range(9):
            new_arr[x].append(deck_arr[index])
            index += 1

    sort_arr1 = cards_obj.sort_cards(new_arr)
    for x in range(4):
        queue.add_rear("  player : "+str(x+1))
        for y in range(9):
            queue.add_rear(sort_arr1[x][y])
        queue.add_rear("\n")

    queue.display()


    # sort_arr1 = utility.sort_cards(new_arr, 0)
    # print "Player 1 : "
    # for j in range(0, 9):
    #     queue1.add_rear(sort_arr1[j])
    # queue1.display()
    #
    # sort_arr2 = utility.sort_cards(new_arr, 1)
    # print "\nPlayer 2 : "
    # for j in range(0, 9):
    #     queue2.add_rear(sort_arr2[j])
    # queue2.display()
    #
    # sort_arr3 = utility.sort_cards(new_arr,2)
    # print "\nPlayer 3 : "
    # for j in range(0, 9):
    #     queue3.add_rear(sort_arr3[j])
    # queue3.display()
    #
    # sort_arr4 = utility.sort_cards(new_arr, 3)
    # print "\nPlayer 4 : "
    # for j in range(0,9 ):
    #     queue4.add_rear(sort_arr4[j])
    # queue4.display()

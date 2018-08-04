
from DataStructures.QueueLinkedList import *
from Utility import *
class ExtendDeck:
    utility = Utility()
    queue1 = QueueLinkedList()
    queue2 = QueueLinkedList()
    queue3 = QueueLinkedList()
    queue4 = QueueLinkedList()
    cards_arr = utility.deck_of_cards()

    sort_arr1 = utility.sort_cards(cards_arr, 0, 9)
    print "Player 1 : "
    for j in range(0, 9):
        queue1.add_rear(sort_arr1[j])
    queue1.display()

    sort_arr2 = utility.sort_cards(cards_arr, 10, 19)
    print "\nPlayer 2 : "
    for j in range(0, 9):
        queue2.add_rear(sort_arr2[j])
    queue2.display()
    #
    sort_arr3 = utility.sort_cards(cards_arr, 18, 27)
    print "\nPlayer 3 : "
    for j in range(0, 9):
        queue3.add_rear(sort_arr3[j])
    queue3.display()

    sort_arr4 = utility.sort_cards(cards_arr, 27, 36)
    print "\nPlayer 4 : "
    for j in range(0,9 ):
        queue4.add_rear(sort_arr4[j])
    queue4.display()










  #
  # char_arr = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '1', 'J', 'Q', 'K']
  #   index = 0
  #   sort_arr = [None] * 9
  #   for x in range(13):
  #       for y in range(10, 19):
  #           temp = cards_arr[y]
  #           if (char_arr[x] == temp[0]):
  #               sort_arr[index] = cards_arr[y]
  #               index = index + 1
  #   print(sort_arr)

from Utility import *
class InsertionSort:
    utility = Utility()
    while True:
        try:
            var_input = int(input("please enter a number of words "))
            break
        except NameError:
            print("please enter integer value")
    my_array = [None] * var_input
    print(" enter values ")
    for x in range(0, var_input):
        my_array[x] = raw_input()
    my_array.sort()
    sort_array = utility.insertion_sort(my_array)
    print("after insertion sort : ")
    for x in range(0, len(sort_array)):
        print(sort_array[x]),
    print("\n")
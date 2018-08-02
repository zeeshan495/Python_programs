
from Utility import *
class BubbleSort:
    utility = Utility()
    print("enter the number of words for bubble sort : ")
    var_input = utility.input_int_data()
    if (var_input <= 0):
        print("please check the input : ")
    else:
        my_array = [None] * var_input
        print(" enter values ")
        for x in range(0, var_input):
            my_array[x] = raw_input()
        my_array.sort()
        sort_array = utility.bubble_sort(my_array)
        print("after Bubble sort : ")
        for x in range(0, len(sort_array)):
            print(sort_array[x]),
        print("\n")
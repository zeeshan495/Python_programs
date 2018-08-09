
from Utility import *
class MergeSort:
    utility = Utility()
    print("enter the number of words for merge sort : ")
    var_input = utility.input_int_data()
    if (var_input <= 0):
        print("please check the input : ")
    else:
        my_array = [None] * var_input
        print(" enter values ")
        for x in range(0, var_input):
            my_array[x] = utility.input_int_data()

        sort_array = utility.merge_sort(my_array)
        print("after Merge sort : ")
        for x in range(0, len(sort_array)):
            print(sort_array[x]),
        print("\n")

from Utility import *
class BinarySearch:
    utility=Utility()
    print("enter the number of words for binary search : ")
    var_input = utility.input_int_data()
    if (var_input <= 0):
        print("please check the input : ")
    else:
        my_array=[None]*var_input
        print(" enter values ")
        for x in range(0,var_input):
            my_array[x]=raw_input()
        my_array.sort()
        print(" your array after sorting: ")
        for x in range(0,var_input):
            print(my_array[x]),
        print("\n")
        var_key = raw_input(" enter a key to search : ")
        utility.binary_search(my_array,0,len(my_array)-1,var_key)

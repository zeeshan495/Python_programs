
from Utility import *
class BinarySearch:
    utility=Utility()
    while True:
        try:
            var_input=int(input("please enter a number of words "))
            break
        except NameError :
            print("please enter integer value")
        except SyntaxError :
            print("please check the entered input")
    my_array=[None]*var_input
    print(" enter values ")
    for x in range(0,var_input):
        my_array[x]=raw_input()
    my_array.sort()
    print(" your array after sorting: ")
    for x in range(0,var_input):
        print(my_array[x]),
    print("\n")
    var_key=raw_input(" enter a key to search : ")
    utility.binary_search(my_array,0,len(my_array)-1,var_key)

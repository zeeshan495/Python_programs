
from Utility import *
class Triplets:
    utility=Utility()
    while True:
        try:
            print("enter the length of array : ")
            given_input = utility.input_int_data()
            if given_input > 0:
                break
            else:
                print("please enter a valid input")
        except NameError:
            print("please enter a number...try again")
    my_array = [None] * given_input
    utility.triplets(my_array)
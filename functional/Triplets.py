
from Utility import *
class Triplets:
    utility=Utility()
    while True:
        try:
            given_input = int(input(" enter the length of array : "))
            break
        except NameError:
            print("please enter a number...try again")
    my_array = [None] * given_input
    utility.triplets(my_array)
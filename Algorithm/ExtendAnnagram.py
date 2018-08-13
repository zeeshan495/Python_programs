
from Utility import *
class ExtendAnnagram:
    utility=Utility()
    try:
        print("to find annagram from prime numbers")
        print("please enter a range")
        var_input = utility.input_int_data()
        if var_input < 0:
            print("enter valid input")
        elif(var_input == 0) or (var_input == 1):
            print(" no prime numbers")
        result_array = utility.primenumber(var_input)
        utility.extend_annagram(result_array)
    except OverflowError :
        print("Overflow....please check the input")
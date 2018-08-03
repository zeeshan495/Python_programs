
from Utility import *
class ExtendPalindrome:
    utility=Utility()

    try:
        print("to find palindrome from prime numbers")
        print("please enter a range")
        var_input = utility.input_int_data()
        if (var_input == 0) or (var_input == 1):
            print(" no prime numbers")
        result_array = utility.primenumber(var_input)
        utility.palindrome(result_array)
    except OverflowError:
        print("Overflow....please check the input")

from Utility import *
class ExtendPalindrome:
    utility=Utility()
    while True:
        try:
            var_input = int(input("please enter a Nth Term "))
            break
        except NameError:
            print("please enter integer value")
    result_array = utility.primenumber(var_input)
    utility.palindrome(result_array)
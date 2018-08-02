
from Utility import *
import math
class GuessNumber:
    utility=Utility()
    while True:
        print("\nplease enter a number : ")
        var_input = utility.input_int_data()
        if(var_input <= 0):
            print("please check the input : ")
        else:
            try:
                var_range=int(math.pow(2,var_input))
                print(" think of a number between : "+str(var_range))
                var_result=utility.guessing(1,var_range)
                print(str(var_result)+" is a number ")
            except OverflowError :
                print("check the entered input, it was overflow")
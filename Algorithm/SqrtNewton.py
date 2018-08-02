
from Utility import *
class SqrtNewton:
    utility = Utility()
    while True:
        print("please enter a non-negative number ")
        var_input = utility.input_int_data()
        if(var_input <= 0):
            print("please check the entered number : ")
        else:
            var_result=utility.calculate_sqrt(var_input)
            break
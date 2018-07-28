
from Utility import *
class SqrtNewton:
    utility = Utility()
    while True:
        try:
            var_input = int(input("please enter a non-negative number "))
            if(var_input <= 0):
                print("please check the entered number : ")
            break
        except NameError:
            print("please enter integer value")

    var_result=utility.calculate_sqrt(var_input)
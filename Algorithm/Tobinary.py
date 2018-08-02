
from Utility import *
class Tobinary:
    utility = Utility()
    while True:
        print("please enter a decimal number ")
        var_input = utility.input_int_data()
        if(var_input < 0):
            print("please check the entered number : ")
        else:
            var_result=utility.to_binary(var_input)
            print(var_result)
            break
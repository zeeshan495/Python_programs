

from Utility import *
class Tobinary:
    utility = Utility()
    while True:
        print("please enter a decimal number ")
        var_input = utility.input_int_data()
        if (var_input < 0):
            print("please check the entered number : ")
        else:
            var_binary = utility.to_binary(var_input)
            print(var_binary)
            print("\n binary is : "+str(var_binary))
            var_swap_binary = utility.swap_nibbles(var_binary)
            print(" after swaping : "+str(var_swap_binary))
            var_result = utility.to_decimal(var_swap_binary)
            print(var_result)
            break

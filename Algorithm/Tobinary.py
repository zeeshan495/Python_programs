
from Utility import *
class Tobinary:
    utility = Utility()
    while True:
        try:
            var_input = int(input("please enter a decimal number "))
            if(var_input <= 0):
                print("please check the entered number : ")
            break
        except NameError:
            print("please enter integer value")
        except SyntaxError :
            print("please check the entered input")
    var_result=utility.to_binary(var_input)
    print(var_result)
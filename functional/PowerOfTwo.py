from Utility import *
class PowerOfTwo:
    while True:
        try :
            utility=Utility()
            input_number=int(input("Please enter a given input number : "))
            if(input_number==0):
                print(1)
            else:
                output_number=int(utility.power_value(input_number))
                print(output_number)
                break
        except NameError :
            print("please enter integer")
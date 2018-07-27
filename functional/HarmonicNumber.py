from Utility import *
class HarmonicNumber:
    while True:
        try:
            utility=Utility()
            input_number = int(input("Please enter a given input number : "))
            if (input_number > 0):
                utility.harmonic_func(input_number)

            else:
                print("please check the entered number")
            break
        except NameError :
            print("please enter integer")

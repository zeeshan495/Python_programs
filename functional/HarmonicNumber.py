from Utility import *
class HarmonicNumber:
    while True:
        try:
            utility=Utility()
            print("Please enter a given input number : ")
            input_number = utility.input_int_data()
            if (input_number > 0):
                utility.harmonic_func(input_number)
            else:
                print("please check the entered number")
        except NameError :
            print("please enter integer")
        except OverflowError :
            print("given number is very high...try again")
        except SyntaxError :
            print("check the given input and try again")

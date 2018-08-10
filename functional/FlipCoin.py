from Utility import *
class FlipCoin:
    while True:
        try:
            utility = Utility()
            print("Please the number of times to Flip Coin ")
            number_of_times = utility.input_int_data()
            if (number_of_times >= 0):
                utility.flip(number_of_times)
            else:
                print("please enter positive number")
        except ValueError :
            print("invalid input")
        except OverflowError:
            print("OverflowError")
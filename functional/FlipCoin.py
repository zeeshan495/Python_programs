from Utility import *
class FlipCoin:
    while True:
        try:
            obj=Utility()
            number_of_times = int(raw_input("Please the number of times to Flip Coin "))
            obj.flip(number_of_times)
            break
        except ValueError :
            print("invalid input")

from Utility import *
class CouponNumber:
    utility = Utility()
    while True:
        try:
            given_input = int(input(" enter the number of coupon to generate : "))
            break
        except NameError :
            print("please enter a number...try again")
    utility.random_number(given_input)
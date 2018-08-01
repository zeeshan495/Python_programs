
from Utility import *
class CouponNumber:

        utility = Utility()
        print(" enter the number of coupon to generate : ")
        given_input = utility.input_int_data()
        utility.random_number(given_input)
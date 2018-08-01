
from Utility import *
class Distance:
    utility=Utility()
    while True:
        try:
            # var_x=int(input("please enter x value : "))
            # var_y=int(input("please enter y value : "))
            print("please enter x value : ")
            var_x = utility.input_int_data()

            print("please enter y value : ")
            var_y = utility.input_int_data()
            break
        except NameError :
            print("OOps....please enter integer values ")
    utility.distance(var_x,var_y)
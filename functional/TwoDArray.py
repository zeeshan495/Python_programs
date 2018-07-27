from Utility import *
class TwoDArray:
    utility=Utility()
    while True:
        while True:
            try:
                choice=int(input("please enter a choice :\n 1 for int\n 2 for boolean\n 3 for float"))
                if(choice==1):
                    utility.twod_int_array()
                elif(choice==2):
                    utility.twod_boolean_array()
                else:
                    utility.twod_float_array()
                break
            except NameError :
                print("please enter a number...try again")
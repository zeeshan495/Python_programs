
from Utility import *
import math
class GuessNumber:
    utility=Utility()
    while True:
        try:
            var_input=int(input("please enter a number "))
            break
        except NameError :
            print("please enter integer value")
    var_range=int(math.pow(2,var_input))
    print(" think of a number between : "+str(var_range))
    var_result=utility.guessing(0,var_range)
    print(str(var_result)+" is a number ")
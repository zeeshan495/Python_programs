
from Utility import *
class MergeSort:
    utility = Utility()
    while True:
        try:
            var_input = int(input("please enter amount "))
            break
        except NameError:
            print("please enter integer value")

    var_result=utility.counting_notes(var_input)
    print("Total notes "+str(var_result))
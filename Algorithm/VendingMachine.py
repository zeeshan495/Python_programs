
from Utility import *
class MergeSort:
    utility = Utility()
    print("enter the amount : ")
    var_input = utility.input_int_data()
    if (var_input <= 0):
        print("please check the input")
    else:
        var_result=utility.counting_notes(var_input)
        print("Total notes "+str(var_result))
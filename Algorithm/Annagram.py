
from Utility import *
class Annagram:
    utility=Utility()
    var_str_1=raw_input("please enter first string : ")
    var_str_2 = raw_input("please enter second string : ")

    var_result = utility.annagram(var_str_1,var_str_2)
    if(var_result):
        print("it is a annagram ")
    else:
        print("it is not a annagram ")


from Utility import *
class Permutations:
    utility=Utility()
    print("please enter the String : ")
    var_str = utility.input_str_data()
    var_len=len(var_str)
    utility.permute(var_str, 0, var_len-1)

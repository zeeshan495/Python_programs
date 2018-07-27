

from Utility import *
class Permutations:
    utility=Utility()

    var_str = raw_input("please enter the String : ")
    var_len=len(var_str)
    utility.permute(var_str,0,var_len)
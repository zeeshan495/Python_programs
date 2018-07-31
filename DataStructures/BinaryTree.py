
from Utility import *
class BinaryTree:
    utility = Utility()
    print("enter no of test cases : ")
    test_cases = utility.input_int_data()
    print("enter a number : ")
    for x in range(0, test_cases):
        var_number = utility.input_int_data()
        var_result = utility.catalan(var_number)
        print(var_result)
    print("***completed***")


from Utility import *
class BinaryTree:
    utility = Utility()
    var_res = utility.factorial(40)
    print(type(var_res))
    print(var_res)

    print("enter no of test cases : ")
    test_cases = utility.input_int_data()
    print("enter a number : ")
    for x in range(0, test_cases):
        var_number = utility.input_int_data()
        var_result = utility.catalan(var_number)
        print(var_result)
    print("***completed***")

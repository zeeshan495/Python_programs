

from Stack import *
from Utility import *
class BalancedParanthesis:
    utility = Utility()
    stack = Stack()
    # var_input = "((5+6)*(7+8)/(4+3)(5+6)*(7+8)/(4+3))"
    print("please enter expression")
    var_input = utility.input_str_data()
    my_array = list(var_input)
    open_para = "("
    close_para = ")"
    for x in range(0 ,len(my_array)):
        if(my_array[x] == open_para)  :
            stack.push(my_array[x])
        elif(my_array[x] == close_para)  :
            result = stack.pop()
            if(result == 0):
                print(" Unbalanced paranthesis..... ")
                exit(0)

    flag1 = stack.is_empty()
    if (flag1):
        pass
        # print("Balanced Paranthesis '()'")
        # exit(0)
    else:
        print("Unbalanced Paranthesis '()'")
        exit(0)

    for x in range(0 ,len(my_array)):
        if (my_array[x] == "{") :
            stack.push(my_array[x])
        elif (my_array[x] == "}") :
            result = stack.pop()
            if(result == 0):
                print(" Unbalanced paranthesis..... ")
                exit(0)

    flag2 = stack.is_empty()
    if(flag2):
        pass
        # print("Balanced Paranthesis '{}'")
    else:
        print("Unbalanced Paranthesis '{}'")


    for x in range(0 ,len(my_array)):
        if (my_array[x] == "[") :
            stack.push(my_array[x])
        elif (my_array[x] == "]") :
            result = stack.pop()
            if(result == 0):
                print(" Unbalanced paranthesis..... ")
                exit(0)

    flag3 = stack.is_empty()
    if(flag3) and flag1 and flag2:
        print("Balanced Paranthesis ")
    else:
        print("Unbalanced Paranthesis ")

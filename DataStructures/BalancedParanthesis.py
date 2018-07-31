

from Stack import *
class BalancedParanthesis:

    stack = Stack()

    var_input = "((5+6)*(7+8)/(4+3)(5+6)*(7+8)/(4+3))"
    my_array = list(var_input)
    open_para = "("
    close_para = ")"
    for x in range(0 ,len(my_array)):
        if(my_array[x] == open_para):
            stack.push(my_array[x])
        elif(my_array[x] == close_para):
            result = stack.pop()
            if(result == 0):
                print(" Unbalanced paranthesis..... ")
                exit(0)

    flag = stack.is_empty()
    if(flag):
        print("Balanced Paranthesis ")
    else:
        print("Unbalanced Paranthesis ")

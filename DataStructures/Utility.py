
from LinkedList import *
class Utility:

    def print_list(self,f,head):
        file = open(f,"w+")
        if(head is None):
            print("it is empty")
        elif (head.next_node is None):
            file.write(head.data),
            file.write(" ")
        else:
            while(head != None):
                file.write(head.data)
                file.write(" ")
                head = head.next_node

    def input_int_data(self):
        while True:
            try:
                var_input = int(input())
                return var_input
                break
            except NameError:
                print("please enter a integer...try again")


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

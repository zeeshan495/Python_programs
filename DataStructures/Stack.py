
from Node import *
class Stack:
    size = 0
    def __init__(self):
        self.head = None

    def push(self,data):
        obj_node = Node.data
        if(self.head == None):
            self.head = obj_node
            size = size + 1
        else:
            temp = obj_node
            temp.next_node = self.head
            self.head = temp
            size = size + 1

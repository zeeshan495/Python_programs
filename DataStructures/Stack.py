
from Node import *
class Stack:

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,data):
        obj_node = Node(data)
        if(self.head == None):
            self.head = obj_node
            self.size = self.size + 1
        else:
            temp = obj_node
            temp.next_node = self.head
            self.head = temp
            self.size = self.size + 1

    def pop(self):
        temp = self.head
        result = None
        if(temp == None):
            print("stack is empty ")
            return 0
        else:
            self.head = temp.next_node
            self.size = self.size - 1
        return temp.data

    def search(self,key):
        temp = self.head
        var_x = 0
        while(temp != None):
            if(temp.data == key):
                return x
            temp = temp.next_node
            var_x = var_x + 1
        return -1

    def display(self):
        temp = self.head
        while(temp.next_node != None):
            print(str(temp.data)+" "),
            temp = temp.next_node
        print(temp.data)

    def is_empty(self):
        if(self.head == None):
            return True
        else:
            return False

    def size(self):
        return self.size
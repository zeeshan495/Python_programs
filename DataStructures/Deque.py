
from Node import *

class Deque:

    def __init__(self):
        self.head = None

    def add_rear(self,data):
         obj_node=Node(data)
         if(self.head == None):
            self.head=obj_node
         else:
             temp = self.head
             while(temp.next_node != None):
                 temp = temp.next_node
             temp.next_node=obj_node

    def add_front(self,data):
        obj_node = Node(data)
        if (self.head == None):
            self.head = obj_node
        else:
            obj_node.next_node = self.head
            self.head = obj_node

    def remove_rear(self):
        temp = self.head
        if(temp == None):
            print("it is empty ")
        elif(temp.next_node == None):
            self.head = None
        else:
            while (temp.next_node != None):
                temp = temp.next_node
            temp.next_node = None

    def remove_front(self):
        temp = self.head
        if(temp == None):
            print("it is empty ")
        else:
            self.head = temp.next_node
            temp = None

    def pop_rear(self):
        temp = self.head
        if (temp == None):
            print("it is empty rear")
            return False
        elif (temp.next_node == None):
            result = temp
            self.head = None
        else:
            while (temp.next_node.next_node != None):
                temp = temp.next_node
            result = temp.next_node
            temp.next_node = None
        return  result.data

    def pop_front(self):
        temp = self.head
        if(temp == None):
            print("it is empty front")
            return False
        else:
            result = self.head
            self.head = temp.next_node
            temp = None
        return result.data

    def operation(self):
        temp = self.head
        if(temp == None) or (temp.next_node == None):
            print("it's a palindrome ")
            exit(0)
        front_elem = self.pop_front()
        rear_elem = self.pop_rear()
        if(front_elem == rear_elem):
            self.operation()
        else:
            print("it's not a palindrome ")

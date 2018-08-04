
from Node import *
class QueueLinkedList:
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

    def remove_front(self):
        temp = self.head
        if(temp == None):
            print("it is empty ")
        else:
            self.head = temp.next_node
            temp = None

    def display(self):
        temp = self.head
        while(temp != None):
            print temp.data
            temp = temp.next_node
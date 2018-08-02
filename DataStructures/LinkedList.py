
from Node import *

class LinkedList:
    def __init__(self):
        self.head=None

    def add(self,data):
         obj_node=Node(data)
         if(self.head == None):
            self.head=obj_node
         else:
             temp = self.head
             while(temp.next_node != None):
                 temp = temp.next_node
             temp.next_node=obj_node

    def delete(self,data):
        temp = self.head
        prev = None

        if temp is None:
            print(" it is empty ")
        elif (temp.data == data):
            temp = self.head
            self.head = temp.next_node
            temp = None
        else:
            temp2 = self.head
            while(temp2 != None):
                if temp2.data == data :
                    prev.next_node = temp2.next_node
                    temp2 = None
                    break
                else:
                    prev = temp2
                    temp2 = temp2.next_node


    def search(self,data):
        temp = self.head
        while(temp != None):
            if (temp.data == data):
                return True
            temp = temp.next_node
        return False

    def display(self):
        temp = self.head
        while(temp != None):
            print temp.data
            temp = temp.next_node

    def add_order(self,data):
        try:
            obj_node = Node(data)
            temp_node = None
            temp = self.head
            key = int(data)
            temp_data = int(temp.data)

            if (self.head == None):
                self.head = obj_node
            elif(temp_data > key):
                temp_node = obj_node
                temp_node.next_node = temp
                self.head = obj_node
            else:
                while (temp.next_node != None):
                    temp_data = int(temp.data)
                    temp_node_data = int(temp.next_node.data)
                    if(temp_data < key and temp_node_data > key):
                        temp_node = obj_node
                        temp_node.next_node = temp.next_node
                        temp.next_node = temp_node
                        break
                    temp = temp.next_node
                temp.next_node = obj_node
        except ValueError :
            print("value error...please check the input")

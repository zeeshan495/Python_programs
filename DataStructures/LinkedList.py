
from Node import *
from Utility import *
class LinkedList:
    global utility
    utility = Utility()
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
        temp2 = None
        if temp is None:
            print(" it is empty ")
        elif (temp is data):
            temp2 = temp
            temp = temp.next_node
        else:
            temp2 = temp
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

    def operation(self,my_array, new_word, file):
        for x in range(0, len(my_array)):
            self.add(my_array[x])
        flag=self.search(new_word)
        print(" flag ",flag)
        if (flag == False):
            self.add(new_word)
        else:
            self.delete(new_word)
        self.display()
        node=self.head
        utility.print_list(file,node)

    def operation_order(self, my_array, new_word, file):
        for x in range(0, len(my_array)):
            self.add(my_array[x])
        flag = self.search(new_word)
        if (flag == False):
            self.add_order(new_word)
        else:
            self.delete(new_word)
        self.display()
        node = self.head
        utility.print_list(file, node)

    def add_order(self,data):
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
                print(" temp.data " + str(temp_data))
                if(temp_data < key and temp_node_data > key):
                    temp_node = obj_node
                    temp_node.next_node = temp.next_node
                    temp.next_node = temp_node
                    break
                temp = temp.next_node
            temp.next_node = obj_node

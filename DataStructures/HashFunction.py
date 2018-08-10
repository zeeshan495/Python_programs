
from Node import *
class HashFunction:
    table = None
    size = None

    def __init__(self):
        self.head = None
        self.size = 0
        self.table = [None]*10

    def insert(self,value):
        self.size += 1
        position = self.table_position(value)
        obj_node = Node(value)
        if(self.table[position] == None):
            self.table[position] = obj_node
        else:
            obj_node.next_node = self.table[position]
            self.table[position] = obj_node

    def table_position(self,hash_value):
        hash_value = hash_value % len(self.table)
        return hash_value


    def delete(self, data):
        position = self.table_position(data)
        temp = self.table[position]
        prev = None

        if temp is None:
            print(" it is empty ")
        elif (temp.data == data):
            prev = temp
            temp = temp.next_node
            self.table[position] = temp
            prev = None
            return
        else:
            temp2 = self.head
            while (temp2 != None):
                if temp2.data == data:
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
        for x in range(len(self.table)):
            print(str(x)+" : "),
            temp = self.table[x]
            while (temp != None):
                print temp.data,
                temp = temp.next_node
            print("\n")

    def print_list(self,f,head):
        file = open(f,"w+")
        if(head is None):
            print("it is empty")
        # elif (head.next_node is None):
        #     file.write(head.data),
        #     file.write(" ")
        else:
            while(head != None):
                file.write(str(head.data)+" ")
                head = head.next_node
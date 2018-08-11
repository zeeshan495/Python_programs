
import json
import os
class DataManage:

        file_name = None

        def __init__(self,file_name):
            self.file_name = file_name

        def read(self):
            try:
                f = open("/home/bridgeit/Zeeshan_Python/JsonFiles/"+str(self.file_name)+".json","r")
                self.inventory = json.load(f)
                print("\tsuccessfully read")
            except IOError:
                print("can't read a file")

        def display(self):
            print("\tdisplaying inventory details of "+str(self.file_name))
            try:
                for x in self.inventory:
                        print("Name " + str(self.inventory[x]["Name"]))
                        print("price "+str(self.inventory[x]["price"]))
                        print("weight " + str(self.inventory[x]["weight"]))
                        print("Total Price " + str(self.inventory[x]["weight"]*self.inventory[x]["price"]))
                        print("\n")
            except AttributeError:
                print("can't display")

class DataManageImpl:
    obj = DataManage("shubham")
    obj.read()
    obj.display()

    obj = DataManage("nikhil")
    obj.read()
    obj.display()

    obj = DataManage("abc")
    obj.read()
    obj.display()

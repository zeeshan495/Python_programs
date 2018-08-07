
from AddressBookManager import *
from Oops.Utility import *
from AddressBookImplementation import *
import json
import os.path
class ManagerImplementation(AddressBookManager):

    utility = Utility()
    bookImplent = AddressBookImplementation()


    def create(self):
        print("enter the name of the address book : ")
        new_address_book = self.utility.input_str_data()
        if(os.path.exists("/home/bridgeit/Zeeshan_Python/AddressJson/"+new_address_book + ".json")):
            print("already exists : ")
        else:
            f = open("/home/bridgeit/Zeeshan_Python/AddressJson/"+new_address_book + ".json", "w+")
            print("successfully created")

    def read_files(self):
        path = "/home/bridgeit/Zeeshan_Python/AddressJson"
        dirs = os.listdir(path)
        for files in dirs:
            print(files)

    def operation(self):
        self.bookImplent.operation()



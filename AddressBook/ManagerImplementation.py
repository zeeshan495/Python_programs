

from AddressBookManager import *
from Oops.Utility import *
class ManagerImplementation(AddressBookManager):

    utility = Utility()
    def create(self):
        print("enter the name of the address book : ")
        new_address_book = self.utility.input_str_data()



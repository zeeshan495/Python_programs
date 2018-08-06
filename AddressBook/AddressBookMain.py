
from Oops.Utility import *
from ManagerImplementation import *
class AddressBookMain:

    manager = ManagerImplementation()
    utility = Utility()
    menu = True
    address_book = AddressBookImplementation()
    while menu:
        print("\t_____________________________________________\n")
        print("\t\t\tADDRESS BOOK")
        print("\t_____________________________________________\n")
        print("\t1. Create new Address Book")
        print("\t2. Open existing Address Book")
        print("\t3. Close Address Book")
        choice = utility.input_int_data()

        if (choice == 1):
            manager.create()
        elif choice == 2:
            manager.read_files()
            manager.operation()
        elif choice == 3:
            print("closed")
            break
            
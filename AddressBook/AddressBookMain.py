
from Oops.Utility import *
class AddressBookMain:

    utility = Utility()
    menu = True
    while menu:
        print("\t_____________________________________________\n")
        print("\t\t\tADDRESS BOOK")
        print("\t_____________________________________________\n")
        print("\t1. Create new Address Book")
        print("\t2. Open existing Address Book")
        print("\t3. Save As Address Book")
        print("\t4. Close Address Book")
        choice = utility.input_int_data()
        if choice == 1:
            
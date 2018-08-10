

from Oops.Utility import *
from CommercialDataProcessing.controller.StockImplementation import *
class StockMain:
    utility = Utility()
    print("\t\t_____________________________________________\n")
    print("\t\t\t***Welcome to our stock account***\n")
    def stock_account(self):
        company_list = {}
        customer_list = {}
        stock_obj1 = StockImplementation()
        # new_company_list = stock_obj1.read(Companies)
        # new_customer_list = stock_obj1.read("Customers")
        # stock_obj2 = StockImplementation(new_customer_list)

        while True:
            print("\t_____________________________________________\n")
            print("\t\t\tSTOCK ACCOUNT");
            print("\t_____________________________________________\n")
            print("\t1.	add customer")
            print("\t2.	add company")
            print("\t3.	transactions")
            print("\t4. 	display companies")
            print("\t5. 	display customers")
            print("\t6. 	display Transaction")
            print("\t7. 	to exit")
            choice = self.utility.input_int_data()
            if choice == 1:
                stock_obj1.add_customer()
            elif choice == 2:
                stock_obj1.add_company()
            elif choice == 3:
                stock_obj1.buy_sell_share()
            elif choice == 4:
                stock_obj1.display_companies()
            elif choice == 5:
                stock_obj1.display_customers()
            elif choice == 6:
                stock_obj1.display_transaction()
            elif choice == 7:
                print("Thank You")
                break
            else:
                print("invalid choice")
stock = StockMain()
stock.stock_account()
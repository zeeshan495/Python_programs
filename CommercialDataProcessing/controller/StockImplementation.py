
from CommercialDataProcessing.model.Companies import *
from CommercialDataProcessing.model.Customer import *
from CommercialDataProcessing.model.Transaction import *
from CommercialDataProcessing.controller.LinkedList import *
from CommercialDataProcessing.controller.QueueLinkedList import *
from CommercialDataProcessing.controller.Stack import *
from Oops.Utility import *
from datetime import *
import json
import os
class StockImplementation:
    __company_list = []
    __customer_list = {}
    utility = Utility()
    list_obj = None
    stack_obj = None
    queue_obj = None

    def __init__(self):
        self.list_obj = LinkedList()
        self.stack_obj = Stack()
        self.queue_obj = QueueLinkedList()
        self.read_companies()
        self.__customer_list = self.read_customers("Customers")

    def read_companies(self):
        path_name = "/home/bridgeit/Zeeshan_Python/stockJson/Companies.json"
        if (os.stat(path_name).st_size != 0):
            f = open(path_name, "r")
            data = json.load(f)
            for x in range(0,len(data)):
                self.list_obj.add(data[x])

    def read_transactions(self):
        path_name = "/home/bridgeit/Zeeshan_Python/stockJson/Transaction.json"
        if (os.stat(path_name).st_size != 0):
            f = open(path_name, "r")
            data = json.load(f)
            for x in range(0,len(data)):
                self.queue_obj.add(data[x])


    def read_customers(self, file_name):
        my_list = {}
        path_name = "/home/bridgeit/Zeeshan_Python/stockJson/" + file_name + ".json"
        if (os.stat(path_name).st_size != 0):
            f = open(path_name, "r")
            data = json.load(f)
            for x in data:
                if x in my_list:
                    my_list[x].append(data[x])
                else:
                    my_list[x] = data[x]
        return my_list

    def add_company(self):
        var_company_details = self.company_info()
        self.list_obj.add({"company_name":var_company_details.get_company_name(),"company_symbol":var_company_details.get_company_symbol(),
                                    "share_price":var_company_details.get_share_price(),"total_shares":var_company_details.get_total_shares(),
                                    "time":var_company_details.get_time()})
        print("successfully added")
        self.save("Companies",self.list_obj)

    def company_info(self):
        company = Companies()
        print("Enter a company name : ")
        company.set_company_name(self.utility.input_str_data())
        print("Enter a company symbol : ")
        company.set_company_symbol(self.utility.input_str_data())
        print("Enter a share price : ")
        company.set_share_price(self.utility.input_int_data())
        print("Enter a total shares : ")
        company.set_total_shares(self.utility.input_int_data())
        date = datetime.now()
        company.set_time(str(date)[:10])
        return company

    def add_customer(self):
        var_customer_info = self.customer_info()
        if var_customer_info.get_name() in self.__customer_list:
            self.__customer_list[var_customer_info.get_name()].append(
                {"customer_name": var_customer_info.get_name(), "amount": var_customer_info.get_amount(),
                 "no_of_shares": var_customer_info.get_no_of_shares()})
        else:
            self.__customer_list[var_customer_info.get_name()] = {"customer_name":var_customer_info.get_name(),"amount":var_customer_info.get_amount(),
                                     "no_of_shares":var_customer_info.get_no_of_shares()}
        print("successfully added")
        self.save_customers("Customers",self.__customer_list)

    def customer_info(self):
        customer = Customer()
        print("Enter a customer name : ")
        customer.set_name(self.utility.input_str_data())
        print("Enter a amount : ")
        customer.set_amount(self.utility.input_int_data())
        print("Enter no of shares : ")
        customer.set_no_of_shares(self.utility.input_int_data())
        return customer

    def display_companies(self):
        new_list = self.list_obj.get_data()
        print("\tCompanies")
        for x in range(len(new_list)):
            print("company name\t:\t"+str(new_list[x]["company_name"]))
            print("company symbol\t:\t"+str(new_list[x]["company_symbol"]))
            print("total shares\t:\t"+str(new_list[x]["total_shares"]))
            print("share price\t:\t" + str(new_list[x]["share_price"]))
            print("\n")

    def display_customers(self):
        for x in self.__customer_list:
            print("name\t\t:\t"+str(self.__customer_list[x]["customer_name"]))
            print("amount\t\t:\t" + str(self.__customer_list[x]["amount"]))
            print("no of shares:\t" + str(self.__customer_list[x]["no_of_shares"]))
            print("\n")

    def display_transaction(self):
        self.queue_obj.display()

    def save(self, file_name, obj):
        my_list = obj.get_data()
        print(my_list)
        data = json.dumps(my_list)
        print(file_name)
        print(my_list)
        with open("/home/bridgeit/Zeeshan_Python/stockJson/"+file_name+".json", 'w') as f:
            f.write(data)

    def save_customers(self, file_name, my_list):
        data = json.dumps(my_list)
        print(file_name)
        print(my_list)
        with open("/home/bridgeit/Zeeshan_Python/stockJson/"+file_name+".json", 'w') as f:
            f.write(data)

    def buy_share(self):
        print("enter symbol of company : ")
        company_symbol = self.utility.input_str_data()
        particular_company = self.search_company(company_symbol)
        if particular_company == False:
            print("company not found for given input")
        else:
            print(particular_company["company_name"])
            print("enter a customer name : ")
            customer_detail = self.utility.input_str_data()
            particular_customer = self.search_customer(customer_detail)
            if particular_customer == False:
                print("customer not found for given input")
            else:
                print(particular_customer)
                print("enter amount to buy a shares : ")
                var_amount = self.utility.input_int_data()
                self.buy(var_amount, particular_company, particular_customer)


    def search_company(self,details):
        new_list = self.list_obj.get_data()
        for x in range(len(new_list)):
            if details == new_list[x]["company_symbol"]:
                return new_list[x]
        return False

    def search_customer(self,details):
        for x in self.__customer_list:
            if(self.__customer_list[x]["customer_name"] == details):
                return self.__customer_list[x]
        return False

    def buy(self, var_amount, particular_company, particular_customer):
        if var_amount <= particular_customer["amount"]:
            print("amount sufficient")
            price_per_share = particular_company["share_price"]
            shares = var_amount/price_per_share
            if(particular_company["total_shares"] >= shares):
                transaction = Transaction()
                transaction.set_buy_sell("buy")
                transaction.set_customer_name(particular_customer["customer_name"])
                transaction.set_customer_symbol(particular_company["company_symbol"])
                transaction.set_total_price(var_amount)
                transaction.set_total_shares(shares)
                date = datetime.now()
                transaction.set_time(str(date)[:10])
                self.queue_obj.add_rear({"customer_name":transaction.get})
                self.save("Transaction", self.queue_obj)



            else:
                print("customer had insufficient shares")

        else:
            print("customer had a insufficient balance")
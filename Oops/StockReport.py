

import json
from Utility import *
class StockReport:
    __file_name = None
    utility = Utility()
    def __init__(self, file_name):
        self.__file_name = file_name

    def read(self):
        try:
            f = open("/home/bridgeit/Zeeshan_Python/JsonFiles/" + str(self.__file_name) + ".json", "r")
            self.stock = json.load(f)
            print("\tsuccessfully read")
        except IOError:
            print("can't read a file")

    def display(self):
        print("\tdisplaying inventory details of " + str(self.__file_name))
        try:
            for x in self.stock:
                print("Company : " + str(self.stock[x]["Name"]))
                print("price Per Stock " + str(self.stock[x]["pricePerStock"]))
                print("enter a number of stocks : ")
                no_of_stocks = self.utility.input_int_data()
                print("total Stocks " + str(no_of_stocks))
                print("Total Price " + str(no_of_stocks * self.stock[x]["pricePerStock"]))
                print("\n")
        except AttributeError:
            print("can't display")

class StockReportImpl:
    obj = StockReport("StockReport")
    obj.read()
    obj.display()

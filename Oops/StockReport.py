

import json
class DataManage:

        f = open("/home/bridgeit/Zeeshan_Python/JsonFiles/StockReport.json","r")
        # s = f.read()
        # print(s)
        stock = json.load(f)
        # print(inventory)
        # print(type(s))
        # print(type(inventory))
        for x in stock:
            # for y in inventory[x]:
                print("Name " + str(stock[x]["Name"]))
                print("price Per Stock "+str(stock[x]["pricePerStock"]))
                print("total Stocks " + str(stock[x]["totalStocks"]))
                print("Total Price " + str(stock[x]["totalStocks"]*stock[x]["pricePerStock"]))
                print("\n")
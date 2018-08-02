
import json
class DataManage:
    # data = json.load(open("DataManagment.json","r"))
    data = json.load(open("DataManagment.json", "r"))
    mylist = list(data["user"])
    # print(mylist)
    # print(data["Inventory"])

    # print("Name : "+str(data["Inventory"]["Name"]))
    # print("price : " + str(data["Inventory"]["price"]))
    # print("weight : " + str(data["Inventory"]["weight"]))
    for x in mylist:
        print(x)
    #
    # for x in data:
    #     print x
    # for x in range(3):
    #     print(data["Inventory"][x] )
    #
    # print(data[0])
    # print(data["Inventory"]["Name"])

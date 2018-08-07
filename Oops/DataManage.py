
import json
class DataManage:

        f = open("/home/bridgeit/Zeeshan_Python/JsonFiles/DataManagment.json","r")
        # s = f.read()
        # print(s)
        inventory = json.load(f)
        # print(inventory)
        # print(type(s))
        # print(type(inventory))
        print(inventory["1"])
        for x in inventory:
            # for y in inventory[x]:
                print("Name " + str(inventory[x]["Name"]))
                print("price "+str(inventory[x]["price"]))
                print("weight " + str(inventory[x]["weight"]))
                print("Total Price " + str(inventory[x]["weight"]*inventory[x]["price"]))
                print("\n")
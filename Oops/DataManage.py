
import json
class DataManage:

        f = open("/home/bridgeit/Zeeshan_Python/JsonFiles/DataManagment.json","r")
        # s = f.read()
        # print(s)
        inventory = json.load(f)
        # print(inventory)
        # print(type(s))
        # print(type(inventory))
        for x in inventory:
            # for y in inventory[x]:
                print("price "+str(inventory[x]["price"]))
                print("Name " + str(inventory[x]["Name"]))
                print("weight " + str(inventory[x]["weight"]))
                print("\n")
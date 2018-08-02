
import json

class Demo:
    data = json.load(open("DataManagment.json","r"))
    data["Inventory"]["price"] = 30
    print(data)
    with open("DataManagment.json", "w") as abc:
        json.dump(data,abc)
    
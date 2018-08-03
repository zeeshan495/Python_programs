import json
from Utility import *
from Product import *


class ExtendDataManage:
    global utility
    utility = Utility()

my_list = {}

def main():
    while True:
        print("\tenter a choice : ")
        print("1 for rice\n2 for pulses\n3 for wheat\n4 for stop\n")
        choice = utility.input_int_data()
        if (choice == 1):
            name = "rice"

        elif (choice == 2):
            name = "pulses"

        elif (choice == 3):
            name = "wheat"

        elif (choice == 4):
            print("Sucessfully saved")
            calculation()
            exit(0)
        else:
            print("invalid choice")
            break
        info = add(name)

        my_list[info.get_name()] = {"price": info.get_price(), "type": info.get_type(), "weight": info.get_weight()}

        save()


def add(name):
    print("enter the type of " + str(name))
    type = utility.input_str_data()
    print("enter the price of " + str(name))
    price = utility.input_int_data()
    print("enter the weight of " + str(name))
    weight = utility.input_int_data()
    obj = Product(name, type, price, weight)
    return obj


def save():
    data = json.dumps(my_list)
    with open("/home/bridgeit/Zeeshan_Python/JsonFiles/extendDataManage.json", 'w') as f:
        f.write(data)

def calculation():
    for x in my_list:
        print(my_list[x])
        print("type : "+str(my_list[x]["type"])+"\n"),
        print("price : " + str(my_list[x]["price"]) + "\n"),
        print("weight : " + str(my_list[x]["weight"]) + "\n"),
        print("Total Price of "+str(my_list[x]["type"])+" : " + str(my_list[x]["price"]*my_list[x]["weight"]) + "\n"),
        print("\n")

main()


import json
from Utility import *
from Product import *

class ExtendDataManage():

    utility = Utility()
    my_list = {}
    __file_name = None

    def __init__(self,file_name):
        self.__file_name = file_name

    def main_func(self):
        choice_list = ["rice", "pulses", "wheat"]
        while True:
            print("\tenter a choice : ")
            print("1 for rice\n2 for pulses\n3 for wheat\n4 for stop\n")
            choice = self.utility.input_int_data()
            if choice < 4 and choice > 0:
                name = choice_list[choice-1]
            elif (choice == 4):
                print("Sucessfully saved")
                self.calculation()
                exit(0)
            else :
                print("invalid choice")
                break
            product_info = self.add(name)

            if product_info.get_name() in self.my_list:
                self.my_list[product_info.get_name()].append({"price": product_info.get_price(), "type": product_info.get_type(), "weight": product_info.get_weight()})
            else:
                self.my_list[product_info.get_name()] = [{"price": product_info.get_price(), "type": product_info.get_type(), "weight": product_info.get_weight()}]

            self.save()

    def add(self, name):
        product_info = Product()
        product_info.set_name(name)
        print("enter the type of " + str(name))
        product_info.set_type(self.utility.input_str_data())
        print("enter the price of " + str(name))
        product_info.set_price(self.utility.input_int_data())
        print("enter the weight of " + str(name))
        product_info.set_weight(self.utility.input_int_data())

        return product_info

    def save(self):
        data = json.dumps(self.my_list)
        with open("/home/bridgeit/Zeeshan_Python/JsonFiles/"+str(self.__file_name)+".json", 'w') as f:
            f.write(data)

    def calculation(self):
        for x in self.my_list:
            for y in range(0,len(self.my_list[x])):
                print("type : "+str(self.my_list[x][y]["type"])+"\n"),
                print("price : " + str(self.my_list[x][y]["price"]) + "\n"),
                print("weight : " + str(self.my_list[x][y]["weight"]) + "\n"),
                print("Total Price of "+str(self.my_list[x][y]["type"])+" : " + str(self.my_list[x][y]["price"] * self.my_list[x][y]["weight"]) + "\n"),
                print("\n")

class DataManageMain:
    obj = ExtendDataManage("extendDataManage")
    obj.main_func()



class Product:
    # def __init__(self,name,type,price,weight):
    #     self.set_name(name)
    #     self.set_type(type)
    #     self.set_price(price)
    #     self.set_weight(weight)

    __name = None
    __type = None
    __price = None
    __weight = None

    def set_name(self,name):
        self.__name = name

    def set_type(self,type):
        self.__type = type

    def set_price(self,price):
        self.__price = price

    def set_weight(self,weight):
        self.__weight = weight


    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_price(self):
        return self.__price

    def get_weight(self):
        return self.__weight
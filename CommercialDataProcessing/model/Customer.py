


class Customer:
    __name = None
    __amount = None
    __no_of_shares = None

    def set_name(self,name):
        self.__name = name

    def set_amount(self,amount):
        self.__amount = amount

    def set_no_of_shares(self,no_of_shares):
        self.__no_of_shares = no_of_shares

    def get_name(self):
        return self.__name

    def get_amount(self):
        return self.__amount

    def get_no_of_shares(self):
        return self.__no_of_shares
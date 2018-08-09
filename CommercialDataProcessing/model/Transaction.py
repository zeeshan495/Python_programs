


class Transaction:
    __customer_name = None
    __customer_symbol = None
    __buy_sell = None
    __total_shares = None
    __total_price = None
    __time = None

    def set_customer_name(self,customer_name):
        self.__customer_name = customer_name

    def set_customer_symbol(self,customer_symbol):
        self.__customer_symbol = customer_symbol

    def set_buy_sell(self,buy_sell):
        self.__buy_sell = buy_sell

    def set_total_shares(self,total_shares):
        self.__total_shares = total_shares

    def set_total_price(self,total_price):
        self.__total_price = total_price

    def set_time(self,time):
        self.__time = time

    self.__customer_name = customer_name

    def get_customer_symbol(self):
        return self.__customer_symbol

    def get_buy_sell(self,buy_sell):
        return self.__buy_sell

    def get_total_shares(self):
        return self.__total_shares

    def get_total_price(self,total_price):
        return self.__total_price

    def get_time(self,time):
        return self.__time
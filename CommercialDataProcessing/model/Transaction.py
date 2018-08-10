


class Transaction:
    __customer_name = None
    __company_symbol = None
    __buy_sell = None
    __total_shares = None
    __total_price = None
    __time = None

    def set_customer_name(self,customer_name):
        self.__customer_name = customer_name

    def set_company_symbol(self,company_symbol):
        self.__company_symbol = company_symbol

    def set_buy_sell(self,buy_sell):
        self.__buy_sell = buy_sell

    def set_total_shares(self,total_shares):
        self.__total_shares = total_shares

    def set_total_price(self,total_price):
        self.__total_price = total_price

    def set_time(self,time):
        self.__time = time

    def get_customer_name(self):
        return self.__customer_name

    def get_company_symbol(self):
        return self.__company_symbol

    def get_buy_sell(self):
        return self.__buy_sell

    def get_total_shares(self):
        return self.__total_shares

    def get_total_price(self):
        return self.__total_price

    def get_time(self):
        return self.__time
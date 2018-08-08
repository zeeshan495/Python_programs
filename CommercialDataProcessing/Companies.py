


class Companies:
    __company_name = None
    __company_symbol = None
    __share_price = None
    __total_shares = None
    __time = None

    def set_company_name(self,__company_name):
        self.__company_name = __company_name

    def set_company_symbol(self,_company_name):
        self.__company_symbol = _company_symbol

    def set_share_price(self,_share_price):
        self.__share_price = _share_price

    def set_total_shares(self,_total_shares):
        self.__total_shares = _total_shares

    def set_time(self,_time):
        self.__time = _time

    def get_company_name(self):
        return self.__company_name

    def get_company_symbol(self):
        return self.__company_symbol
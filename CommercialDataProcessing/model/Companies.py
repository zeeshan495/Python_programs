


class Companies:
    __company_name = None
    __company_symbol = None
    __share_price = None
    __total_shares = None

    def set_company_name(self,__company_name):
        self.__company_name = __company_name

    def set_company_symbol(self,company_symbol):
        self.__company_symbol = company_symbol

    def set_share_price(self,share_price):
        self.__share_price = share_price

    def set_total_shares(self,total_shares):
        self.__total_shares = total_shares


    def get_company_name(self):
        return self.__company_name

    def get_company_symbol(self):
        return self.__company_symbol

    def get_share_price(self):
        return self.__share_price

    def get_total_shares(self):
        return self.__total_shares


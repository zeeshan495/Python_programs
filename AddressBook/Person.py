

class Person():
    __first_name = None
    __last_name = None
    __phone_number = None
    __state = None
    __city = None
    __zip = None

    def set_first_name(self,_first_name):
        self.__first_name = _first_name

    def set_last_name(self,_last_name):
        self.__last_name = _last_name

    def set__phone_number(self,_phone_number):
        self.__phone_number = _phone_number

    def set__state(self,_state):
        self.__state = _state

    def set__city(self,_city):
        self.__city = _city

    def set__zip(self,_zip):
        self.__zip = _zip


    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get__phone_number(self):
        return self.__phone_number

    def get__state(self):
        return self.__state

    def get__city(self):
        return self.__city

    def get__zip(self):
        return self.__zip
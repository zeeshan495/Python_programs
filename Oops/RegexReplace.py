
from Utility import *
from RegexInfo import *
class RegexReplace:

    __main_str = None
    __info_obj = RegexInfo()

    def __init__(self, main_str):
        self.__main_str = main_str

    def regex_replace(self, info_obj):
        self.__info_obj = info_obj

        if re.search("[\wA-Za-z]{2,20}", self.__info_obj.get__sur_name()):
            self.__main_str = self.__main_str.replace("<<name>>",self.__info_obj.get__sur_name())
        else:
            print("invalid input......try again : ")
            return False

        if re.search("[\wA-Za-z]{2,20}\s\w[A-Za-z]{2,20}", self.__info_obj.get__full_name()):
            self.__main_str = self.__main_str.replace("<<full name>>", self.__info_obj.get__full_name())
        else:
            print("invalid input......try again : ")
            return False

        if re.search("\w{10}", self.__info_obj.get__mobile_num()):
            self.__main_str = self.__main_str.replace("xxxxxxxxxx", self.__info_obj.get__mobile_num())
        else:
            print("invalid input......try again : ")
            return False

        self.__main_str = self.__main_str.replace("01/01/2016", self.__info_obj.get__date())
        return True

    def display(self):
        print(self.__main_str)





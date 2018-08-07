

class Doctor:
    __doctor_name = None
    __docotr_id = None
    __specialization = None
    __avialability = None

    def set_doctor_name(self,data):
        self.__doctor_name = data

    def set_doctor_id(self,data):
        self.__doctor_id = data

    def set_specialization(self,data):
        self.__specialization = data

    def set_avialability(self,data):
        self.__avialability = data

    def get_doctor_name(self):
        return self.__doctor_name

    def get_doctor_id(self):
        return self.__doctor_id

    def get_specialization(self):
        return self.__specialization

    def get_avialability(self):
        return self.__avialability
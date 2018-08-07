

class Patient:
    __patient_name = None
    __patient_id = None
    __number = None
    __age = None

    def set__patient_name(self, data):
        self.__patient_name = data

    def set_patient_id(self, data):
        self.__patient_id = data

    def set_number(self, data):
        self.__number = data

    def set_age(self, data):
        self.__age = data

    def get_patient_name(self):
        return self.__patient_name

    def get_patient_id(self):
        return self.__patient_id

    def get_number(self):
        return self.__number

    def get_age(self):
        return self.__age
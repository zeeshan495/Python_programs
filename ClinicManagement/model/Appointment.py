

class Appointment:
    __doctor = None
    __patient = None
    __date = None

    def set_doctor(self,doctor):
        self.__doctor = doctor

    def set_patient(self,patient):
        self.__patient = patient

    def set_date(self,date):
        self.__date = date

    def get_doctor(self):
        return self.__doctor

    def get_patient(self):
        return self.__patient

    def get_date(self):
        return self.__date
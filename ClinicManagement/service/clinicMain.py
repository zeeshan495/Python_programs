

from Oops.Utility import *
from ClinicManagement.controller.ClinicImplementation import *
class clinicMain:

    utility = Utility()
    print("\t\t_____________________________________________\n")
    print("\t\t\t***Welcome to our clinic***\n")
    def clinicManagement(self):
        clinic = ClinicImplementation()

        while True:
            print("\t\t\t\tMAIN MENU")
            print("\t\t_____________________________________________\n")
            print("\t\tenter '1' to add doctor")
            print("\t\tenter '2' to add patient")
            print("\t\tenter '3' to take appointment")
            print("\t\tenter '4' to display appointments or to search")
            print("\t\tenter '5' to close")
            print("\t\t_____________________________________________")
            choice = self.utility.input_int_data()
            if choice == 1:
                doctor_list = clinic.read("doctor")
                clinic.add_doctor(doctor_list)

            elif choice == 2:
                patient_list = clinic.read("patient")
                clinic.add_patient(patient_list)

            elif choice == 3:
                doctor_list = clinic.read("doctor")
                patient_list = clinic.read("patient")
                clinic.take_appointment(doctor_list,patient_list)

            elif choice == 4:
                doctor_list = clinic.read("doctor")
                patient_list = clinic.read("patient")
                clinic.display(doctor_list,patient_list)

            elif choice == 5:
                print("clinic closed...thank you")
                break

            else:
                print("invalid input")

obj = clinicMain()
obj.clinicManagement()
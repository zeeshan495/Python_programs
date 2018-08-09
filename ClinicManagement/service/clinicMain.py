

from Oops.Utility import *
from ClinicManagement.controller.ClinicImplementation import *
class clinicMain:

    utility = Utility()
    print("\t\t_____________________________________________\n")
    print("\t\t\t***Welcome to our clinic***\n")
    def clinicManagement(self):
        doctor_list = {}
        patient_list = {}
        clinic1 = ClinicImplementation(doctor_list,patient_list)
        new_doctor_list = clinic1.read("doctor")
        new_patient_list = clinic1.read("patient")
        clinic = ClinicImplementation(new_doctor_list, new_patient_list)

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
                clinic.add_doctor()

            elif choice == 2:
                clinic.add_patient()

            elif choice == 3:
                clinic.take_appointment()

            elif choice == 4:
                clinic.display()

            elif choice == 5:
                print("clinic closed...thank you")
                break

            else:
                print("invalid input")

obj = clinicMain()
obj.clinicManagement()
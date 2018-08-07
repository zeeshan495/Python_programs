
from ClinicManagement.model.Doctor import *
from Oops.Utility import *
import json
class ClinicImplementation:
    utility = Utility()
    doctor_list = {}
    patient_list = {}
    appointment_list = {}

    def add_doctor(self):
        var_doctor_details = self.doctor_details()
        if var_doctor_details.get_doctor_name in self.doctor_list:
            self.doctor_list[var_doctor_details.get_doctor_name()].append({"doctor_name": var_doctor_details.get_doctor_name(),"doctor_id":var_doctor_details.get_doctor_id(),"specialization":var_doctor_details.get_specialization(),"avialability":var_doctor_details.get_avialability()})
        else:
            self.doctor_list[var_doctor_details.get_doctor_name()] = {"doctor_name": var_doctor_details.get_doctor_name(), "doctor_id": var_doctor_details.get_doctor_id(),
                 "specialization": var_doctor_details.get_specialization(),
                 "avialability": var_doctor_details.get_avialability()}
        self.save("doctor",self.doctor_list)

    def doctor_details(self):
        doctor = Doctor()
        print("please enter a doctor name : ")
        doctor.set_doctor_name(self.utility.input_str_data())
        print("please enter a doctor id : ")
        doctor.set_doctor_id(self.utility.input_int_data())
        print("please enter a doctor specialiazation : ")
        doctor.set_specialization(self.utility.input_str_data())
        print("please enter a doctor availiability : ")
        while True:
            print("1 for 'am'")
            print("2for 'pm'")
            print("3 for 'both'")
            choice = self.utility.input_int_data()
            if choice == 1:
                data = "am"
                break
            elif choice == 2:
                data = "pm"
                break
            elif choice == 3:
                data = "both"
                break
            else:
                print("invalid")
        doctor.set_avialability(data)
        return doctor

    def add_patient(self):
        var_patient_details = patient_details()
        if var_patient_details.get in self.patient_list:
            pass



    def patient_details(self):
        patient = Patient()
        print("please enter a patient name : ")
        patient.get_patient_name(self.utility.input_str_data())
        print("please enter a patient id : ")
        patient.get_patient_id(self.utility.input_int_data())
        print("please enter a number : ")
        patient.get_number(self.utility.input_int_data())
        print("please enter age : ")
        patient.get_age(self.utility.input_int_data())
        return patient


    def save(self, file_name, my_list):
        data = json.dumps(my_list)
        print(file_name)
        print(my_list)
        with open("/home/bridgeit/Zeeshan_Python/clinicJson/"+file_name+".json", 'w') as f:
            f.write(data)
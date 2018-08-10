
from ClinicManagement.model.Doctor import *
from ClinicManagement.model.Patient import *
from ClinicManagement.model.Appointment import *
from Oops.Utility import *
from datetime import *
from ClinicManagement.controller.searchClinic import *
from ClinicManagement.controller.displayClinic import *
from ClinicManagement.controller.ClinicManager import *
import os
import json
class ClinicImplementation(ClinicManager):
    utility = Utility()
    appointment_list = {}
    __doctor_list = {}
    __patient_list = {}

    def __init__(self, doctor_list, patient_list):
        self.__doctor_list = doctor_list
        self.__patient_list = patient_list

    def add_doctor(self):
        # self.__doctor_list = self.read("doctor")
        var_doctor_details = self.doctor_details()
        if var_doctor_details.get_doctor_name() in self.__doctor_list:
            self.__doctor_list[var_doctor_details.get_doctor_name()].append({"doctor_name": var_doctor_details.get_doctor_name(),"doctor_id":var_doctor_details.get_doctor_id(),"specialization":var_doctor_details.get_specialization(),"avialability":var_doctor_details.get_avialability()})
        else:
            self.__doctor_list[var_doctor_details.get_doctor_name()] = {"doctor_name": var_doctor_details.get_doctor_name(), "doctor_id": var_doctor_details.get_doctor_id(),
                 "specialization": var_doctor_details.get_specialization(),
                 "avialability": var_doctor_details.get_avialability()}
        self.save("doctor",self.__doctor_list)

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
        # self.__patient_list = self.read("patient")
        var_patient_details = self.patient_details()
        if var_patient_details.get_patient_name() in self.__patient_list:
            self.__patient_list[var_patient_details.get_patient_name()].append({"patient_name":var_patient_details.get_patient_name(), "patient_id":var_patient_details.get_patient_id(), "number":var_patient_details.get_number(), "age":get_age()})
        else:
            self.__patient_list[var_patient_details.get_patient_name()] = {"patient_name": var_patient_details.get_patient_name(),
                 "patient_id": var_patient_details.get_patient_id(), "number": var_patient_details.get_number(),
                 "age": var_patient_details.get_age()}
        self.save("patient",self.__patient_list)

    def patient_details(self):
        patient = Patient()
        print("please enter a patient name : ")
        patient.set__patient_name(self.utility.input_str_data())
        print("please enter a patient id : ")
        patient.set_patient_id(self.utility.input_int_data())
        print("please enter a number : ")
        patient.set_number(self.utility.input_int_data())
        print("please enter age : ")
        patient.set_age(self.utility.input_int_data())
        return patient

    def add_appointment(self,particular_doctor, particular_patient):
        var_appointment_details = self.appointment_details(particular_doctor, particular_patient)
        f = open("/home/bridgeit/Zeeshan_Python/clinicJson/appointment.json", 'r')
        data = json.load(f)
        data["appointment"].append({'doctor':var_appointment_details.get_doctor(),'patient':var_appointment_details.get_patient()
                                    ,'date':var_appointment_details.get_date()})
        with open("/home/bridgeit/Zeeshan_Python/clinicJson/appointment.json",'w') as var_x:
            json.dump(data,var_x,sort_keys=True)
        print("appointment done")

    def appointment_details(self, particular_doctor, particular_patient):
        appointment = Appointment()
        appointment.set_doctor(particular_doctor)
        appointment.set_patient(particular_patient)
        date = datetime.now()
        appointment.set_date(str(date)[:20])
        return appointment

    def take_appointment(self):
        while True:
            print("please enter a doctor name : ")
            doctor_detail = self.utility.input_str_data()
            availibility_list = self.search_doctor(doctor_detail,self.__doctor_list)
            if availibility_list == {}:
                print("you searched doctor was unavailable : ")
            else:
                appointment_list = self.read("appointment")
                count = 0
                for x in range(0,len(appointment_list["appointment"])):
                    if(availibility_list[doctor_detail]["doctor_name"] == appointment_list["appointment"][x]["doctor"][doctor_detail]["doctor_name"]):
                        count +=1
                print(count)
                if(count >= 5):
                    print("doctor had more appointments ")
                else:
                    print("please enter any patient detail : ")
                    patient_detail = self.utility.input_str_data()
                    particular_patient = self.search_patient(patient_detail,self.__patient_list)

                    if particular_patient == {}:
                        print("you searched patient was unavailable : ")
                    else:
                        self.add_appointment(availibility_list, particular_patient)
                    break

    def search_doctor(self,details,doctor_list):
        new_list = {}
        for x in doctor_list:
            if(details == doctor_list[x]["doctor_name"] or details == doctor_list[x]["doctor_id"] or details == doctor_list[x]["specialization"] or details == doctor_list[x]["avialability"]):
                if doctor_list[x]["doctor_name"] in new_list:
                    new_list[doctor_list[x]["doctor_name"]].append[doctor_list[x]]
                else:
                    new_list[doctor_list[x]["doctor_name"]] = doctor_list[x]
        return new_list

    def search_patient(self,details,patient_list):
        new_list = {}
        for x in patient_list:
            if(details == patient_list[x]["patient_name"] or details == patient_list[x]["patient_id"] or details == patient_list[x]["number"] or details == patient_list[x]["age"]):
                    new_list[patient_list[x]["patient_name"]] = patient_list[x]
        return new_list

    def save(self, file_name, my_list):
        data = json.dumps(my_list)
        print(file_name)
        print(my_list)
        with open("/home/bridgeit/Zeeshan_Python/clinicJson/"+file_name+".json", 'w') as f:
            f.write(data)

    def read(self, file_name):
        my_list = {}
        path_name = "/home/bridgeit/Zeeshan_Python/clinicJson/" + file_name + ".json"
        if (os.stat(path_name).st_size != 0):
            f = open(path_name, "r")
            data = json.load(f)
            for x in data:
                if x in my_list:
                    my_list[x].append(data[x])
                else:
                    my_list[x] = data[x]
        return my_list

    def display(self):
        appointment_list = self.read("appointment")
        display_clinic_obj = displayClinic()
        search_clinic_obj = searchClinic()
        while True:
            print("enter choice : ")
            print("1 for display doctor")
            print("2 for display patients")
            print("3 for display appointments")
            print("4 for display Popular Doctor")
            print("5 for display Popular Specialization")
            print("6 for search")
            print("7 for main menu")
            choice = self.utility.input_int_data()
            if choice == 1:
                display_clinic_obj.display_doctor(self.__doctor_list)
            elif choice == 2:
                display_clinic_obj.display_patient(self.__patient_list)
            elif choice == 3:
                display_clinic_obj.display_appointments(appointment_list)
            elif choice == 4:
                display_clinic_obj.popular_doctor(self.__doctor_list,appointment_list)
            elif choice == 5:
                display_clinic_obj.popular_specialization(self.__doctor_list,appointment_list)
            elif choice == 6:
                search_clinic_obj.search(self.__doctor_list,self.__patient_list)
            elif choice == 7:
                break
            else:
                print("invalid")

from Oops.Utility import *
import json
class searchClinic:
    utility = Utility()

    def search_doctor(self, doctor_list):
         print("enter any detail of doctor : ")
         detail = self.utility.input_str_data()
         flag = False
         for x in doctor_list:
             if(detail == doctor_list[x]["doctor_name"]) or (detail == str(doctor_list[x]["doctor_id"])) or (detail == doctor_list[x]["specialization"]) or (detail == doctor_list[x]["avialability"]):
                 print("doctor was found")
                 print("doctor name\t\t:\t" + str(doctor_list[x]["doctor_name"]))
                 print("doctor id\t\t:\t" + str(doctor_list[x]["doctor_id"]))
                 print("specialization\t:\t" + str(doctor_list[x]["specialization"]))
                 print("avialability\t:\t" + str(doctor_list[x]["avialability"]))
                 print("\n")
                 flag = True
         if(flag == False):
             print("Your entered details are not found")

    def search_patient(self, patient_list):
         print("enter any detail of patient : ")
         detail = self.utility.input_str_data()
         flag = False
         for x in patient_list:
             if(detail == patient_list[x]["patient_name"]) or (detail == str(patient_list[x]["patient_id"])) or (detail == str(patient_list[x]["number"])) or (detail == str(patient_list[x]["age"])):
                 print("name\t:\t" + str(patient_list[x]["patient_name"]))
                 print("id\t\t:\t" + str(patient_list[x]["patient_id"]))
                 print("number\t:\t" + str(patient_list[x]["number"]))
                 print("age\t\t:\t" + str(patient_list[x]["age"]))
                 print("\n")
                 flag = True
         if(flag == False):
             print("Your entered details are not found")

    def search(self,doctor_list, patient_list):
        while True:
            print("enter a choice : ")
            print("1 for search doctor")
            print("2 for search patient")
            print("3 go back for menu")
            choice = self.utility.input_int_data()
            if choice == 1:
                self.search_doctor(doctor_list)
            elif choice == 2:
                self.search_patient(patient_list)
            elif choice == 3:
                break

            else:
                print("invalid choice")

import json

class displayClinic:

    def display_doctor(self,doctor_list):
        print("\tDoctors")
        for x in doctor_list:
            print("doctor name\t\t:\t"+str(doctor_list[x]["doctor_name"]))
            print("doctor id\t\t:\t" + str(doctor_list[x]["doctor_id"]))
            print("specialization\t:\t" + str(doctor_list[x]["specialization"]))
            print("avialability\t:\t" + str(doctor_list[x]["avialability"]))
            print("\n")

    def display_patient(self,patient_list):
        print("\tPatients")
        for x in patient_list:
            print("name\t:\t"+str(patient_list[x]["patient_name"]))
            print("id\t\t:\t" + str(patient_list[x]["patient_id"]))
            print("number\t:\t" + str(patient_list[x]["number"]))
            print("age\t\t:\t" + str(patient_list[x]["age"]))
            print("\n")

    def display_appointments(self,appointment_list):
        for x in range(0, len(appointment_list["appointment"])):
             name_key = appointment_list["appointment"][x]["doctor"]
             main_key = name_key.keys()
             print("\t\tAppointment"+str(x+1))
             print("\t\tDoctor")
             print("doctor name\t\t:\t"+str(main_key[0]))
             print("doctor id\t\t:\t"+str(appointment_list["appointment"][x]["doctor"][main_key[0]]["doctor_id"]))
             print("avialability\t:\t" + str(appointment_list["appointment"][x]["doctor"][main_key[0]]["avialability"]))
             print("specialization\t:\t" + str(appointment_list["appointment"][x]["doctor"][main_key[0]]["specialization"]))

             name_key2 = appointment_list["appointment"][x]["patient"]
             main_key2 = name_key2.keys()
             print("\n\t\tpatient")
             print("name\t:\t" + str(main_key2[0]))
             print("id\t\t:\t" + str(appointment_list["appointment"][x]["patient"][main_key2[0]]["patient_id"]))
             print("age\t\t:\t" + str(
                 appointment_list["appointment"][x]["patient"][main_key2[0]]["age"]))
             print("number\t:\t" + str(
                 appointment_list["appointment"][x]["patient"][main_key2[0]]["number"]))
             print("\n")

    def popular_doctor(self,doctor_list, appointment_list):
        for x in doctor_list:
            count = 0
            for y in range(0, len(appointment_list["appointment"])):
                name_key = appointment_list["appointment"][y]["doctor"]
                main_key = name_key.keys()
                if(main_key[0] == doctor_list[x]["doctor_name"]):
                    count += 1
            if(count >= 5):
                print("our popular doctor : "+str(doctor_list[x]["doctor_name"]))

    def popular_specialization(self,doctor_list, appointment_list):
        for x in doctor_list:
            count = 0
            for y in range(0, len(appointment_list["appointment"])):
                name_key = appointment_list["appointment"][y]["doctor"]
                main_key = name_key.keys()
                if(main_key[0] == doctor_list[x]["doctor_name"]):
                    count += 1
            if(count >= 5):
                print("our popular specialization : "+str(doctor_list[x]["specialization"]))
                print("Doctor name is : "+str(doctor_list[x]["doctor_name"]))

from AddressBook import *
from Oops.Utility import *
from Person import *
import os
import os.path
import json
class AddressBookImplementation(AddressBook):
    my_list = {}
    utility = Utility()

    def operation(self):
        print("enter the address book name : ")
        addressbook_name = self.utility.input_str_data()
        path = "/home/bridgeit/Zeeshan_Python/AddressJson"
        dirs = os.listdir(path)
        status = False
        for files in dirs:
            if (files == addressbook_name+".json"):
                status = True
                file_name = "/home/bridgeit/Zeeshan_Python/AddressJson/" + addressbook_name + ".json"
                if (os.stat(file_name).st_size != 0):
                    f = open(file_name,"r")
                    data = json.load(f)
                    for x in data:
                        if x in self.my_list:
                            self.my_list[x].append(data[x])
                        else:
                            self.my_list[x] = data[x]
        if(status):
            print("File exists")
            while True:
                print("\tMENU")
                print("\tselect a choice : ")
                print("1 add new person information : ")
                print("2 display information")
                print("3 sort by zip")
                print("4 sort by name")
                print("5 delete")
                print("6 edit")
                print("7 go for main menu")
                choice = self.utility.input_int_data()
                if (choice == 1):
                    self.add_person()
                    self.save(addressbook_name)

                elif (choice == 2):
                    if (os.stat(file_name).st_size == 0):
                        print("it is empty")
                    else:
                        self.display(addressbook_name)

                elif (choice == 3):
                    if (os.stat(file_name).st_size == 0):
                        print("it is empty")
                    else:
                        self.sort_by_zip(addressbook_name)

                elif (choice == 4):
                    if (os.stat(file_name).st_size == 0):
                        print("it is empty")
                    else:
                        self.sort_by_name(addressbook_name)

                elif (choice == 5):
                    if (os.stat(file_name).st_size == 0):
                        print("it is empty")
                    else:
                        print("enter a first name to delete : ")
                        self.delete(addressbook_name)

                elif (choice == 6):
                    if (os.stat(file_name).st_size == 0):
                        print("it is empty")
                    else:
                        print("enter a first name to edit : ")
                        self.edit(addressbook_name)
                elif (choice == 7):
                    self.my_list = {}
                    break
                else:
                    print('Invalid input')
        else:
            print("file doesn't found")

    def add_person(self):
        user = self.add_user()
        try:
            if user.get_first_name() in self.my_list:
                self.my_list[user.get_first_name()].append({"first_name": user.get_first_name(), "last_name": user.get_last_name(), "city": user.get__city(),
                  "state": user.get__state(), "phone": user.get__phone_number(), "zip": user.get__zip()})
            else:
                self.my_list[user.get_first_name()] = {"first_name": user.get_first_name(), "last_name": user.get_last_name(), "city": user.get__city(),
                  "state": user.get__state(), "phone": user.get__phone_number(), "zip": user.get__zip()}
        except AttributeError:
            print("enter name is already exist")

    def add_user(self):
        person = Person()
        print("enter first name : ")
        person.set_first_name(self.utility.input_str_data())
        print("enter last name : ")
        person.set_last_name(self.utility.input_str_data())
        print("enter city name : ")
        person.set__city(self.utility.input_str_data())
        print("enter state name : ")
        person.set__state(self.utility.input_str_data())
        print("enter phone number : ")
        person.set__phone_number(self.utility.input_int_data())
        print("enter zipcode : ")
        person.set__zip(self.utility.input_int_data())
        return person

    def save(self,addressbook_name):
        data = json.dumps(self.my_list)
        with open("/home/bridgeit/Zeeshan_Python/AddressJson/"+addressbook_name+".json", 'w') as f:
            f.write(data)

    def display(self,addressbook_name):
        f = open("/home/bridgeit/Zeeshan_Python/AddressJson/"+addressbook_name+".json", "r")
        data = json.load(f)
        print("***contacts***\n")
        for x in data:
            print("first name : "+str(data[x]["first_name"]))
            print("last name : " + str(data[x]["last_name"]))
            print("mobile number : " + str(data[x]["phone"]))
            print("city : " + str(data[x]["city"]))
            print("state : " + str(data[x]["state"]))
            print("zip code : " + str(data[x]["zip"]))
            print("\n")


    def sort_by_name(self,addressbook_name):
        temp = []
        f = open("/home/bridgeit/Zeeshan_Python/AddressJson/" + addressbook_name + ".json", "r")
        data = json.load(f)
        for x in data:
            temp.append(data[x]["first_name"])
        sort_list = sorted(temp)

        print("***contacts***\n")
        print("sorted by first name")
        for y in range(0,len(sort_list)):
            for x in data:
                if(sort_list[y] == data[x]["first_name"]):
                    print("first name : " + str(data[x]["first_name"]))
                    print("lasr name : " + str(data[x]["last_name"]))
                    print("mobile number : " + str(data[x]["phone"]))
                    print("city : " + str(data[x]["city"]))
                    print("state : " + str(data[x]["state"]))
                    print("zip code : " + str(data[x]["zip"]))
                    print("\n")

    def sort_by_zip(self,addressbook_name):
        temp = []
        f = open("/home/bridgeit/Zeeshan_Python/AddressJson/" + addressbook_name + ".json", "r")
        data = json.load(f)
        for x in data:
            var_zip =   str(data[x]["zip"])[0]
            temp.append(var_zip)
        sort_list = sorted(temp)
        print("***contacts***\n")
        print("sorted by first name")
        for y in range(0,len(sort_list)):
            for x in data:
                if(sort_list[y] == str(data[x]["zip"])[0]):
                    print("first name : " + str(data[x]["first_name"]))
                    print("lasr name : " + str(data[x]["last_name"]))
                    print("mobile number : " + str(data[x]["phone"]))
                    print("city : " + str(data[x]["city"]))
                    print("state : " + str(data[x]["state"]))
                    print("zip code : " + str(data[x]["zip"]))
                    print("\n")


    def delete(self,addressbook_name):
        key = self.utility.input_str_data()
        if key in self.my_list:
            del self.my_list[key]
            print("successfully done")
            data = json.dumps(self.my_list)
            with open("/home/bridgeit/Zeeshan_Python/AddressJson/" + addressbook_name + ".json", 'w') as f:
                f.write(data)
            return True
        else:
            print("entered contact is unavaialable")


    def edit(self,addressbook_name):
        status = self.delete(addressbook_name)
        if(status):
            self.add_person()
            self.save(addressbook_name)


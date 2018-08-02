
from Utility import *
class Calender:
    utility = Utility()
    while True:
            print("please enter a principal : ")
            var_principal = utility.input_float_data()
            print("please enter a interest : ")
            var_interest = utility.input_float_data()
            print("please enter a year : ")
            var_year = utility.input_float_data()
            if (var_year <= 0) or (var_principal <= 0) or (var_interest < 0):
                print("please check the entered input")
            else:
                utility.calculation(var_principal, var_interest, var_year)
                break
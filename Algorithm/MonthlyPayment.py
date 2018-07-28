
from Utility import *
class Calender:
    utility = Utility()
    while True:
        try:
            var_principal = float(input("please enter principal "))
            var_interest = float(input("please enter interest "))
            var_year = float(input("please enter year "))
            break
        except NameError:
            print("please enter integer value ")
        except SyntaxError :
            print("please check the input ")
    utility.calculation(var_principal,var_interest,var_year)
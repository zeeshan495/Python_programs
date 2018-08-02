
from Utility import *
class Calender:
    utility = Utility()
    print('please enter day ')
    var_date = utility.input_int_data()
    print('please enter month ')
    var_month = utility.input_int_data()
    print('please enter year ')
    var_year = utility.input_int_data()
    if(var_date <= 0) or (var_month <= 0) or (var_year <= 0) or (var_month >12):
        print("check the entered input")
    else:
        var_day=utility.day_of_week(var_date,var_month,var_year)
        if(var_day==0):
            print("sunday")
        elif(var_day==1):
            print("monday")
        elif (var_day == 2):
            print("tuesday")
        elif (var_day == 3):
            print("wednesday")
        elif(var_day == 4):
            print("thursday")
        elif (var_day == 5):
            print("friday")
        elif (var_day == 6):
            print("saturday")
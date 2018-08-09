
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
        print("please check the entered input")

    elif var_date > 29 and var_month == 2:
        print("there is no such a day as with your entered input")
    else:
        result = utility.is_leap_year(var_year)
        if var_date == 29 and result == False:
            print("there is no such a day as with your entered input")
        else:
            x = utility.day_of_week(var_date,var_month,var_year)
            var_day = ["sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
            print(var_day[x])

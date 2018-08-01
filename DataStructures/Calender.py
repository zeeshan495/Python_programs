

from Utility import *
class Calender:
    utility = Utility()
    print("enter a month : ")
    var_month = utility.input_int_data()
    print("enter a year : ")
    var_year = utility.input_int_data()
    months_array = ["",
            "January", "February", "March",
            "April", "May", "June",
            "July", "August", "September",
            "October", "November", "December"]
    days_array = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if(var_month == 2) and (utility.is_leap_year(var_year)):
        days_array[var_month] = 29

    print("\t\t---------------------"+str(months_array[var_month])+" "+str(var_year)+"---------------------\n")
    week_arr = ["S","M","TU","W","TH","F","SA"]
    for x in range(0,len(week_arr)):
        value = format(str(week_arr[x]), " >8s")
        print(value),
    print("\n")
    var_day = utility.day_of_week(1,var_month,var_year)
    for x in range(0,var_day):
        value = format("", ">8s")
        print(value),
    for x in range(1,days_array[var_month]+1):
        # print ' '+str(x),
        value = format(str(x)," >8s")
        print(value),
        if((x + var_day) % 7 == 0) or(x == days_array[var_month]):
            print("\n")
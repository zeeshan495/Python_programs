
from Utility import *
class Calender:
    utility = Utility()
    while True:
        try:
            var_date = int(input("please enter day "))
            var_month = int(input("please enter month "))
            var_year = int(input("please enter year "))
            break
        except NameError:
            print("please enter integer value")

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
from Utility import *
class LeapYear :
        utility = Utility()
        print("please enter a year : ")
        year = utility.input_int_data()
        result= utility.is_leap_year(year)
        if(result==True) :
            print("given year is a leap year")
        else:
            print("not a leap year")

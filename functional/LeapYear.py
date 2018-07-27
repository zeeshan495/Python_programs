from Utility import *
class LeapYear :
        obj = Utility()
        year=int(input("please enter a year"))
        result= obj.is_leap_year(year)
        if(result==True) :
            print("given year is a leap year")
        else:
            print("not a leap year")

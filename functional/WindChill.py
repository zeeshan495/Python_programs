
from Utility import *
class WindChill:
    utility=Utility()
    while True:
        try:
            var_t=int(input("please enter the temperature t (in Fahrenheit)"))
            var_v=int(input("please enter the wind speed v (in miles per hour)"))
            break
        except NameError :
            print("please enter integer values")
        utility.weather(var_t, var_v)
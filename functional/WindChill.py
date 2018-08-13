
from Utility import *
class WindChill:
    utility=Utility()
    print("please enter the temperature t (in Fahrenheit) below '50'")
    var_t = utility.input_int_data()
    print("please enter the wind speed v (in miles per hour) between '3' and '120'")
    var_v = utility.input_int_data()
    if ((var_t <= 50) and (var_v <= 120) and (var_v >= 3)):
        utility.weather(var_t, var_v)
    else:
        print("please enter input as mention in range")
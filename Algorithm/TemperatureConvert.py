
from Utility import *
class TemperatureConvert:
    utility = Utility()
    print("please enter choice : ")
    print("To enter the temperature in fahrenheit enter '1'")
    print("To enter the temperature in Celsius enter '2'")
    var_input = utility.input_int_data()

    if(var_input == 1):
        utility.celsius()
    elif(var_input == 2):
        utility.fahrenheit()
    else:
        print("enter a valid number")

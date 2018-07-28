
from Utility import *
class TemperatureConvert:
    utility = Utility()
    while True:
        try:
            print("please enter choice : ")
            print("To enter the temperature in fahrenheit enter '1'")
            print("To enter the temperature in Celsius enter '2'")
            var_input = int(input())
            break
        except NameError:
            print("please enter integer value")
    if(var_input == 1):
        utility.celsius()
    elif(var_input == 2):
        utility.fahrenheit()
    else:
        print("enter a valid number")

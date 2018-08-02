
from Utility import *
class PrimeNumber:
    utility=Utility()
    try:
        print("enter a Nth term for prime numbers : ")
        var_input = utility.input_int_data()
        if (var_input == 0) or (var_input == 1):
            print(" no prime numbers")
        else:
            result_array = utility.primenumber(var_input)
            print("\n\t****Prime Numbers****\n")
            for x in range(0,len(result_array)):
                if(result_array[x] != None):
                    print(str(result_array[x])+" "),
    except OverflowError:
        print("overflow.....entered number is very high")

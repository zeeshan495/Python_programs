
from Utility import *
class PrimeNumber:
    utility=Utility()
    while True:
        try:
            var_input=int(input("please enter a Nth Term "))
            break
        except NameError :
            print("please enter integer value")
    result_array=utility.primenumber(var_input)
    print("\n\t****Prime Numbers****\n")
    for x in range(0,len(result_array)):
        if(result_array[x] != None):
            print(str(result_array[x])+" "),

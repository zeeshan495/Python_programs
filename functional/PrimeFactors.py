from Utility import *
class PrimeFactors:

            utility=Utility()
            input_number=int(input("Please enter a given input number : "))
            if(input_number >= 2):
                utility.factorization(input_number)
            else:
                print("check entered number")


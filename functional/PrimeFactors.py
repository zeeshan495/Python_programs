from Utility import *
class PrimeFactors:

            utility=Utility()
            input_number=int(input("Please enter a given input number : "))
            if(input_number>0):
                output_number=int(utility.factorization(input_number))
                if(output_number>0):
                    print('square root : '+str(output_number))
                else:
                    print("given number is not a square root")
            else:
                print("check entered number")
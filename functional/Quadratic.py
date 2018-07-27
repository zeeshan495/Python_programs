
from Utility import *
class Quadratic:
    utility=Utility()
    while True:
        try:
            a = int(input(" enter the a : "))
            b = int(input(" enter the b : "))
            c = int(input(" enter the c : "))
            break
        except NameError:
            print("please enter a number...try again")
    utility.find_roots(a,b,c)
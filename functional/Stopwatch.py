
from Utility import *
class Stopwatch:
    utility=Utility()
    print("***STOPWATCH***")
    while True:
        try:
            # input("enter any number to start ")
            print("enter 1 to start")
            choice = utility.input_int_data()
            if choice == 1:
                utility.start()
                # input("enter any number to stop ")
                print("enter 2 to stop")
                choice2 = utility.input_int_data()
                if choice2 == 2:
                    break
                else:
                    print("invalid input")
            else:
                print("invalid input")
        except NameError :
            print("please enter only integers ")
    utility.stop()
    var_elapsed_time=utility.elapsed_time()
    in_sec=var_elapsed_time/60
    print(" elapsed time "+str(var_elapsed_time)+" milli sec")
    print(" elapsed time " + str(in_sec) + " sec")
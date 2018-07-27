
from Utility import *
class Stopwatch:
    utility=Utility()
    print("***STOPWATCH***")
    while True:
        try:
            input("enter any number to start ")
            utility.start()
            input("enter any number to stop ")
            break
        except NameError :
            print("please enter only integers ")
    utility.stop()
    var_elapsed_time=utility.elapsed_time()
    in_sec=var_elapsed_time/60
    print(" elapsed time "+str(var_elapsed_time)+" milli sec")
    print(" elapsed time " + str(in_sec) + " sec")
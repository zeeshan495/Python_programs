

import time
import math
from array import *
import random

class Utility():
    start_time = 0
    stop_time = 0
    running = False
    global swap
    global permute

    def replacing(self, input_string, main_string):
        if len(input_string) >= 3:
            output_string = main_string.replace("<<UserName>>", input_string)
            return output_string
        else:
            return "enter more than two characters"

    def flip(self, number_of_times):
        heads = 0
        tails = 0
        if (number_of_times >= 0):
            for flip in range(1, number_of_times+1):
                if (random.random() < 0.5):
                    tails = tails + 1
                else:
                    heads = heads + 1
        else:
            print("please enter positive number")
        try:
            print("percentage of head " + float((100.0 * heads) / number_of_times))
            print("percentage of tail " + float((100.0 * tails) / number_of_times))
        except  ZeroDivisionError :
             print("Oops!  That was no valid number.  Try again...")

    def is_leap_year(self,year):
        if (year % 4 == 0) :
            if (year % 100 == 0) :
                if (year % 400 == 0) :
                    return True
                else :
                    return False
            else :
                return True
        else :
            return False

    def power_value(self,input_number):
        result=2
        for i in range(1,input_number):
            result=result*2
        return result

    def harmonic_func(self,given_input):
        harmonic_value=0
        for i in range(1,given_input+1):
            harmonic_value=(1.0/i)+harmonic_value
        print("the harmonic value : ",harmonic_value)

    def factorization(self,given_input):
        loop=given_input/2
        for x in range(1,loop+1):
            value=x*x
            if(given_input==value):
                return x
        return -1

    def game(self,stake,goal,number_of_times):
        loss=0
        wins=0
        for x in range(0,number_of_times):
            amount=stake
            while(amount>0) and (amount<goal):
                if(random.random()>0.5):
                    amount=amount+1
                else:
                    amount=amount-1
            if(amount==goal):
                wins=wins+1
            else:
                loss=loss+1
        print("total number of wins "+str(wins))
        print("percentage of win "+str((100.0 * wins) / number_of_times))
        print("percentage of loss "+str((100.0 * loss) / number_of_times))

    def random_number(self,given_input):
        count=0
        my_array=[None]*given_input
        for x in range(0,given_input):
            print(" x value : "+str(x))
            temp=random.randint(0,given_input)
            count=count+1
            my_array[x]=temp+1
            for y in range(0,x):
                if(my_array[x]==my_array[y]):
                    # print(" x array "+str(my_array[x])+ " y array "+str(my_array[y]))
                    # print("before "+str(x))
                    x-=1
                    # print("after " + str(x))
                    break

        for x in range(0,given_input):
            print(my_array[x]),
        print("\ntotal number of times random number generate "+str(count))

    def twod_int_array(self,):
        rows = int(input(" enter the number of rows : "))
        columns = int(input(" enter the number of columns : "))
        int_array = []
        for i in range(rows):
            int_array.append([])
            for j in range(columns):
                while True:
                    try:
                        input_value = int(input(" enter the value : "))
                        break
                    except NameError:
                        print("enter integer value only...try again")
                int_array[i].append(input_value)
        for i in range(rows):
            for j in range(columns):
                print(str(int_array[i][j])+" "),
            print("\n")

    def twod_boolean_array(self,):
        rows = int(input(" enter the number of rows : "))
        columns = int(input(" enter the number of columns : "))
        boolean_array = []
        for i in range(rows):
            boolean_array.append([])
            for j in range(columns):
                while True:
                    try:
                        input_value = bool(input(" enter the value : "))
                        break
                    except NameError:
                        print("enter boolean value...try again\n")
                boolean_array[i].append(input_value)
        for i in range(rows):
            for j in range(columns):
                print(str(boolean_array[i][j])+" "),
            print("\n")

    def twod_float_array(self, ):
        rows = int(input(" enter the number of rows : "))
        columns = int(input(" enter the number of columns : "))
        float_array = []
        for i in range(rows):
            float_array.append([])
            for j in range(columns):
                while True:
                    try:
                        input_value = float(input(" enter the value : "))
                        break
                    except NameError:
                        print("enter float values...try again\n")
                float_array[i].append(input_value)
        for i in range(rows):
            for j in range(columns):
                print(str(float_array[i][j])+" "),
            print("\n")

    def triplets(self,my_array):
        count=0
        for x in range(0,len(my_array)):
            while True:
                try:
                    my_array[x] = int(input(" enter the value : "))
                    break
                except NameError:
                    print("enter integer value only...try again")
        for x in range(0, len(my_array)-2):
            for y in range(x+1,len(my_array)-1):
                for z in range(y+1,len(my_array)):
                    if(my_array[x]+my_array[y]+my_array[z]==0):
                        count=count+1
                        print(str(my_array[x])+" "+str(my_array[y])+" "+str(my_array[z]))
        print("number of triplets "+str(count))

    def distance(self,var_x,var_y):
        var_result=math.sqrt(math.pow(var_x, 2)+math.pow(var_y,2))
        print("The Euclidean distance of "+str(var_x)+" and "+str(var_y)+" is : "+str(var_result))

    # global permute
    def permute(self,var_str,var_left,var_right):
        if(var_left==var_right):
                print(var_str)
        else:
            for x in range(var_left,var_right+1):
                var_str=swap(var_str,var_left,x)
                permute(var_str,var_left+1,var_right)


    def swap(var_str,var_left,var_right):
        temp=0
        my_list=list(var_str)
        temp=my_list[var_left]
        my_list[var_left]=my_list[var_right]
        my_list[var_right]=temp
        var_out=''.join(my_list)
        return var_out

    def start(self):
        global start_time,running
        start_time = int(round(time.time() * 100))
        running=True

    def stop(self):
        global stop_time, running
        stop_time=int(round(time.time() * 100))
        running=False

    def elapsed_time(self):
        global start_time, running, stop_time
        if(running==True):
            elapsed_time=int(round(time.time() * 100))-start_time
        else:
            elapsed_time=stop_time-start_time
        return elapsed_time

    def find_roots(self,a,b,c):
        delta=0
        root_1=0
        root_2=0
        try:
            delta = (b * b)-(4 * a * c)
            root_1 = (-b + math.sqrt(delta)) / (2 * a)
            root_2 = (-b - math.sqrt(delta)) / (2 * a)
            print("root 1 of x : "+str(root_1))
            print("root 2 of x : " + str(root_2))
        except ValueError :
            print("roots are not found for those values")

    def weather(self,var_t,var_v):
        var_w=0
        if((var_t<=50) and (var_v<=120) and (var_v >=3)):
            var_w = 35.74 + (0.6215 * var_t) + ((0.4275 * var_t) - 35.75) * math.pow(var_v, 0.16)
            print(var_w)
        else:
            print("please enter valid input")


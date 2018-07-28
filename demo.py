
import time
import math
from array import *
import random
# print(random.uniform(0,1))
# print(random.randint(0,20))
#numberOfTimes = int(raw_input("Please the number of times to Flip Coin "))
# rand=random.random()
# if (rand < 0.5):
#     print("if.....")
# else:
#     print("else.....")

# for i in range(0,10):
#     print(i),

# my_array=array('i',[99])
# my_array[0]=88
# print(my_array[0])
# my_array.append(44)
# print(my_array[1])
# my_array=[None]*2
# print("array length : "+str(len(my_array)))
# T=[[1,2,3],[4,5,6]]
# m = int(input(" enter the m : "))
# n = int(input(" enter the n : "))
# for x in range(0,m):
#     for y in range(0, n):
#         given_input = int(input(" enter the number : "))
#         T[x][y]=given_input
# for x in range(0,2):
#     for y in range(0, 2):
#         print(T[x][y]),
#     print("\n")

# a = []
# for i in range(3):
#     a.append([])
#     for j in range(3):
#          a[i].append(i+j)
#
# a[0][1]=99
# print(a)

#print(" power "+str(math.pow(2,2)))

# start_time = 0
# stop_time=0
# start_time = int(round(time.time() /1000000000))
# stop_time = int(round(time.time() /1000000000))
# print(start_time)
# print(stop_time)
# time=stop_time-start_time
# print(time)

# var_str="ABCZYX"
# out=list(var_str)
# print(out)
# out.sort()
# print(out)

# my_arr=[None]*4
# for x in range(0,len(my_arr)):
#         my_arr[x]=int(input("enter value"))
# for x in range( len(my_arr)-1, -1,-1):
#     print(my_arr[x]),
# print("\n")
var_binary_str="00000100"
# var_binary_arr=list(var_binary)
var_mid = len(var_binary_str) / 2
var_binary=int(var_binary_str)
var_temp=""

print(var_binary[0,2])
var_temp = var_temp + var_binary[var_mid+1,len(var_binary)]
print(var_temp)

from array import *
import random
print(random.uniform(0,1))
print(random.randint(0,20))
#numberOfTimes = int(raw_input("Please the number of times to Flip Coin "))
rand=random.random()
if (rand < 0.5):
    print("if.....")
else:
    print("else.....")

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

a = []
for i in range(3):
    a.append([])
    for j in range(3):
         a[i].append(i+j)

a[0][1]=99
print(a)

from QueueLinkedList import *
from Utility import *
class PrimeQueue:
    utility = Utility()
    queue = QueueLinkedList()
    var_list = []
    non_annagram = []
    index = 0
    prime_arr = utility.primenumber(1000)
    for x in range(0, len(prime_arr) - 1):
        for y in range(x + 1, len(prime_arr)):
            if (prime_arr[x] != None) and (prime_arr[y] != None):
                flag = utility.annagram(prime_arr[x], prime_arr[y])
                if (flag):
                    var_list.append(prime_arr[x])
                    var_list.append(prime_arr[y])

    print("\nAnnagrams : ")
    for x in range(0, len(var_list) - 1, 2):
        print(str(var_list[x]) + " " + str(var_list[x + 1])),
        queue.add_rear(var_list[x])
        queue.add_rear(var_list[x + 1])
        print("\n")

    for x in range(0, len(var_list) - 1):
        status = utility.check(prime_arr[x], var_list)
        if (status):
            non_annagram.append(prime_arr[x])

    print("After adding in queue : ")
    queue.display()
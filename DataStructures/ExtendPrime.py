

from Utility import *
class ExtendPrime:
    utility = Utility()
    var_list = []
    non_annagram = []
    index = 0
    prime_arr = utility.primenumber(1000)
    for x in range(0,len(prime_arr)-1):
        for y in range(x+1,len(prime_arr)):
            if(prime_arr[x] != None) and (prime_arr[y]!= None):
                flag = utility.annagram(prime_arr[x],prime_arr[y])
                if(flag):
                    var_list.append(prime_arr[x])
                    var_list.append(prime_arr[y])

    print("\nAnnagrams : ")
    for x in range(0,len(var_list)-1,2):
        print(str(var_list[x])+" "+str(var_list[x+1])),
        print("\n")


    for x in range(0,len(var_list)-1):
        status = utility.check(prime_arr[x],var_list)
        if(status):
           non_annagram.append(prime_arr[x])

    print("Non Annagrams")
    for x in range(len(non_annagram)):
        print str(non_annagram[x])+" ",

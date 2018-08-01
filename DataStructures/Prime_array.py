

from Utility import *
class Prime_array:
    utility = Utility()
    var_list = []
    for x in range(0, 10):
        var_list.append([])
    var_row = 0
    var_column = 0
    var_count = 1
    prime_arr = utility.primenumber(1000)

    for x in range(0,len(prime_arr)):
        if(prime_arr[x] != None):
            var_row = prime_arr[x]/100
            var_list[var_row].append(prime_arr[x])

    try:
        for x in range(0, len(prime_arr)):
            if(prime_arr[x] != None):
                var_row = prime_arr[x]/100

                if(var_row == var_count):
                    var_count = var_count + 1
                    var_column = 0
                    print("\n")
                print(var_list[var_row][var_column]),
                var_column = var_column + 1
    except IndexError:
        print(" index error ")

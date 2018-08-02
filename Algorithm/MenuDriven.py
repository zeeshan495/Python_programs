
from Utility import *
class MenuDriven:
    utility = Utility()
    while True:
        print("\t please select a choice : ")
        print("1 for binary search for integers : ")
        print("2 for binary search for strings : ")
        print("3 for insertion sort for integers : ")
        print("4 for insertion sort for strings : ")
        print("5 for bubble sort for integers : ")
        print("6 for bubble sort for strings : ")
        print("7 to exit")
        var_choice = utility.input_int_data()
        if(var_choice == 1):
            my_list = [99,88,23,78,95,11,45]
            my_list.sort()
            print(my_list)
            print("enter a key : ")
            var_key = utility.input_int_data()
            utility.binary_search(my_list, 0, len(my_list) - 1, var_key)
        elif(var_choice == 2):
            my_list = ["java", "c", "python", "aws", "nodejs"]
            my_list.sort()
            print(my_list)
            print("enter a key : ")
            var_key = utility.input_str_data()
            utility.binary_search(my_list, 0, len(my_list) - 1, var_key)

        elif (var_choice == 3):
            my_list = [99,88,23,78,95,11,45]
            print("before sort : "+str(my_list))
            sort_array = utility.insertion_sort(my_list)
            print("after insertion  sort : "+str(my_list))

        elif (var_choice == 4):
            my_list = ["java", "c", "python", "aws", "nodejs"]
            print("before sort : " + str(my_list))
            sort_array = utility.insertion_sort(my_list)
            print("after insertion sort : " + str(my_list))

        elif (var_choice == 5):
            my_list = [99, 88, 23, 78, 95, 11, 45]
            print("before sort : " + str(my_list))
            sort_array = utility.bubble_sort(my_list)
            print("after bubble sort : " + str(my_list))

        elif (var_choice == 6):
            my_list = ["java", "c", "python", "aws", "nodejs"]
            print("before sort : " + str(my_list))
            sort_array = utility.bubble_sort(my_list)
            print("after bubble sort : " + str(my_list))

        elif (var_choice == 7):
            print("Thank You")
            break

        else:
            print("please enter a valid choice")
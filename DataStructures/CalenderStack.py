
from Utility import *
from Stack import *
class CalenderStack:
    utility = Utility()
    stack_obj = Stack()
    stack_obj_2 = Stack()
    print("enter a month : ")
    var_month = utility.input_int_data()
    print("enter a year : ")
    var_year = utility.input_int_data()
    months_array = ["",
                    "January", "February", "March",
                    "April", "May", "June",
                    "July", "August", "September",
                    "October", "November", "December"]
    days_array = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (var_month == 2) and (utility.is_leap_year(var_year)):
        days_array[var_month] = 29

    print("\t\t---------------------" + str(months_array[var_month]) + " " + str(var_year) + "---------------------\n")
    week_arr = ["S", "M", "TU", "W", "TH", "F", "SA"]
    for x in range(0, len(week_arr)):
        value = format(str(week_arr[x]), " >8s")
        stack_obj.push(value)

    stack_obj.push("\n")
    var_day = utility.day_of_week(1, var_month, var_year)
    for x in range(0, var_day):
        value = format("", ">8s")
        stack_obj.push(value)
    for x in range(1, days_array[var_month] + 1):
        value = format(str(x), " >8s")
        stack_obj.push(value)
        if ((x + var_day) % 7 == 0) or (x == days_array[var_month]):
            stack_obj.push("\n")

    size_of_stack = stack_obj.size_of_stack()
    while(size_of_stack > 0):
        data = stack_obj.pop()
        stack_obj_2.push(data)
        size_of_stack = size_of_stack - 1
    stack_obj_2.display()
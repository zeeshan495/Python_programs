

from Utility import *
from QueueLinkedList import *
from Deque import *
class CalenderQueue:
    utility = Utility()
    que = QueueLinkedList()
    que2 = Deque()
    print("enter a month : ")
    var_month = utility.input_int_data()
    print("enter a year : ")
    var_year = utility.input_int_data()
    if  (var_month <= 0) or (var_year <= 0) or (var_month > 12):
        print("check the entered input")
    else:
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
            que.add_rear(value)

        que.add_rear("\n")
        var_day = utility.day_of_week(1, var_month, var_year)
        for x in range(0, var_day):
            value = format("", ">8s")
            que.add_rear(value)
        for x in range(1, days_array[var_month] + 1):
            value = format(str(x), " >8s")
            que.add_rear(value)
            que2.add_rear(value)

            if ((x + var_day) % 7 == 0) or (x == days_array[var_month]):
                que.add_rear("\n")
        que.display_que()

        # for x in range(1, days_array[var_month] + 1):
        #     element1 = que2.pop_front()
        #     element2 = que2.pop_rear()
        #     if element1 == False:
        #         print("elem1 "+str(element2))
        #     elif element2 == False:
        #         print("elem2 "+str(element1-1))
        #     print(que2.pop_front())
        #     print(que2.pop_rear())

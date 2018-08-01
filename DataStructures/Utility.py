
from LinkedList import *
class Utility:

    def print_list(self,f,head):
        file = open(f,"w+")
        if(head is None):
            print("it is empty")
        elif (head.next_node is None):
            file.write(head.data),
            file.write(" ")
        else:
            while(head != None):
                file.write(head.data)
                file.write(" ")
                head = head.next_node

    def input_int_data(self):
        while True:
            try:
                var_input = int(input())
                return var_input
                break
            except NameError:
                print("please enter a integer...try again")
            except OverflowError:
                print("given number is very high...try again")
            except SyntaxError:
                print("check the given input and try again")

    def factorial(self,var_input):
        var_fact = 1
        for x in range(1, var_input+1):
            var_fact = var_fact * x
        return var_fact

    def catalan(self,var_input):
        var_result = self.factorial(2 * var_input) / (self.factorial(var_input + 1) * self.factorial(var_input))
        return var_result

    def is_leap_year(self, year):
        if (year % 4 == 0):
            if (year % 100 == 0):
                if (year % 400 == 0):
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def day_of_week(self,var_day,var_month,var_year):
        var_yo = var_year-(14-var_month) / 12
        var_xo = var_yo + (var_yo / 4) - (var_yo / 100) + (var_yo / 400)
        var_mo = var_month + 12 * ((14-var_month)/12) -2
        var_d = (var_day + var_xo + (31 * var_mo)/12)%7

        return var_d;

    def primenumber(self,var_range):
        my_array = [None]*var_range
        j=0
        for x in range(1,var_range+1):
            count=0
            for num in range(1,x+1):
                if(x%num==0):
                    count=count+1
            if(count==2):
                my_array[j]=x
                j=j+1
        return my_array

    def annagram(self,var_int1,var_int2):
        var_str1 = str(var_int1)
        var_str2 = str(var_int2)
        var_nospace_str1=var_str1.replace(" ","")
        var_nospace_str2=var_str2.replace(" ","")
        if(len(var_str1) != len(var_str2)):
            return False
        else:
            var_lower_str1=var_nospace_str1.lower()
            var_lower_str2=var_nospace_str2.lower()

            char_array_1=list(var_lower_str1)
            char_array_2=list(var_lower_str2)

            char_array_1.sort()
            char_array_2.sort()

            for x in range(0,len(char_array_1)):
                if(char_array_1[x]!= char_array_2[x]):
                    return False
            return True

    def check(self,var_key,annagran_arr):
        for x in range(0,len(annagran_arr)):
            if(annagran_arr[x] == var_key):
                return False
        return True
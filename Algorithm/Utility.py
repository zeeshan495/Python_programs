
import math
class Utility:


    def input_int_data(self):
        while True:
            try:
                var_input = int(input())
                return var_input
                break
            except NameError:
                print("please enter a integer...try again")
            except NameError:
                print("please enter integer value")
            except SyntaxError:
                print("Check the entered input and try again")
            except MemoryError:
                print("Check the entered input and try again")
            except OverflowError:
                print("Entered number is very high")
            except Exception:
                print("exception...something went wrong")

    def input_str_data(self):
        while True:
            try:
                var_input = raw_input()
                return var_input
                break
            except NameError:
                print("please enter a string...try again")
            except NameError:
                print("please enter integer value")
            except SyntaxError:
                print("Check the entered input and try again")
            except MemoryError:
                print("Check the entered input and try again")
            except OverflowError:
                print("Entered number is very high")
            except Exception:
                print("exception...something went wrong")


    def input_float_data(self):
        while True:
            try:
                var_input = float(input())
                return var_input
                break
            except NameError:
                print("please enter a string...try again")
            except NameError:
                print("please enter integer value")
            except SyntaxError:
                print("Check the entered input and try again")
            except MemoryError:
                print("Check the entered input and try again")
            except OverflowError:
                print("Entered number is very high")
            except Exception:
                print("exception...something went wrong")


    def annagram(self,var_str1,var_str2):
        var_nospace_str1=var_str1.replace(" ","")
        var_nospace_str2=var_str2.replace(" ","")
        if(len(var_nospace_str1) != len(var_nospace_str2)):
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

    def primenumber(self,var_range):
        my_array = [None] * var_range
        index=0
        for x in range(1,var_range+1):
            count=0
            for num in range(1,x+1):
                if(x % num == 0):
                    count=count+1
            if(count == 2):
                my_array[index] = x
                index = index+1
        return my_array

    def extend_annagram(self,prime_array):
        var_size=0
        var_j=0
        for x in  range(0,len(prime_array)):
            if(prime_array[x]!=None):
                var_size=var_size+1

        my_array=[None]*var_size
        for x in range(0,len(prime_array)):
            if (prime_array[x] != None):
                my_array[var_j]=prime_array[x]
                var_j=var_j+1
                print(str(prime_array[x])+" "),
        print ("\n")
        var_str1=""
        var_str2=""
        for x in range(0,len(my_array)-1):
            for y in range(x+1,len(my_array)):
                var_str1=my_array[x]
                var_str2=my_array[y]
                flag=self.annagram(str(var_str1),str(var_str2))
                if(flag):
                    print(str(my_array[x])+" "+str(my_array[y]))

    def palindrome(self,prime_array):
        var_size = 0
        var_j = 0
        for x in range(0, len(prime_array)):
            if (prime_array[x] != None):
                var_size = var_size + 1

        my_array = [None] * var_size
        for x in range(0, len(prime_array)):
            if (prime_array[x] != None):
                my_array[var_j] = prime_array[x]
                var_j = var_j + 1
                print(str(my_array[x]) + " "),
        print ("\n")

        for x in range(0,len(my_array)):
            # var_remainder=0
            # var_sum=0
            # var_temp=my_array[x]
            # while(my_array[x]>0):
            #     var_remainder == my_array[x]%10
            #     print(var_remainder)
            #     var_sum = (var_sum * 10) + var_remainder
            #     print(var_sum)
            #     my_array[x] = my_array[x]/10
            #     print(my_array[x])
            var_temp=str(my_array[x])
            if int(var_temp) > 10:
                if(var_temp == var_temp[::-1]):
                    if var_temp > 10:
                        print(str(var_temp)+" palindrome")
                else:
                    print(str(var_temp)+" is not a palindrome")

    def guessing(self,var_low,var_high):
        var_mid=(var_low+var_high)/2
        if(var_mid == var_high):
            return var_mid
        if( 1 == var_mid) or ((var_mid + 1) == var_high):
            print( str(var_mid) + " then enter '1' \n " + str(
                var_high) + " then enter '2'")
        else:
            print(" 1 - "+str(var_mid)+" then enter '1' \n "+str(var_mid + 1)+" - "+str(var_high)+" then enter '2'")
        var_option=self.input_int_data()
        if(var_option == 1):
            return  self.guessing(var_low,var_mid)
        elif(var_option == 2):
            return self.guessing(var_mid+1,var_high)
        else:
            print(" please enter valid option : ")
            return self.guessing(var_low,var_high)

    def binary_search(self,my_array, var_low, var_high, var_key):
        if(var_low <= var_high):
            var_mid = var_low+(var_high-var_low)/2

            if(my_array[var_mid] == var_key):
                print(" key found at : "+str(var_mid+1))
            elif(my_array[var_mid] > var_key):
                self.binary_search(my_array, var_low, var_mid-1, var_key)
            elif(my_array[var_mid] < var_key):
                self.binary_search(my_array, var_mid+1, var_high, var_key)
        else:
            print(" key not found ")

    def insertion_sort(self,my_array):
        for index in range(1,len(my_array)):
            var_key = my_array[index]
            prev_index = index-1
            while prev_index >= 0:
                if(var_key < my_array[prev_index]):
                    my_array[prev_index+1] = my_array[prev_index]
                    my_array[prev_index] = var_key
                    prev_index -=  1
                else:
                    break
        return my_array

    def bubble_sort(self,my_array):
        for x in range(0,len(my_array)):
            for y in range(0, len(my_array)-1 ):
                if(my_array[y] > my_array[y+1]):
                    var_temp = my_array[y]
                    my_array[y] = my_array[y+1]
                    my_array[y+1] = var_temp
        return my_array

    def merge_sort(self,my_array):
        # if given number is only one integer or nothing then it will return.
        if (len(my_array) <= 1):
            return my_array
        # dividing length into half.
        var_mid = len(my_array)/2
        left_array = [None]*var_mid
        right_array=[]
        if (len(my_array) % 2 == 0):
            right_array = [None]*var_mid
        else:
            var_len=var_mid+1
            right_array = [None]*var_len

        # collecting in left array.
        for x in range(0,var_mid):
            left_array[x] = my_array[x]
        # collecting in right array.
        var_x=0
        for y in range(var_mid,len(my_array)):
            if(var_x < len(right_array)):
                right_array[var_x] = my_array[y]
                var_x=var_x+1

        left_array = self.merge_sort(left_array)
        # print(" left_array "+str(left_array))
        right_array = self.merge_sort(right_array)
        # print(" right_array " + str(right_array))
        result_array = self.merge_arrays(left_array,right_array)
        print(" result_array " + str(result_array))
        return result_array

    def merge_arrays(self,left_array,right_array):
        # taking length to initialize arrays
        var_length = len(left_array)+len(right_array)
        result_array = [None]*var_length
        var_left_index = 0
        var_right_index = 0
        var_result_index = 0

        while (var_left_index<len(left_array)) or (var_right_index < len(right_array)):
            if(var_left_index < len(left_array)) and (var_right_index < len(right_array)):
                if(left_array[var_left_index] <= right_array[var_right_index]):
                    result_array[var_result_index] = left_array[var_left_index]
                    var_left_index += 1
                    var_result_index += 1
                else:
                    result_array[var_result_index] = right_array[var_right_index]
                    var_right_index += 1
                    var_result_index += 1

            elif (var_left_index < len(left_array)):
                result_array[var_result_index] = left_array[var_left_index]
                var_left_index = var_left_index + 1
                var_result_index = var_result_index + 1

            elif (var_right_index < len(right_array)):
                result_array[var_result_index] = right_array[var_right_index]
                var_right_index = var_right_index + 1
                var_result_index = var_result_index + 1
        return result_array

    def counting_notes(self,var_amount):
        my_array=[2000,1000,500,100,50,10,5,2,1]
        var_note=0
        for x in range(0,len(my_array)):
            var_number = var_amount/my_array[x]
            padding = format(""," <4s")
            print(" "+str(my_array[x])+""+str(padding)+"x"+str(padding)+""+str(var_number))
            var_amount = var_amount % my_array[x]
            var_note = var_note + var_number
        return var_note

    def day_of_week(self,var_day,var_month,var_year):
        var_yo = var_year - (14-var_month) / 12
        var_x = var_yo + var_yo / 4 - var_yo / 100 + var_yo / 400
        var_mo = var_month + 12 * ((14-var_month)/12) -2
        var_d = (var_day + var_x + 31 * var_mo/12)%7
        return var_d

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

    def celsius(self):
        print("enter fahrenheit temperature : ")
        var_fahrenheit = self.input_int_data()
        var_celsius = (var_fahrenheit - 32) * 5 / 9;
        print(" In celsius : "+str(var_celsius))

    def fahrenheit(self):
        print("enter celsius temperature : ")
        var_celsius = self.input_int_data()
        var_fahrenheit = (var_celsius * 9 / 5) + 32
        print(" In farenheit : "+str(var_fahrenheit))

    def calculation(self,var_principle,var_interest,var_year):
        var_n = 12 * var_year
        if(var_interest == 0):
            var_payment = (var_principle/(var_year*12))
        else:
            var_r = var_interest / (12*100)
            var_payment = (var_principle * var_r) / (1 - math.pow((1+var_r),(-var_n)))
        print(" monthly payment : "+str(var_payment))

    def calculate_sqrt(self,var_input):
        var_temp = var_input
        var_epsilon = 1e-15
        while (abs(var_temp - (var_input / var_temp)) > (var_epsilon * var_temp)):
            var_temp = (((var_input / var_temp) + var_temp) / 2.0)
        print("The square root of "+str(var_input)+" is "+str(var_temp))

    def to_binary(self,var_decimal):
        var_binary = ""
        var_rem = 0
        while (var_decimal > 0) :
            var_rem = var_decimal % 2
            var_binary = str(var_rem) + var_binary
            var_decimal = var_decimal / 2
        while (len(var_binary) < 8) :
            var_binary = str(0) + var_binary
        return var_binary

    def swap_nibbles(self,var_binary):
        var_temp = ""
        var_mid = len(var_binary) / 2
        var_temp = var_temp + var_binary[var_mid:]
        var_temp = var_temp + var_binary[:var_mid]
        return var_temp

    def to_decimal(self,var_binary):
        var_sum = 0
        var_temp = ""
        char_array = list(var_binary)
        var_power = len(char_array)-1
        print(" ")
        for x in range(0,len(char_array)):
            var_index_value =char_array[x]
            var_sum = var_sum + (int(var_index_value) * math.pow(2,var_power))
            var_power = var_power-1
        var_temp = var_temp + str(var_sum)
        return var_temp
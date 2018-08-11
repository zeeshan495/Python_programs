
import re
import math
import random
from datetime import *
class Utility:

    def input_int_data(self):
        while True:
            try:
                var_input = int(input())
                return var_input
                break
            except NameError:
                print("please enter a integer...try again")

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

    def regex_replace(self,main_str):
        print("enter a sur name")
        sur_name = self.input_str_data()
        if re.search("[\wA-Za-z]{2,20}", sur_name):
            main_str = main_str.replace("<<name>>",sur_name)
        else:
            print("invalid input......try again : ")
            return False

        print("enter a full name")
        full_name = self.input_str_data()
        if re.search("[\wA-Za-z]{2,20}\s\w[A-Za-z]{2,20}", full_name):
            main_str = main_str.replace("<<full name>>", full_name)
        else:
            print("invalid input......try again : ")
            return False

        print("enter a mobile number : ")
        mobile_num = self.input_str_data()
        if re.search("\w{10}", mobile_num):
            main_str = main_str.replace("xxxxxxxxxx", mobile_num)
        else:
            print("invalid input......try again : ")
            return False

        date = datetime.now()
        main_str = main_str.replace("01/01/2016", str(date)[:10])
        print(main_str)

    def deck_of_cards2(self):
        deck_list = []
        for x in range(36):
            deck_list.append(x)
        my_list = []
        for x in range(4):
                my_list.append([])
        suits_arr = ["Spades", "Hearts", "Diamonds", "Clubs"]
        ranks_arr = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        # Shuffle the cards
        for x in range(len(deck_list)):
            var_index = random.randint(0,len(deck_list))
            temp = deck_list[x]
            deck_list[x] = deck_list[var_index]
            deck_list[var_index] = temp
        #collecting all cards
        row = 0
        column = 0
        for x in range(36):
            suit = suits_arr[deck_list[x]/13]
            rank = ranks_arr[deck_list[x]%13]

            my_list[row][column].append(str(rank) +" of " +str(suit))
            row = row + 1
            if ((x+1)%9 == 0):
                row = 0
                column = column + 1
        return my_list




    def sort_cards2(self,deck_arr, column):
        char_arr = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '1', 'J', 'Q', 'K']
        index = 0
        sort_arr = [None] * 9

        for x in range(len(char_arr)):
            for y in range(9):
                temp = deck_arr[column][y][0]

                if (char_arr[x] == temp):
                    sort_arr[index] = deck_arr[column][y]
                    index = index + 1
        return sort_arr

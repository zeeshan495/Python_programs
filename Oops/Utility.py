
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

    def regex_replace(main_str):
        print("enter a sur name")
        sur_name = utility.input_str_data()
        if re.search("[\wA-Za-z]{2,20}\s\w[A-Za-z]{2,20}", sur_name):
            main_str.re
        else:
            return False

from Utility import *
from RegexInfo import *
from RegexReplace import *
class Regex_main:

    utility = Utility()
    info_obj = RegexInfo()
    main_str = "Hello <<name>>, We have your full name as <<full name>> in our system. your contact number is 91-xxxxxxxxxx. Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016."
    regex_obj = RegexReplace(main_str)

    while True:
        print("enter a sur name")
        info_obj.set__sur_name(utility.input_str_data())
        print("enter a full name")
        info_obj.set__full_name(utility.input_str_data())
        print("enter a mobile number : ")
        info_obj.set__mobile_num(utility.input_int_data())
        date = datetime.now()
        info_obj.set__date(str(date)[:20])
        flag = regex_obj.regex_replace(info_obj)

        if (flag == True):
            regex_obj.display()
            break
        # else:
        #     print("Please enter data properly")
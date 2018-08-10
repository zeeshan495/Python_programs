

from Utility import *
class UserName:

    utility = Utility()
    print("please enter a name")
    input_string = utility.input_str_data()
    main_string="Hello <<UserName>>, How are you?"
    output_string = utility.replacing(input_string,main_string)
    print(output_string)


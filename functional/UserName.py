

from Utility import *
class UserName:

    obj=Utility()
    input_string=raw_input("please enter a name")
    main_string="Hello <<UserName>>, How are you?"
    output_string=obj.replacing(input_string,main_string)
    print(output_string)


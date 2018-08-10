
from HashFunction import *
from Utility import *
class HashMain:
    list = HashFunction()
    utility = Utility()
    file = open("HashingFile.txt", "r")

    if file.mode == 'r':
        contents = file.read()
    print(contents)

    temp_array = contents.split(" ")
    my_array = []

    # for removing spaces
    for x in range(0, len(temp_array)):
        if (temp_array[x] != ""):
            my_array.append(temp_array[x])

    for x in range(0, len(my_array)):
        list.add(my_array[x])

    list.display()

    print("please enter a number")
    new_word = utility.input_int_data()

    status = list.search(new_word)
    if status == False:
        list.insert(new_word)
    else:
        list.delete(new_word)

    list.display()

    node = list.table
    print(node)
    list.print_list("HashingFile.txt", node)

    file.close()
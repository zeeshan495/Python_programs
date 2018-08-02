


from LinkedList import *
from Utility import *

def main():
        list = LinkedList()
        utility = Utility()
        file_name = "Ordered.txt"
        file = open(file_name, "r")
        if file.mode == 'r':
            contents = file.read()
        print(contents)
        temp_array = contents.split(" ")
        my_array = []

        # for removing spaces
        for x in range(0,len(temp_array)):
            if(temp_array[x] != ""):
                my_array.append(temp_array[x])

        print("please enter a number")
        new_word = utility.input_str_data()

        for x in range(0, len(my_array)):
            list.add(my_array[x])
        flag = list.search(new_word)
        if (flag == False):
            list.add_order(new_word)
        else:
            list.delete(new_word)
        list.display()
        node = list.head
        utility.print_list(file_name, node)

        file.close()

class OrderedMain:

    if __name__ == '__main__':
        main()

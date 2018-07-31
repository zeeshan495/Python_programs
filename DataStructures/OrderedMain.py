


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
        my_array = contents.split(" ")
        new_word = raw_input("please enter a word : ")

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

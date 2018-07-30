
from LinkedList import *

def main():
    list = LinkedList()
    file_name = "Unordered.txt"
    file = open(file_name, "r")
    if file.mode == 'r':
        contents = file.read()
    print(contents)
    my_array = contents.split(" ")
    new_word = raw_input("please enter a word : ")
    list.operation(my_array, new_word, file_name)
    file.close()


class UnorderedMain:

    if __name__ == '__main__':
        main()

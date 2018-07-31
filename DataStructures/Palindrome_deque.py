
from Deque import *
class Palindrome_deque:
    deq = Deque()
    var_input = raw_input("please enter a string to check palindrome : ")
    my_array = list(var_input)
    for x in range(0,len(my_array)):
        deq.add_rear(my_array[x])
    deq.operation()

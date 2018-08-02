

from Queue import *
from Utility import *

class Banking:

    global que,utility

    utility = Utility()
    que = Queue(10, 100000)
print("\t***welcome to our bank***")
print("first add in queue...then go for transactions :\n")

def counter():
    print("Enter the 1 amount to deposit \nEnter the 2 amount to withdraw\n")
    choice = utility.input_int_data()

    if(choice == 1) and (que.bank_cash>=0):
        print("enter amount to deposit : ")
        deposit = utility.input_int_data()
        que.bank_cash = que.bank_cash + deposit
        print("present bank cash "+str(que.bank_cash))
        que.dequeue()
        operation()
    elif(choice == 2) and (que.bank_cash>=0):
        print("enter amount to withdraw : ")
        withdraw = utility.input_int_data()
        que.bank_cash = que.bank_cash - withdraw
        if(que.bank_cash < 0):
            print("insufficient balance ")
            que.bank_cash = que.bank_cash + withdraw
            counter()
        print("present cash bank '"+str(que.bank_cash)+"'")
        que.dequeue()
        operation()
    elif(choice != 1) and (choice !=2):
        print("enter a valid cash ")
    else:
        print("bank balance is insufficient")
        que.dequeue()
        operation()

def operation():
    print("enter 1 to add in a queue \nEnter 2 for transaction \nEnter 3 for present customers in queue \nEnter 4 for Bank balance\n")
    choice = utility.input_int_data()
    if(choice == 1):
        result = que.enqueue(1)
        if(result == False):
            print("queue was full,go for transaction")
        else:
            print("you are added in queue ")
            operation()
    elif(choice == 2):
        var_isempty=que.is_empty()
        if(var_isempty):
            print("queue was empty,first add in queue")
            operation()
        else:
            counter()
    elif(choice == 3):
        print("present customers in queue : "+str(que.queue_size))
        operation()

    elif(choice == 4):
        print("present cash bank '" + str(que.bank_cash)+"'")
        operation()
    else:
        print("invalid number....try again")
        operation()

operation()

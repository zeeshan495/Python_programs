

class Queue:

    bank_cash = 0
    rare = -1
    front = 0
    queue_size = 0
    def __init__(self,queue_length,initial_cash):
        self.size = queue_length
        self.bank_cash = initial_cash
        self.queue_array = [None]*self.size

    def enqueue(self,element):
        if(self.rare == self.size-1):
            print("queue was full insertion not possible ")
            return False
        else:
            self.rare = self.rare + 1
            self.queue_array[self.rare] = element
            self.queue_size = self.queue_size + 1
            return True

    def dequeue(self):
        if(self.rare == -1 or self.front > self.rare):
            print("queue was empty...deletion not possible")
        else:
            self.front = self.front + 1
            self.queue_size = self.queue_size - 1

    def display(self):
        if (self.rare == -1 or self.front > self.rare):
            print("queue was empty...insertion not possible")
        else:
            for x in range(self.front,self.rare+1):
                print(str(self.queue_array[x])+" "),
            print("\n")

    def is_empty(self):
        if (self.rare == -1 or self.front > self.rare):
            return True
        else:
            return False

    def size_is(self):
        return self.queue_size


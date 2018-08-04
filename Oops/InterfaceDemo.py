

class shape(object):

    def __area__(self):
        print("area...")

    def __perimeter__(self):
        print("perimeter......")

class rectangle(shape):

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def __area__(self):
        return self.length*self.width


    def __perimeter__(self):
        return self.length * self.length

    def __area__(self,len=None):
        if(len is not None):
            print("over load done")
        else:
            print("without parameters")


r = rectangle(2,4)


print  r.__area__()
print  r.__area__(3)


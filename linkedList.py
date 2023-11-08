class linkedList:
    def __init__(self, value):
        self.val = value
        self.next = None

    def add(self, value):
        if (self.next):
            self.next.add(value)
        else:
            self.next = linkedList(value)

    def find(self, value):
        if (self.val == value):
            print('value is found')
            return value
        if (self.next):
            return self.next.find(value)
        else:
            print('value not found!')
            return 'value not found!'

list = linkedList(1) # 1 => x

list.add(2) # 1 => 2 => x

list.add(3) # 1 => 2 => 3 => x 

list.find(4) # should value be not found
list.find(2) # value should be found 


# print('dd' != not def)

class que:
    def __init__(self, value):
        self.list = [value]
    def push(self, val):
        self.list.append(val)
        print('pushed in queue')

    def unque(self):
        res = self.list[0]
        del self.list[0]
        return res
        
            
myQue = que(1) # list => [1]
myQue.push(2) # list => [1, 2]
myQue.push(3) # list => [1, 2, 3]

myQue.unque() # list => [2, 3]

print(myQue.list)
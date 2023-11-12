class tree:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
    def add(self, val):
        if(val > self.val):
            if(self.right):
                return self.right.add(val)
            else:
                self.right = tree(val)
                return val
            
        if(val < self.val):
            if(self.left):
                return self.left.add(val)
            else:
                self.left = tree(val)
                return val

    def find(self, val):
        if (val == self.val):
            print(val, 'is found!!')
            return val
        elif((val > self.val) and (self.right)):
            return self.right.find(val)
            
        elif((val < self.val) and (self.left)):
            return self.left.find(val)
        else:
            print(val,'is not found!!')
            return None
            
        
mytree = tree(5)

mytree.add(9)
mytree.add(4)
mytree.add(7)

#                5
#               / \
#              /   \
#             4     9
#                  /
#                 7

print(mytree.right.val)
print(mytree.left.val) 
print(mytree.right.left.val)
mytree.find(8)
mytree.find(9)
mytree.find(4)
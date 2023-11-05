print('hello world')
class stackExample:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)
    def length(self):
        return len(self.data)
    def pop(self):
        return self.data.pop()

stack=stackExample() # init stack

stack.push(1) # current stack [1]
stack.push(3) # current stack [1, 3]

print(stack.pop()) # current stack [1]
stack.push(2) # current stack [1, 2]
print(stack.length()) # prints 2 
print(stack.data)
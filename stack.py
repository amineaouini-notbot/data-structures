print('hello world')
class stackExample:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)
    def length(self):
        return len(self.data)
    
stack=stackExample()

stack.push(1)
stack.push(3)

print(stack.data)
print(stack.length())
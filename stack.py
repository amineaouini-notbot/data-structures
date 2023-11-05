print('hello world')
class stackExample:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    
stack=stackExample()

stack.push(1)

print(stack.data)
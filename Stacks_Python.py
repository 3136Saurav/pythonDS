#Implementing Stack in Python

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack()
print(s.isEmpty())
s.push('Hello')
s.push(5)
s.push(58.3)
print(s.peek())
s.pop()
print(s.peek())
print(s.isEmpty())
s.push('Burger')
print(s.size())
print(s.peek())

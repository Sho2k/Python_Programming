"""Program 66: Stack Using a List"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("The stack is empty.")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Stack (bottom to top):", self.items)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

stack.display()
print("Top element:", stack.peek())
print("Removed:", stack.pop())
stack.display()

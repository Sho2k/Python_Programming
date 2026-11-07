"""Program 67: Queue Using collections.deque"""

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Queue (front to rear):", list(self.items))

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.display()
print("Removed:", queue.dequeue())
queue.display()

"""Program 68: Singly Linked List"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        values = []

        while current is not None:
            values.append(str(current.data))
            current = current.next

        print(" -> ".join(values) if values else "Linked list is empty.")

    def search(self, target):
        current = self.head
        while current is not None:
            if current.data == target:
                return True
            current = current.next
        return False

linked_list = LinkedList()
for value in [10, 20, 30, 40]:
    linked_list.append(value)

linked_list.display()
print("Search for 30:", "Found" if linked_list.search(30) else "Not found")
print("Search for 50:", "Found" if linked_list.search(50) else "Not found")

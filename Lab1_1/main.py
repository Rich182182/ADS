class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = []

    def isFull(self):
        return len(self.array) == self.capacity

    def isEmpty(self):
        return len(self.array) == 0

    def enqueue(self, item):
        if not self.isFull():
            self.array.append(item)
            return True
        return False

    def dequeue(self):
        if not self.isEmpty():
            return self.array.pop(0)

    def display(self):
        print(self.array)


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def insert(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove_node(self, node):
        if self.isEmpty() or not node:
            return
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif node == self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)


def main():
    #1
    queue = ArrayQueue(5)
    for i in [10, 20, 30, 40]:
        queue.enqueue(i)
    queue.display()

    queue.dequeue()
    queue.dequeue()
    queue.display()
    #2
    dll = DoublyLinkedList()
    for s in ["15", "22", "33", "42", "55", "8"]:
        dll.insert(s)
    dll.display()

    dll.remove_node(dll.head)
    dll.display()
    #3
    current = dll.head
    while current:
        next_node = current.next
        num_val = int(current.data)
        if num_val % 2 == 0:
            if queue.enqueue(num_val):
                dll.remove_node(current)
        current = next_node

    dll.display()
    queue.display()


if __name__ == "__main__":
    main()
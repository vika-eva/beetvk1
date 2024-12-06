
class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        n = self.head
        s = '['
        while n.next:
            s += str(n.data) + ', '
            n = n.next
        s += str(n.data) + ']'
        return s

    def is_empty(self):
        return self.head is None and self.tail is None

    def append(self, data):
        new_node = QueueNode(data)
        if self.head is None:
            self.head = self.tail = new_node
            self.size += 1
            return

        self.tail.next = new_node
        self.tail = new_node


    def pop(self):
        if self.is_empty():
            print('Queue is empty')
            return
        temp = self.head
        self.head = self.head.next
        self.size -= 1
        if self.head is None:
            self.tail = None

    def get_head(self):
        if self.is_empty():
            print("Queue is empty")
            return float('-inf')
        return self.head.data

    def get_tail(self):
        if self.is_empty():
            print("Queue is empty")
            return float('inf')
        return self.tail.data

d = LinkedListQueue()
d.append(10)
d.append(20)
d.append(30)
print(d)
print(d.get_head())
print(d.get_tail())
d.pop()
print(d)
class StackNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedStack:
    def __init__(self, size_max):
        self.root = None
        self.size = 0
        self.size_max = size_max
        if self.size_max <= 0:
            raise ValueError("Size must be greater than 0")

    def __str__(self):
        n = self.root
        s = '['
        while n.next_node:
            s += str(n.data) + ', '
            n = n.next_node
        s += str(n.data) + ']'
        return s

    def is_empty(self):
        return self.root is None

    def push_1(self, data):
        new_node = StackNode(data)
        new_node.next_node = self.root
        self.root = new_node

    def pop_1(self):
        if self.is_empty():
            return None
        pop_node = self.root.data
        self.root = self.root.next_node
        return pop_node

    def peek(self):
        if self.is_empty():
            return None
        return self.root.data


s = LinkedStack(4)
print(s.is_empty())
s.push_1(1)
s.push_1(2)
s.push_1(3)
s.push_1(4)
s.push_1(5)
print(s)
s.is_empty()
s.pop_1()
print(s)
s.pop_1()
print('-----')
s.peek()
print(s)


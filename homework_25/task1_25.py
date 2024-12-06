
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def __str__(self):
        n = self.root
        s = '['
        while n.next_node:
            s += str(n.data) + ', '
            n = n.next_node
        s += str(n.data) + ']'
        return s

    def append(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        current = self.root
        while current.next_node:
            current = current.next_node
        current.next_node = new_node
        self.size += 1
        return

    def insert(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next_node = self.root
            self.root = new_node
            return
        current = self.root
        current_index = 0
        while current_index and current < index -1:
            current = current.next_node
            current_index += 1
        if not current:
            raise IndexError

        new_node.next_node = current.next_node
        current.next_node = new_node

    def get_index(self, data):
        index = 0
        current = self.root
        found = False
        while current is not None and not found:
            if current.data == data:
                found = True
            else:
                current = current.next_node
                index += 1
                print(index)
        if not found:
            raise ValueError(f'{data} not in list')
        return index




    def pop(self, index):
        current_node = self.root
        previous_node = None
        pop_index = 0
        while current_node:
            if pop_index == index:
                if previous_node:
                    previous_node.next_node = current_node.next_node
                else:
                    self.root = current_node.next_node
                self.size -= 1
                print(current_node.data)
                return current_node.data
            else:
                pop_index += 1
                previous_node = current_node
                current_node = current_node.next_node
        return False

    def slice(self, start, end):
        if start >= end:
            raise ValueError('Start index out of range')
        if end > self.size:
            raise ValueError('End index out of range')
        index = 0
        current_node = self.root
        data_list = []
        while index != end:
            if start <= index:
                data_list.append(current_node.data)
            index +=1
            current_node = current_node.next_node
        data_list.reverse()

        for i, n_data in enumerate(data_list):
            new_node = Node(n_data)
            if i == 0:
                new_node.next_node = None
                self.root = new_node
            else:
                new_node.next_node = self.root
                self.root = new_node
        return self





x = LinkedList()
x.append(1)
x.append(2)
x.append(3)
x.append(4)
x.append(5)
x.append(6)
x.append(7)
print(x)
print(x.get_index(2))
print('-----')
print(x.pop(2))
print(x)
print(x.slice(0, 5))

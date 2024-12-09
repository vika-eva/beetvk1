from task_1_24 import Stack

class StackOne(Stack):
    def __init__(self):
        self.items = []
        super().__init__()

    def get_el(self, element):
        if element not in self.items:
            raise ValueError(f"Element {element} not in Stack")
        data_list = []
        for item in self.items:
            if item == element:
                continue
            data_list.append(item)
        self.items = data_list
        print(data_list)
        print(element)
        return element

class MyQueue:
    def __init__(self):
        self.items = []

    def append_q(self, element):
        self.items.append(element)

    def pop_q(self):
        self.items.pop(0)

    def get_from_q(self, element):
        if element not in self.items:
            raise ValueError(f'Element {element} not in queue')
        list_q = []
        for el in self.items:
            if el == element:
                continue
            list_q.append(el)
        #self.items = list_q
        return element



ex = StackOne()
ex.push('h')
ex.push('e')
ex.push('l')
ex.push('o')
ex.push(1)
ex.show()
print('----')
ex.get_el('o')
print('----')
ex.show()


f = MyQueue()
f.append_q('a')
f.append_q('b')
f.append_q('c')
print(f.items)
f.get_from_q('a')
print(f.items)





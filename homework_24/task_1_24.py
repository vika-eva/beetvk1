
class Stack:
    def __init__(self):
        self.items = []

    def push(self, new_item):
        self.items.append(new_item)

    def pop(self):
        return self.items.pop()

    def empty(self):
        return self.items == []

    def show(self):
        for new_item in reversed(self.items):
            print(new_item)

    def get(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)

    def __ne__(self, other):
        return self.items == other

    def __eq__(self, other):
        return self.items == other

    def __len__(self):
        return len(self.items)

    #def get_el(self, element):
    #    if element not in self.items:
    #        raise ValueError(f"Element {element} not in Stack")
    #    data_list = []
    #    for item in self.items:
    #        if item == element:
    #            continue
    #        data_list.append(item)
        #self.items = data_list
    #    print(self.items)
    #    print(element)
    #    return element

    def rev(self, element):
        list_1 = []
        for item in element:
            list_1.append(item)
        element = ''
        while list_1:
            element += list_1.pop()
        return element

def bottom(stack, value):
    if stack.empty():
        stack.push(value)
    else:
        popped = stack.pop()
        bottom(stack, value)
        stack.push(popped)

def reverse_1(stack):
    if stack.empty():
        pass
    else:
        popped = stack.pop()
        reverse_1(stack)
        bottom(stack, popped)

def reverse_2(s):
    stack = []
    for i in s:
        stack.append(i)
    s = ""
    while stack:
        s += stack.pop()
    return s



stk = Stack()
stk.push(1)
stk.push('banana')
stk.push(2)
stk.push(3)
stk.push('apple')
stk.show()
print(20 * '-')
#stk.get_el('banana')
print(20 * '-')
stk.show()
reverse_1(stk)
print('--------')
str = 'apple'
revs = reverse_2(str)
print(stk.rev('banana'))


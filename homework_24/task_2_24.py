class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get(self):
        return self.items[-1]

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def is_balanced(equation):
    stack = Stack()

    for c in equation:
        if c == '(' or c == '[' or c == '{':
            stack.push(c)
            print(stack)
        elif c == ')' or c == ']' or c == '}':
            if not stack:
                return False
            stack.pop()
            print(stack)
    return len(stack) == 0

x = '([]{})'
res = is_balanced(x)
print(res)
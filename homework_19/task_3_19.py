from collections.abc import Iterator

class MyIterator(Iterator):
    def __init__(self, lists: list, start=0, end=0):
        self.lists = lists
        self.counter = 0
        self.elem = lists
        self.start = start
        self.end = end


    def __next__(self):
        if self.start < self.end:
            self.start += 1
            print(f'{self.start}: {self.elem[self.start]}')
            return self.elem[self.start]

        if self.counter < len(self.lists):
            element = self.lists[self.counter]
            print(f'{self.counter} - {self.lists[self.counter]}')
            self.counter += 1
            return element
        raise StopIteration

x = MyIterator("apple, sun, fruit", 6, 10)
for i in x:
    print()
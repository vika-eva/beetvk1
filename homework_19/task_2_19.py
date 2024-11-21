from collections.abc import Iterator

class InRange(Iterator):

    def __init__(self, start: int, end: int, step=1):
        self.start = start
        self.end = end
        self.step = step


    def __next__(self):
        if self.start <= self.end:
            num = self.start
            self.start += self.step
            return num
        else:
            raise StopIteration


for num in InRange(1, 10, 3):
    print(num)

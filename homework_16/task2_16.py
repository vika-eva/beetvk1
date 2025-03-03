import math

class Mathematician:

    def __init__(self, value):
        self.value = value


    def square_nums(self):
        self.value = list(map(lambda x: x ** 2, self.value))
        print(self.value)



    def remove_positives(self):
        self.value = [i for i in self.value if i < 0]
        print(self.value)


    def filter_leaps(self):
        self.value = [i for i in self.value if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0)]
        print(self.value)


n = Mathematician([7, 11, 5, 4])
n.square_nums()
x = Mathematician([26, -11, -8, 13, -90])
x.remove_positives()
m = Mathematician([2001, 1884, 1995, 2003, 2020])
m.filter_leaps()




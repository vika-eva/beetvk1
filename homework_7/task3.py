import math
list1 = []
i = tuple(range(1, 11))
j = tuple([x**2 for x in i])
list1.append(i + j)
print(list1)

# or

i1 = tuple(range(1, 11))
j1 = tuple([x**2 for x in i1])
print([i1 + j1])

# or

list3 = [tuple(range(1, 11)), tuple(x**2 for x in range(1, 11))]
print(list3)

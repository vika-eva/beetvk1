def bubble_sort(array, arg = 0):
    data = array.copy()
    n = len(data)
    if arg == 1:
        for i in range(n - 1):
            for j in range(n - i - 1):
                if data[j] > data[j + 1]:
                    temp = data[j + 1]
                    data[j + 1] = data[j]
                    data[j] = temp
    else:
        for i in range(n - 1):
            for j in range(n - i - 1):
                if data[j] < data[j + 1]:
                    temp = data[j + 1]
                    data[j + 1] = data[j]
                    data[j] = temp
    return data


x = [5, 1, 2, 8, 6, 10, 45, 34, 100, 87]
print(bubble_sort(x, 1))
print(bubble_sort(x))

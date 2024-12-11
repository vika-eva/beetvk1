# o(log n), o log n
def binary_recursive(arr, x, start=0, end=None):
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_recursive(arr, x, mid + 1, end)
        else:
            return binary_recursive(arr, x, start, mid - 1)
    return False

# o(log n), o(1)
def binary_search(arr, x, low, high):
    tries = 0

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return f'index {mid}, tries {tries}'
        elif arr[mid] < x:
            low = mid + 1
            tries += 1
        elif arr[mid] > x:
            high = mid - 1
            tries += 1
    return False


d = [1, 4, 8, 15, 20]
print(binary_recursive(d, 4, 0, end=len(d) - 1))

c = [1, 2, 4, 5, 7, 9, 11]
print(binary_search(c, 9, 0, high=len(c) - 1))
print(binary_search(c, 4, 0, len(c) - 1))

def search(arr, x):
    return binary_recursive(arr, x, 0, len(arr) - 1)
arr = [2, 4, 1, 78, 90, 54]
print(search(sorted(arr), 78))
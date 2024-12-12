import random
import time

# worst o(n^2), average o(n log n)
def partition(arr, low, high):
    pivot_p = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot_p:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1
# для невеликих рахує швидше
def quick_sort(arr):
    quick_sort_help(arr, 0, len(arr) - 1)
#
def quick_sort_help(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort_help(arr, low, pivot - 1)
        quick_sort_help(arr, pivot + 1, high)

d = [4, 10, -5, 9, 1, -2, 3, 100, 76, 44, 98]
print(d)
quick_sort(d)
partition(d, 0, len(d) - 1)
print(d)
print(d)



# time complexity o(n log n), memory o(n),
def quick_sort2(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = [x for x in array[1:] if x < pivot]
        right = [x for x in array[1:] if x >= pivot]
        return quick_sort2(left) + [pivot] + quick_sort2(right)



quick_sort2(d)
print(d)

def gen_random(n):
    return [random.randint(1, 1000) for _ in range(n)]


n = 1000

random_num = gen_random(n)
print('start for quick_sort')
start_qs = time.time()
quick_sort(random_num)
print(time.time() - start_qs)

rand_num = gen_random(n)
print('start for quick_sort2')
start_qs_2 = time.time()
quick_sort2(rand_num)
print(time.time() - start_qs_2)







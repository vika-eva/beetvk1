def merge(arr, left, mid, right):
    left_arr = mid - left + 1
    right_arr = right - mid

    temp_left = [0] * left_arr
    temp_right = [0] * right_arr

    for i in range(left_arr):
        temp_left[i] = arr[left + i]
    for j in range(right_arr):
        temp_right[j] = arr[mid + j + 1]

    i, j = 0, 0
    min_index = left

    while i < left_arr and j < right_arr:
        if temp_left[i] <= temp_right[j]:
            arr[min_index] = temp_left[i]
            i += 1
        else:
            arr[min_index] = temp_right[j]
            j += 1
        min_index += 1

    while i < left_arr:
        arr[min_index] = temp_left[i]
        i += 1
        min_index += 1

    while j < right_arr:
        arr[min_index] = temp_right[j]
        j += 1
        min_index += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

d = [11, 45, 30, 6, 12]
merge_sort(d, 0, len(d) - 1)
print(d)
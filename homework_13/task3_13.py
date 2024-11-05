

def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(nums: list, func1, func2):
    num = all(map(lambda x: x > 0, nums))
    return func1(nums) if num else func2(nums)

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

if __name__ == '__main__':
    assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
    assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]


#or

def choose_func(nums: list, func1, func2):
    num = all(map(lambda x: x > 0, nums))
    if num > 0:
        return func1(nums)
    #if len(list(filter(lambda x: x < 0, nums))):
    return func2(nums)

if __name__ == '__main__':
    assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
    assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]





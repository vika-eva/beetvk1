import math
import operator
from statistics import multimode
from operator import sub, truediv
from functools import reduce


def make_operation(operators:str, *nums:int):
    if operators == "+":
        return sum(nums)
    if operators == "-":
        return reduce(sub, nums)
    if operators == "*":
        return reduce((lambda x, y: x * y), nums)
    else:
        return "error"

print(make_operation("+", 7, 7, 2))
print(make_operation("-", 5, 5, -10, -20))
print(make_operation("*", 7, 6))


#--------

def make_operat(op, *numbers: list[int | float]):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul
        }
    result = numbers[0]
    for number in range(1, len(numbers)):
       result = operators[op](result, numbers[number])
    print(result)
    return result

make_operat("+", [7, 7, 2])
make_operat('-', [5, 5, -10, -20])
make_operat('*', [7, 6])

#def make_operation(operators, *nums:int):
#    if operators == "+":
#        return nums[0] + nums[1] + nums[2]
#    if operators == "-":
#        return nums[0] - nums[1] - nums[2] - nums[3]
#    if operators == "*":
#        return nums[0] * nums[1]
#    else:
#        return "error"
#print(make_operation("+", 7, 7, 2))
#print(make_operation("-", 5, 5, -10, -20))
#print(make_operation("*", 7, 6))



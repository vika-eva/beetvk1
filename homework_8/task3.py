def make_operation(operators, *nums:int):
    if operators == "+":
        return nums[0] + nums[1] + nums[2]
    if operators == "-":
        return nums[0] - nums[1] - nums[2] - nums[3]
    if operators == "*":
        return nums[0] * nums[1]
    else:
        return "error"
print(make_operation("+", 7, 7, 2))
print(make_operation("-", 5, 5, -10, -20))
print(make_operation("*", 7, 6))

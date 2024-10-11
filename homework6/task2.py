import random

random_list = [random.randint(1, 10) for _ in range(10)]
random_1_list = [random.randint(1, 10) for _ in range(10)]
print(random_list)
print(random_1_list)
while True:
    print([set (random_list) & set (random_1_list)])
    break




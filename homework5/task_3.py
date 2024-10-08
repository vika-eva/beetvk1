import random

my_string = input("Enter: ")
char_list = list(my_string)
counter = 0
while counter < len(char_list):
    random.shuffle(char_list)
    first_list = "".join(char_list)
    print(first_list)
    counter += 1



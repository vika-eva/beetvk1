import random

a = random.randint(1,10)
counter = 0
while True:
    x = int(input("Enter a number from 1 to 10: "))
    counter += 1
    if x == a:
        print("You vin")
        break
    print("Error, try again")
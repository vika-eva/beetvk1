
def funct_input(a, b):
    x = (a ** 2) / b
    return x
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print((a ** 2) / b)
except (ValueError, TypeError, ZeroDivisionError):
    print("error")




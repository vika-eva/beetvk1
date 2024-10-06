x = input()
if len(x) < 2:
    print("")
elif len(x) > 2 or len(x) == 2:
    print(x[0:2] + x[-2:])


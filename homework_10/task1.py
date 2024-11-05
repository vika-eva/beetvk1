def oops():
    raise IndexError


def oops_1():
    try:
        oops()
    except IndexError:
        print("Oops!")
    #raise IndexError










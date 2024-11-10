import functools


def logger(func):
    @functools.wraps(func)
    def wrapper(*args):
        print(f"{func.__name__} called {args}")
        #return func(*args)
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(add(4, 5))
print(square_all(4, 5))
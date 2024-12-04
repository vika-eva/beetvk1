import functools

class TypeDecorators:
    #def __init__(self, type_):
    #    self.type_ = type_

    @staticmethod
    def to_int(func):
        @functools.wraps(func)
        def wrapper(*args):
            res = func(*args)
            try:
                return f"{int(res)}"
            except (ValueError, TypeError):
                print("Error, not possible to convert the result")
                return res
        return wrapper

    @staticmethod
    def to_str(func):
        @functools.wraps(func)
        def wrapper(*args):
            res = func(*args)
            try:
                return f"{str(res)}"
            except (ValueError, TypeError):
                print("Error, not possible to convert the result")
                return res
        return wrapper


    @staticmethod
    def to_bool(func):
        @functools.wraps(func)
        def wrapper(*args):
            res = func(*args)
            try:
                return f"{bool(res)}"
            except (ValueError, TypeError):
                print("Error, not possible to convert the result")
                return res
        return wrapper


    @staticmethod
    def to_float(func):
        @functools.wraps(func)
        def wrapper(*args):
            res = func(*args)
            try:
                return f"{float(res)}"
            except (ValueError, TypeError):
                print("Error, not possible to convert the result")
                return res
        return wrapper


@TypeDecorators.to_int
def vika(value):
    return value

print(vika("8765432"))
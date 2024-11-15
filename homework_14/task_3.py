import functools


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            result = func(*args)
            print(*args)
            if len(args[0]) > max_length and args[0] != type_:
                return False
            if contains:
                for s in contains:
                    if s not in args[0]:
                        return False
            return result
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan("S@SH05"))
#assert create_slogan('johndoe05@gmail.com') is False
#assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

import functools

def stop_words(words: list):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            result = func(*args)
            for word in words:
                if word in result:
                    result = result.replace(word, "*")
            return result
        return wrapper
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan("steve"))
#assert create_slogan("Steve") == "Steve drinks * in his brand new *!"


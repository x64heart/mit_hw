def debug(func):
    def wrapper(*args, **kwargs):
        print(f'function {func.__name__} called, {args=},{kwargs=}')
        return_value = func(*args, **kwargs)
        print(f'{return_value=}')
        return return_value

    return wrapper


@debug
def foo(x: int):
    return x


@debug
def baz(y: list):
    return sorted(y)


foo(2)
baz([4, 3, 5, 7, 2])

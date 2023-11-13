# Задание 6
def foo(n: int) -> int:
    return sum([int(x) for x in [str(n) * i for i in range(1, 4)]])


print(foo(3))

# Задание 6
print('*' * 50)


def func(n: int):
    step = (n + 10) // 5
    ranges = [
        lambda x: 2 * x,
        lambda x: 2 * abs(x) - 1,
        lambda x: x * x,
        lambda x: 2 * x
    ]
    if step < 0 or step > len(ranges):
        return None
    return ranges[step](n)


for i in range(-11, 10):
    print(func(i))

# Домашнее задание
print('*' * 50)


def func(something):
    def foo_str(s: str):
        return len([c for c in s if c.isalpha()])

    def foo_int(i: int):
        return sum([int(x) for x in str(i) if int(x) % 2])

    def foo_tuple(t: tuple):
        return len([word for word in t if type(word) == str and word.isalpha()])

    def foo_list(l: list):
        letters = len([x for x in l if type(x) == str and x.isalpha() and len(x) == 1])
        digits = len([x for x in l if str(x).isdigit() and len(str(x)) == 1])
        return letters, digits

    functions = {
        str: foo_str,
        int: foo_int,
        tuple: foo_tuple,
        list: foo_list
    }
    got_type = type(something)
    if got_type in functions:
        return functions[got_type](something)


print(func(123456789))
print(func('qwertyuio10433204'))
print(func(['a', 'as', 121, 32, 2, '2']))
print(func((1, '432', None, 'Word', 'werrwe')))

import random


# Задание 5


def is_prime(number: int) -> bool:
    n = abs(number)
    if n < 2:
        return False
    upper_bound = int(n ** 0.5)
    for i in range(2, upper_bound + 1):
        if n % i == 0:
            return False
    return True


while True:
    s = input("Введите число")
    if s.isdigit():
        num = int(s)
        if is_prime(num):
            print(f"{num} - простое число")
        else:
            print(f"{num} не простое")
        break
    print("Вы ввели не число, попробуйте еще раз")


# Задание 6


def calc_avg(items) -> float:
    items_count = len(items)
    total = 0.0
    if items_count == 0:
        return 0.0
    for item in items:
        total += item
    total = sum(items)
    return total / items_count


arr = []
for _ in range(10):
    arr.append(random.randint(0, 10000))
print(f"Числа:{arr}")
avg = calc_avg(arr)
print(f"Среднее:{avg}")


# Калькулятор


def input_float(msg: str) -> float:
    while True:
        input_str = input(msg)
        chunks = input_str.split('.')
        if len(chunks) == 1:
            if input_str.isdigit():
                return float(input_str)
        elif len(chunks) == 2:
            if chunks[0].isdigit() and chunks[1].isdigit():
                return float(input_str)
        print('Вы ввели неправильное число, попробуйте еще раз')


def add(first: float, second: float) -> float:
    return first + second


def sub(first: float, second: float) -> float:
    return first - second


def mul(first: float, second: float) -> float:
    return first * second


def div(first: float, second: float) -> float:
    return first / second


while True:
    first_number = input_float("Введите первое число")
    operator = input("Введите операцию")
    second_number = input_float("Введите второе число")
    operation = None
    if operator == '+':
        operation = add
    elif operator == '-':
        operation = sub
    elif operator == '*':
        operation = mul
    elif operator == '/':
        operation = div
        if second_number == 0:
            print("На ноль делить нельзя!!!")
            continue
    elif operator == '0':
        print("Выход из программы")
        break
    else:
        print(f"Неизвестная операция: {operator}")
    if operation is not None:
        result = operation(first_number, second_number)
        print(f"{first_number}{operator}{second_number}={result}")

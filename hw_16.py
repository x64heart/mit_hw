while True:
    try:
        a = float(input("Введите первое число"))
        b = float(input("Введите второе число"))
        res = a / b
        print(f"Результат :{res}")
        break
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except ValueError:
        break

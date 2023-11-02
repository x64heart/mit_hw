stored_items = {
    'apples': [
        2,
        15
    ],
    'milk': [
        3,
        10
    ],
    'pineapples': [
        7,
        5
    ],
    'bread': [
        2,
        8
    ],
}

balance = 100
cart = {

}


def input_items():
    while True:
        s = input("Введите название товара и количество через пробел").strip()
        if s == 'n':
            return
        chunks = s.split(' ')
        if len(chunks) != 2:
            continue
        item_name, quantity = chunks
        if not str(quantity).isdigit():
            print("Количество товара должно быть числом")
            continue
        return item_name, int(quantity)


def get_items():
    print("Товары в наличии")
    for k, v in stored_items.items():
        print("-".join([str(x) for x in [k, v[0], v[1]]]))


def get_info():
    global balance
    global cart
    print(f"Осталось на балансе :{balance}")
    print(f"Товары в корзине: {cart}")


def buy_item(item_name: str, item_count: int) -> bool:
    global balance
    global cart
    if not isinstance(item_name, str):
        return False
    if not isinstance(item_count, int):
        print("Количество товара должно быть числом")
        return False
    if item_count <= 0:
        print("Количество товара должно быть больше нуля")
        return False
    if item_name not in stored_items:
        print(f"Товара {item_name} нет в наличии")
        return False
    item = stored_items[item_name]
    item_price, item_remaining = item
    price_total = item_count * item_price
    if item_count > item_remaining:
        print("Выбранное количество товара превышает в наличии")
        return False
    if price_total > balance:
        print(f"У вас недостаточно средств на балансе ({balance}, необходимо {price_total})")
        return False
    item[1] -= item_count
    if item_name in cart:
        cart[item_name] += item_count
    else:
        cart[item_name] = item_count
    balance -= price_total
    return True


while True:
    get_items()
    user_input = input_items()
    if user_input is None:
        print("Выход из программы")
        break
    name, count = user_input
    if buy_item(name, count):
        get_info()

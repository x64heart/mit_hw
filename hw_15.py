import json

sep = ';'
cart = []
s = input(f"Введите название и стоимость через {sep}")
while s != 'стоп':
    s = input(f"Введите название и стоимость через {sep}")
    chunks = s.split(sep)
    if len(chunks) != 2:
        continue
    name, price = chunks
    if not str(price).isnumeric():
        continue
    cart.append({
        'name': name,
        'price': int(price)
    })
with open('cart.json', 'tw', encoding='utf-8') as f:
    json.dump(cart, f)

with open('cart.json', 'tr', encoding='utf-8') as f:
    items = json.load(f)
    total_price = sum([int(x['price']) for x in items if 'price' in x])
    print(f"Стоимость всех покупок за день: {total_price}")

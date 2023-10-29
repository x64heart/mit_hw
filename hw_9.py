# Задача №1
vowels = 'aeoiu'
arr = [15, 48, 'hello', 6, 19, 'world']
counter = 0
for item in arr:
    if type(item) == int:
        if item % 2:
            arr[counter] = 1
        else:
            digit_sum = sum([int(x) for x in str(item)])
            print(f"{item} - сумма цифр = {digit_sum}")
    elif type(item) == str:
        vowels_count = 0
        consonants_count = 0
        for c in item:
            if c in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
        print(f"{item} , {vowels_count} гласных, {consonants_count} согласных")
    counter += 1

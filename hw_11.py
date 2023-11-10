# Задание 1
s = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(sum(s))

# Задание 2
long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и',
             'и', 'и', 'т', 'т', 'а', 'и', 'и',
             'и', 'и', 'и', 'т', 'и')
letters = set(long_word)
for letter in letters:
    print(f"{letter} - {long_word.count(letter)}")

# Задание 3
week_temp = (26, 29, 34, 32, 28, 26, 23)
sum_temp = sum(week_temp)
days = len(week_temp)
mean_temp = sum_temp / days
print(int(mean_temp))

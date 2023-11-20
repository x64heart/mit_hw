data = [
    1, 4242, 'awaw', 35235, 'fdsfds', 532523, 'Words', 'qwertyuio', -624462462
]

with open("file.txt", 'tw', encoding='utf-8') as f:
    numbers = [x for x in data if type(x) == int]
    words = [x for x in data if type(x) == str]
    words.sort(key=lambda x: len(x))
    numbers.sort()
    arr = words + numbers
    result = '\n'.join([str(x) for x in arr])
    f.write(result)

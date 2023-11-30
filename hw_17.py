class Solution(object):
    vowels = 'eyuioa'
    consonants = 'qwrtpsdfghjklzxcvbnm'
    odd_digits = '13579'
    even_digits = '02468'

    def __init__(self, x):
        self.x = x

    def count_length(self, v):
        return len(v)

    def solve(self):
        if type(self.x) == str:
            consonants = ''
            vowels = ''
            for c in self.x:
                if c in Solution.vowels:
                    vowels += c
                elif c in Solution.consonants:
                    consonants += c
            mul = self.count_length(consonants) * self.count_length(vowels)
            if mul > self.count_length(self.x):
                print(consonants)
            else:
                print(vowels)

        elif type(self.x) == int:
            evens = 0
            odds = 0
            for c in str(self.x):
                if c in self.odd_digits:
                    odds += int(c)
                elif c in self.even_digits:
                    evens += int(c)
            print(evens * odds)


s1 = Solution('adsosoad')
s1.solve()
s2 = Solution(12345789)
s2.solve()

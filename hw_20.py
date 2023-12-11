import random


class CardDeck(object):
    SUITS = ['пик', 'треф', 'бубен', 'червей']
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
    CARDS = []
    for value in VALUES:
        for suit in SUITS:
            CARDS.append(f'{value} {suit}')

    def __init__(self):
        self.__cards_remaining = []
        self.shuffle()

    def shuffle(self):
        cards = CardDeck.CARDS.copy()
        self.__cards_remaining = []
        while len(cards) > 0:
            card = random.choice(cards)
            cards.remove(card)
            self.__cards_remaining.append(card)

    def __next__(self):
        if len(self.__cards_remaining) == 0:
            raise StopIteration()
        return self.__cards_remaining.pop()

    def __iter__(self):
        return self


deck = CardDeck()
for c in deck:
    print(c)

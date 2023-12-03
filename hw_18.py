class Tomato:
    states = ['seed', 'green', 'yellow', 'ripe']

    def __init__(self):
        self._index = 0
        self._state = self.states[self._index]

    def grow(self):
        if self._index == (len(self.states) - 1):
            return False
        self._index += 1
        self._state = self.states[self._index]
        return True

    def is_ripe(self):
        return self._index == len(self.states) - 1


class TomatoBush:
    def __init__(self, tomato_count: int):
        self.tomatoes = [Tomato() for _ in range(tomato_count)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def are_all_ripe(self):
        return all([x.is_ripe() for x in self.tomatoes])

    def give_all_away(self):
        self.tomatoes = list(filter(lambda x: not x.is_ripe(), self.tomatoes))
        if len(self.tomatoes) != 0:
            print('WARNING: not all tomatoes are ripe')


class Gardener:
    def __init__(self, name: str, plant: TomatoBush):
        self.name = name
        self._plant = plant

    def work(self):
        print('working on the plants')
        self._plant.grow_all()

    def harvest(self):
        self._plant.give_all_away()

    @staticmethod
    def knowledge_base():
        print()


Gardener.knowledge_base()
bush = TomatoBush(4)
gardener = Gardener('Alex', bush)
gardener.work()
gardener.harvest()
while not bush.are_all_ripe():
    gardener.work()
gardener.harvest()

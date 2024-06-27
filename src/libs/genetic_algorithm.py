from backpack import Item
import sys


class Alg:
    def __init__(self, items: list, limitWeight: int):
        self.items = items
        self.limitAmount = len(items)
        self.limitWeight = limitWeight

    def conductGeneticAlgorithm(self):
        pass


def getInput():
    print("Введите вместимость рюкзака")
    limitWeight = int(input())
    items = []
    print("Введите вес и стоимость каждой вещи с новой строки")
    for line in sys.stdin:
        weight, cost = line.split()
        items.append(Item(weight, cost))
    return items, limitWeight


if __name__ == '__main__':
    items, limitWeight = getInput()
    geneticAlgorithm = Alg(items, limitWeight)
    Alg.conductGeneticAlgorithm()

from objects import *
import sys
import random


class GeneticAlgorithm:
    def __init__(self, items: list[Item],
                 parameters: AlgorithmParameters):
        self.items = items
        self.parameters = parameters

    def generateRandomGeneration(self) -> Generation:
        pass
        # randomGeneration = Generation([])
        # for _ in range(self.parameters.amountOfIndividsPerGeneration):
        #     randomGeneration.append([item for item in self.items])
        # return randGeneration


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

from objects import *
import sys
import random


class GeneticAlgorithm:
    def __init__(self, items: list[Item], parameters: AlgorithmParameters):
        self.items = items
        self.parameters = parameters

    def generateRandomGeneration(self) -> Generation:
        randomGeneration = Generation([])
        for _ in range(self.parameters.amountOfIndividsPerGeneration):
            randomGeneration.append(Backpack([random.randint(0, self.parameters.maxBackpackWeight // item.weight)
                                              for item in self.items]))
            randomGeneration[-1].calculationWeight(self.items)
            randomGeneration[-1].calculationFitness(self.parameters.maxBackpackWeight, self.items)
        return randomGeneration

    def tournamentSelection(self, generation: Generation) -> Backpack:
        tournament = random.shuffle([i for i in range(0, len(generation))])[:4]
        return max([generation[i] for i in tournament])

    def uniformCrossing(self, parents: tuple[Backpack, Backpack]) -> list[Backpack]:
        pass

    # метод может ничего не возвращать, если будет менять передаваемый параметр (не помню, как это делается в питоне)
    def densityMutation(self, individ: Backpack) -> Backpack:
        # + описание мутации каждого гена в геноме
        pass

    def eliteChoice(self, generation: Generation) -> Generation:
        pass

    def dynamicProgrammingSolution(self) -> Backpack:
        pass

    def solution(self) -> list[list[Backpack]]:
        initGeneration = self.generateRandomGeneration()
        result = []


def getInput():
    print("Введите вместимость рюкзака")
    limitWeight = int(input())
    items = []
    print("Введите стоимость и вес каждой вещи с новой строки")
    for line in sys.stdin:
        weight, cost = line.split()
        items.append(Item(weight, cost))
    return items, limitWeight


if __name__ == '__main__':
    GA = GeneticAlgorithm([Item(3, 5), Item(4, 6)], AlgorithmParameters(20, 0.1, 0.1, 10, 10))
    print(GA.generateRandomGeneration())
    # items, limitWeight = getInput()
    # geneticAlgorithm = Alg(items, limitWeight)
    # Alg.conductGeneticAlgorithm()

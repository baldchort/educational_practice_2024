import matplotlib.pyplot as plt
import numpy as np

from src.libs.GA_methods.crossing import *
from src.libs.GA_methods.generation_selection import *
from src.libs.GA_methods.mutation import *
from src.libs.GA_methods.parent_selection import *


class GeneticAlgorithm:
    def __init__(self, items: list[Item], algorithmParameters: AlgorithmParameters):
        self.items = items
        self.algorithmParameters = algorithmParameters
        self.parentsSelectionStrategy = algorithmParameters.parentsSelectionStrategy
        self.crossingStrategy = algorithmParameters.crossingStrategy
        self.mutationStrategy = algorithmParameters.mutationStrategy
        self.generationSelectionStrategy = algorithmParameters.generationSelectionStrategy

    def generateRandomBackpack(self) -> Backpack:
        remainingWeight = self.algorithmParameters.maxBackpackWeight
        availableItems = [i for i in range(len(self.items)) if
                          self.items[i].weight <= remainingWeight]
        genome = [0] * len(self.items)
        while availableItems and remainingWeight:
            itemIndex = random.choice(availableItems)
            item = self.items[itemIndex]
            maxAmount = remainingWeight // item.weight
            amount = maxAmount if (len(availableItems) == 1 or maxAmount == 1) \
                else random.randint(1, maxAmount)

            genome[itemIndex] += amount
            remainingWeight -= amount * item.weight

            availableItems = [i for i in availableItems if self.items[i].weight <= remainingWeight]
        return Backpack(genome)

    def generateRandomGeneration(self) -> Generation:
        randomGeneration = Generation([])
        for _ in range(self.algorithmParameters.amountOfIndividsPerGeneration):
            backpack = self.generateRandomBackpack()
            backpack.calculateWeight(self.items)
            backpack.calculateFitness(self.algorithmParameters.maxBackpackWeight, self.items)
            randomGeneration.append(backpack)
        return randomGeneration

    def getSolution(self) -> list[IterationInfo]:
        generation = self.generateRandomGeneration()
        if log:
            print(f"Начальное случайно сгенерированное поколение:")
            self.outputBackpacks(generation.backpacks)
            print()

        maxFitness = []
        averageFitness = []
        allIterations = []
        global generationNum
        for generationNumber in range(1, self.algorithmParameters.maxAmountOfGenerations + 1):
            generationNum = generationNumber
            generation.calculateWeight(self.items)
            generation.calculateFitness(self.algorithmParameters.maxBackpackWeight, self.items)
            generation.sortBackpacksInDescendingOrder()
            maxFitness.append(generation.getMaxFitness())
            averageFitness.append(generation.getAverageFitness())
            allIterations.append(IterationInfo(generation.getBestBackpacks(), maxFitness[-1], averageFitness[-1]))

            if log:
                print(f"\n------------------")
                print(f"Лучшие решения поколения №{generationNumber}")
                self.outputBackpacks(generation.getBestBackpacks())
                print(f"Текущая максимальная приспособленность: {generation.getMaxFitness()}")
                print(f"Текущая средняя приспособленность: {generation.getAverageFitness()}")

            selectedParents = self.parentsSelectionStrategy.selectParent(generation, self.algorithmParameters)
            producedChildren = self.crossingStrategy.crossing(selectedParents, self.algorithmParameters)
            self.mutationStrategy.mutation(producedChildren, self.algorithmParameters, self.items)
            generation = self.generationSelectionStrategy.select(generation, producedChildren,
                                                                 self.algorithmParameters)
        if log:
            self.drawPlot(maxFitness, averageFitness)
        return allIterations

    def drawPlot(self, maxFitness: list[int], averageFitness: list[float]) -> None:
        x_len = self.algorithmParameters.maxAmountOfGenerations
        plt.plot(list(range(x_len)), averageFitness, 'r-')
        plt.plot(list(range(x_len)), maxFitness, 'b-')
        plt.grid()
        plt.xticks(np.arange(0, x_len + 1, 2))
        plt.xlabel('Поколение')
        plt.ylabel('Приспособленность')
        plt.show()

    def outputGenerationInfo(self, generation: Generation, generationNumber: int) -> None:
        print(f"\nПоколение №{generationNumber}:")
        for i, solution in enumerate(generation.descendingSortedBackpacks):
            print(f"{i + 1}) {solution.genome}")
            print(f"\tСуммарная стоимость вещей: {solution.cost}")
            print(
                f"\tСуммарный вес вещей: {solution.weight}, дельта = {self.algorithmParameters.maxBackpackWeight - solution.weight}")
        print(f"Текущая максимальная приспособленность: {generation.getMaxFitness()}")
        print(f"Текущая средняя приспособленность: {generation.getAverageFitness()}")

    def outputBackpacks(self, backpacks: list[Backpack]) -> None:
        for i, backpack in enumerate(backpacks):
            print(f"{i + 1}) {backpack.genome}")
            print(f"\tСуммарная стоимость вещей: {backpack.cost}")
            print(
                f"\tСуммарный вес вещей: {backpack.weight}, дельта = {self.algorithmParameters.maxBackpackWeight - backpack.weight}")


if __name__ == '__main__':
    items = [Item(5, 2), Item(7, 3), Item(4, 6), Item(3, 2)]
    maxBackpackWeight = 22
    crossingProbability = 0.9
    mutationProbability = 0.2
    amountOfIndividsPerGeneration = 20
    maxAmountOfGenerations = 20

    parentsSelectionStrategy = TournamentSelection()
    crossingStrategy = UniformCrossing()
    mutationStrategy = DensityMutation()
    generationSelectionStrategy = EliteSelection()

    algorithmParameters = AlgorithmParameters(
        maxBackpackWeight,
        crossingProbability,
        mutationProbability,
        amountOfIndividsPerGeneration,
        maxAmountOfGenerations,
        parentsSelectionStrategy,
        crossingStrategy,
        mutationStrategy,
        generationSelectionStrategy
    )

    GA = GeneticAlgorithm(items, algorithmParameters)
    GA.getSolution()

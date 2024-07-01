from objects import *
import matplotlib.pyplot as plt
import random


class GeneticAlgorithm:
    def __init__(self, items: list[Item], parameters: AlgorithmParameters):
        self.items = items
        self.parameters = parameters

    def generateRandomGeneration(self) -> Generation:
        randomGeneration = Generation([])
        for _ in range(self.parameters.amountOfIndividsPerGeneration):
            randomGeneration.append(Backpack([random.randint(0, self.parameters.maxBackpackWeight // item.weight // 2)
                                              for item in self.items]))
            randomGeneration.calculateWeight(self.items)
            randomGeneration.calculateFitness(self.parameters.maxBackpackWeight, self.items)
        return randomGeneration

    def tournamentParentsSelection(self, generation: Generation) -> list[Backpack]:
        selectedParents = []
        while len(selectedParents) != self.parameters.amountOfIndividsPerGeneration:
            indexes = [i for i in range(len(generation))]
            tournamentIndexes = random.sample(indexes, 2)
            selectedParents.append(max([generation[i] for i in tournamentIndexes]))
        return selectedParents

    def uniformCrossingForTwoParents(self, parents: tuple[Backpack, Backpack]) -> list[Backpack]:
        children = [[], []]
        for j in range(len(parents[0].genome)):
            i = random.choice([0, 1])
            children[0].append(parents[i].genome[j])
            children[1].append(parents[1 - i].genome[j])

        for i in range(len(children)):
            children[i] = Backpack(children[i])
            children[i].calculateWeight(self.items)
            children[i].calculateFitness(self.parameters.maxBackpackWeight, self.items)
        return children

    def uniformParentsCrossing(self, selectedParents: list[Backpack]) -> list[Backpack]:
        producedChildren = []
        while len(producedChildren) <= self.parameters.amountOfIndividsPerGeneration:
            parents = random.sample(selectedParents, 2)
            if random.random() < self.parameters.crossingProbability:
                producedChildren += self.uniformCrossingForTwoParents(parents)
        return producedChildren

    def densityMutationOneChild(self, child: Backpack) -> None:
        parameter = 10
        for i in range(len(child.genome)):
            if random.random() < self.parameters.mutationProbability:
                delta = 0
                for j in range(parameter):
                    randVal = random.choices([1, 0], weights=[1 / parameter, 1 - 1 / parameter])[0]
                    delta += randVal * 2 ** (-i)
                child.genome[i] = int(child.genome[i] + random.choice([-1, 1]) * delta * 2)
        child.calculateWeight(self.items)
        child.calculateFitness(self.parameters.maxBackpackWeight, self.items)

    def densityChildrenMutation(self, children: list[Backpack]) -> None:
        for i in range(len(children)):
            if random.random() < self.parameters.mutationProbability:
                self.densityMutationOneChild(children[i])

    def eliteChoice(self, selectedParents: list[Backpack], producedChildren: list[Backpack]) -> Generation:
        allCandidates = selectedParents + producedChildren
        generation = sorted(allCandidates, key=lambda x: x.cost, reverse=True)[
                     :int(0.2 * self.parameters.amountOfIndividsPerGeneration)]
        while len(generation) != self.parameters.amountOfIndividsPerGeneration:
            generation.append(random.choice(allCandidates))
        return Generation(generation)

    def dynamicProgrammingSolution(self) -> Backpack:
        pass

    def drawPlot(self, maxFitness: list[float], averageFitness: list[float]) -> None:
        x_len = self.parameters.maxAmountOfGenerations
        plt.plot(list(range(x_len)), averageFitness, 'r-')
        plt.plot(list(range(x_len)), maxFitness, 'b-')
        plt.grid()
        plt.xlabel('Поколение')
        plt.ylabel('Приспособленность')
        plt.show()

    def outputGenerationInfo(self, generation: Generation, generationNum: int):
        print(f"\nПоколение №{generationNum}:")
        sortedGeneration = sorted(generation, key=lambda x: x.cost, reverse=True)
        for i, solution in enumerate(sortedGeneration):
            print(f"{i + 1}) {solution.genome}")
            print(f"\tСуммарная стоимость вещей: {solution.cost}")
            print(
                f"\tСуммарный вес вещей: {solution.weight}, дельта = {self.parameters.maxBackpackWeight - solution.weight}")
        print(f"Текущая максимальная приспособленность: {generation.getMaxFitness()}")
        print(f"Текущая средняя приспособленность: {generation.getAverageFitness()}")

    def outputBackpacks(self, backpacks: list[Backpack]):
        for i, backpack in enumerate(backpacks):
            print(f"{i + 1}) {backpack.genome}")
            print(f"\tСуммарная стоимость вещей: {backpack.cost}")
            print(
                f"\tСуммарный вес вещей: {backpack.weight}, дельта = {self.parameters.maxBackpackWeight - backpack.weight}")

    def getSolution(self) -> list[IterationInfo]:
        generation = self.generateRandomGeneration()
        self.outputGenerationInfo(generation, 1)
        maxFitness = [generation.getMaxFitness()]
        averageFitness = [generation.getAverageFitness()]
        allIterations = []

        for generationNumber in range(1, self.parameters.maxAmountOfGenerations):
            print(f"------------------")
            print(f"Поколение №{generationNumber}")
            selectedParents = self.tournamentParentsSelection(generation)
            print(f"\nОтобранные родители:")
            self.outputBackpacks(selectedParents)
            producedChildren = self.uniformParentsCrossing(selectedParents)
            print(f"\nПолученные дети:")
            self.outputBackpacks(producedChildren)
            self.densityChildrenMutation(producedChildren)
            generation = self.eliteChoice(selectedParents, producedChildren)

            generation.calculateWeight(self.items)
            generation.calculateFitness(self.parameters.maxBackpackWeight, self.items)
            maxFitness.append(generation.getMaxFitness())
            averageFitness.append(generation.getAverageFitness())

            self.outputGenerationInfo(generation, generationNumber)
            allIterations.append(IterationInfo(generation.getBestBackpacks(), maxFitness[-1], averageFitness[-1]))

        self.drawPlot(maxFitness, averageFitness)
        return allIterations


#
# def getInput():
#     print("Введите вместимость рюкзака")
#     limitWeight = int(input())
#     items = []
#     print("Введите стоимость и вес каждой вещи с новой строки")
#     for line in sys.stdin:
#         weight, cost = line.split()
#         items.append(Item(weight, cost))
#     return items, limitWeight


if __name__ == '__main__':
    items = [Item(5, 2), Item(7, 3), Item(6, 4), Item(3, 2)]
    maxBackpackWeight = 9
    crossingProbability = 0.9
    mutationProbability = 0.1
    amountOfIndividsPerGeneration = 20
    maxAmountOfGenerations = 20

    GA = GeneticAlgorithm(items, AlgorithmParameters(maxBackpackWeight, crossingProbability, mutationProbability,
                                                     amountOfIndividsPerGeneration, maxAmountOfGenerations))
    GA.getSolution()

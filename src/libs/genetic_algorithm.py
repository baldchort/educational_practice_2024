import numpy as np

from objects import *
import matplotlib.pyplot as plt
import random

generationNum = mutationNum = 1


class GeneticAlgorithm:
    def __init__(self, items: list[Item], parameters: AlgorithmParameters):
        self.items = items
        self.parameters = parameters

    def generateRandomBackpack(self) -> Backpack:
        currentBackpackWeight = 0
        availableItems = self.items
        genome = [0] * len(self.items)
        while len(availableItems) != 0:
            item = random.choice(availableItems)

            if len(availableItems) == 1:
                amount = int((self.parameters.maxBackpackWeight - currentBackpackWeight) / item.weight)
            else:
                amount = random.randint(1, (self.parameters.maxBackpackWeight - currentBackpackWeight) // item.weight)

            ind = self.items.index(item)
            genome[ind] += amount
            currentBackpackWeight += amount * item.weight

            availableItems = list(
                filter(lambda x: x.weight <= self.parameters.maxBackpackWeight - currentBackpackWeight, availableItems))
        return Backpack(genome)

    def generateRandomGeneration(self) -> Generation:
        randomGeneration = Generation([])
        for _ in range(self.parameters.amountOfIndividsPerGeneration):
            randomGeneration.append(self.generateRandomBackpack())
            randomGeneration.calculateWeight(self.items)
            randomGeneration.calculateFitness(self.parameters.maxBackpackWeight, self.items)
        return randomGeneration

    def tournamentParentsSelection(self, generation: Generation) -> list[Backpack]:
        selectedParents = []
        while len(selectedParents) != self.parameters.amountOfIndividsPerGeneration:
            indexes = [i for i in range(len(generation))]
            tournamentIndexes = random.sample(indexes, 2)
            selectedParents.append(max([generation[i] for i in tournamentIndexes]))

            global generationNum
            if len(selectedParents) < 2 and generationNum == 1:
                print("\nОтбор родителей турниром")
                individ1 = generation[tournamentIndexes[0]]
                individ2 = generation[tournamentIndexes[1]]
                print(f"Две случайно выбранные особи:")
                print(f"\t1) {individ1}")
                print(f"\t2) {individ2}")
                print(f"\tВыбираем лучшую из них: {selectedParents[-1].genome}")

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
            global generationNum
            if len(producedChildren) < 2 and generationNum == 1:
                print("\nРавномерное скрещивание особей")
                print(f"Два случайно выбранных родителя:")
                print(f"\t1) {parents[0]}")
                print(f"\t2) {parents[1]}")
            if random.random() < self.parameters.crossingProbability:
                producedChildren += self.uniformCrossingForTwoParents(parents)
                if len(producedChildren) == 2 and generationNum == 1:
                    print(f"Полученные дети:")
                    print(f"\t1) {producedChildren[-1]}")
                    print(f"\t1) {producedChildren[-2]}")
            elif len(producedChildren) < 2 and generationNum == 1:
                if len(producedChildren) == 2 and generationNum == 1:
                    print("Скрещивание не проводится")
        return producedChildren

    def densityMutationOneChild(self, child: Backpack) -> None:
        global mutationNum
        if mutationNum == 1:
            print("\nПлотность мутации")
            print(f"Геном до мутации:")
            print(f"{child}")

        parameter = 20
        for i in range(len(child.genome)):
            if i == mutationNum == 1:
                print(f"\tПервый ген до мутации: {child.genome[i]}")
            if random.random() < self.parameters.mutationProbability:
                delta = 0
                for j in range(parameter):
                    randVal = random.choices([1, 0], weights=[1 / parameter, 1 - 1 / parameter])[0]
                    delta += randVal * 2 ** (-i)
                sign = random.choice([-1, 1])
                child.genome[i] = int(child.genome[i] + sign * delta * 2)
                if child.genome[i] < 0:
                    child.genome[i] = 0
                if i == mutationNum == 1:
                    print(f"\tСлучайно полученное значение, на которое мутирует ген: {int(2 * delta)}")
                    print(f"\tЗнак мутации: {sign}")
                    print(f"\tПервый ген после мутации: {child.genome[i]}")
            else:
                if i == mutationNum == 1:
                    print(f"\tПервый ген не мутирует")
        child.calculateWeight(self.items)
        child.calculateFitness(self.parameters.maxBackpackWeight, self.items)
        if mutationNum == 1:
            print(f"Геном после мутации:")
            print(f"{child}")
        mutationNum = 2

    def densityChildrenMutation(self, children: list[Backpack]) -> None:
        for i in range(len(children)):
            if random.random() < self.parameters.mutationProbability:
                self.densityMutationOneChild(children[i])

    def eliteChoice(self, selectedParents: list[Backpack], producedChildren: list[Backpack]) -> Generation:
        allCandidates = selectedParents + producedChildren
        generation = sorted(allCandidates, key=lambda x: x.cost, reverse=True)[
                     :int(0.1 * self.parameters.amountOfIndividsPerGeneration)]
        global generationNum
        if generationNum == 1:
            print(f"\nЭлитарный отбор")
            print(f"Лучшие 10% родительских и детских особей:")
            self.outputBackpacks(generation)
        while len(generation) != self.parameters.amountOfIndividsPerGeneration:
            generation.append(random.choice(allCandidates))
        if generationNum == 1:
            print(f"Остальные 90% выбираются случайно")
            print(f"\nИтоговое новое поколение:")
            self.outputBackpacks(generation)
            print()
        return Generation(generation)

    def dynamicProgrammingSolution(self) -> Backpack:
        pass

    def drawPlot(self, maxFitness: list[int], averageFitness: list[float]) -> None:
        x_len = self.parameters.maxAmountOfGenerations
        plt.plot(list(range(x_len)), averageFitness, 'r-')
        plt.plot(list(range(x_len)), maxFitness, 'b-')
        plt.grid()
        plt.xticks(np.arange(0, x_len + 1, 2))
        # строчка ниже все ломает, хотя она должна задавать шаг рисок по оси oy
        # plt.yticks(np.arange(min(maxFitness), max(maxFitness)+1, 5))
        plt.xlabel('Поколение')
        plt.ylabel('Приспособленность')
        plt.show()

    def outputGenerationInfo(self, generation: Generation, generationNumber: int) -> None:
        print(f"\nПоколение №{generationNumber}:")
        sortedGeneration = sorted(generation, key=lambda x: x.cost, reverse=True)
        for i, solution in enumerate(sortedGeneration):
            print(f"{i + 1}) {solution.genome}")
            print(f"\tСуммарная стоимость вещей: {solution.cost}")
            print(
                f"\tСуммарный вес вещей: {solution.weight}, дельта = {self.parameters.maxBackpackWeight - solution.weight}")
        print(f"Текущая максимальная приспособленность: {generation.getMaxFitness()}")
        print(f"Текущая средняя приспособленность: {generation.getAverageFitness()}")

    def outputBackpacks(self, backpacks: list[Backpack]) -> None:
        for i, backpack in enumerate(backpacks):
            print(f"{i + 1}) {backpack.genome}")
            print(f"\tСуммарная стоимость вещей: {backpack.cost}")
            print(
                f"\tСуммарный вес вещей: {backpack.weight}, дельта = {self.parameters.maxBackpackWeight - backpack.weight}")

    def getSolution(self) -> list[IterationInfo]:
        generation = self.generateRandomGeneration()
        print(f"Начальное случайно сгенерированное поколение:")
        self.outputBackpacks(generation.backpacks)
        print()

        maxFitness = []
        averageFitness = []
        allIterations = []
        global generationNum
        for generationNumber in range(1, self.parameters.maxAmountOfGenerations + 1):
            generationNum = generationNumber
            generation.calculateWeight(self.items)
            generation.calculateFitness(self.parameters.maxBackpackWeight, self.items)
            maxFitness.append(generation.getMaxFitness())
            averageFitness.append(generation.getAverageFitness())
            allIterations.append(IterationInfo(generation.getBestBackpacks(), maxFitness[-1], averageFitness[-1]))

            print(f"\n------------------")
            print(f"Лучшие решения поколения №{generationNumber}")
            self.outputBackpacks(generation.getBestBackpacks())

            selectedParents = self.tournamentParentsSelection(generation)
            # if generationNumber == 1:
            #     print(f"\nОтобранные для скрещивания родители:")
            #     self.outputBackpacks(selectedParents)

            producedChildren = self.uniformParentsCrossing(selectedParents)
            # if generationNumber == 1:
            #     print(f"\nПолученные дети:")
            #     self.outputBackpacks(producedChildren)

            self.densityChildrenMutation(producedChildren)
            # if generationNumber == 1:
            #     print(f"\nДети после мутации:")
            #     self.outputBackpacks(producedChildren)

            generation = self.eliteChoice(generation.backpacks, producedChildren)

        self.drawPlot(maxFitness, averageFitness)
        return allIterations


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
    mutationProbability = 0.2
    amountOfIndividsPerGeneration = 20
    maxAmountOfGenerations = 20

    GA = GeneticAlgorithm(items, AlgorithmParameters(maxBackpackWeight, crossingProbability, mutationProbability,
                                                     amountOfIndividsPerGeneration, maxAmountOfGenerations))
    GA.getSolution()

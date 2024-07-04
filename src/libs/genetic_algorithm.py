from src.libs.objects import *
import matplotlib.pyplot as plt
import numpy as np
import random

generationNum = mutationNum = 1


class AlgorithmParameters:
    def __init__(self,
                 maxBackpackWeight: int,
                 crossingProbability: float,
                 mutationProbability: float,
                 amountOfIndividsPerGeneration: int,
                 maxAmountOfGenerations: int,
                 wayOfParentsSelection: str,
                 wayOfCrossing: str,
                 wayOfMutation: str,
                 wayOfNewGenerationSelection: str):
        self.maxBackpackWeight = maxBackpackWeight
        self.crossingProbability = crossingProbability
        self.mutationProbability = mutationProbability
        self.amountOfIndividsPerGeneration = amountOfIndividsPerGeneration
        self.maxAmountOfGenerations = maxAmountOfGenerations
        self.wayOfParentsSelection = wayOfParentsSelection
        self.wayOfCrossing = wayOfCrossing
        self.wayOfMutation = wayOfMutation
        self.wayOfNewGenerationSelection = wayOfNewGenerationSelection


class AlgorithmDataAndCommonMethods:
    def __init__(self, items: list[Item], algorithmParameters: AlgorithmParameters):
        self.items = items
        self.algorithmParameters = algorithmParameters

    def drawPlot(self, maxFitness: list[int], averageFitness: list[float]) -> None:
        x_len = self.algorithmParameters.maxAmountOfGenerations
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
                f"\tСуммарный вес вещей: {solution.weight}, дельта = {self.algorithmParameters.maxBackpackWeight - solution.weight}")
        print(f"Текущая максимальная приспособленность: {generation.getMaxFitness()}")
        print(f"Текущая средняя приспособленность: {generation.getAverageFitness()}")

    def outputBackpacks(self, backpacks: list[Backpack]) -> None:
        for i, backpack in enumerate(backpacks):
            print(f"{i + 1}) {backpack.genome}")
            print(f"\tСуммарная стоимость вещей: {backpack.cost}")
            print(
                f"\tСуммарный вес вещей: {backpack.weight}, дельта = {self.algorithmParameters.maxBackpackWeight - backpack.weight}")


class Selection(AlgorithmDataAndCommonMethods):
    def __init__(self, items: list[Item], algorithmParameters: AlgorithmParameters):
        super().__init__(items, algorithmParameters)
        self.selectionWays = {"Турнир": self.tournamentSelection, "Элитарный отбор": self.eliteSelection}

    def tournamentSelection(self, generation: Generation) -> list[Backpack]:
        selectedParents = []
        while len(selectedParents) != self.algorithmParameters.amountOfIndividsPerGeneration:
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

    def eliteSelection(self, selectedParents: list[Backpack], producedChildren: list[Backpack]) -> Generation:
        allCandidates = selectedParents + producedChildren
        generation = sorted(allCandidates, key=lambda x: x.cost, reverse=True)[
                     :int(0.1 * self.algorithmParameters.amountOfIndividsPerGeneration)]
        global generationNum
        if generationNum == 1:
            print(f"\nЭлитарный отбор")
            print(f"Лучшие 10% родительских и детских особей:")
            self.outputBackpacks(generation)
        while len(generation) != self.algorithmParameters.amountOfIndividsPerGeneration:
            generation.append(random.choice(allCandidates))
        if generationNum == 1:
            print(f"Остальные 90% выбираются случайно")
            print(f"\nИтоговое новое поколение:")
            self.outputBackpacks(generation)
            print()
        return Generation(generation)

    pass


class Crossing(AlgorithmDataAndCommonMethods):
    def __init__(self, items: list[Item], algorithmParameters: AlgorithmParameters):
        super().__init__(items, algorithmParameters)
        self.crossingWays = {"Равномерное скрещивание": self.uniformCrossing}

    def uniformCrossingForTwoParents(self, parents: tuple[Backpack, Backpack]) -> list[Backpack]:
        children = [[], []]
        for j in range(len(parents[0].genome)):
            i = random.choice([0, 1])
            children[0].append(parents[i].genome[j])
            children[1].append(parents[1 - i].genome[j])

        for i in range(len(children)):
            children[i] = Backpack(children[i])
            children[i].calculateWeight(self.items)
            children[i].calculateFitness(self.algorithmParameters.maxBackpackWeight, self.items)
        return children

    def uniformCrossing(self, selectedParents: list[Backpack]) -> list[Backpack]:
        producedChildren = []
        while len(producedChildren) <= self.algorithmParameters.amountOfIndividsPerGeneration:
            parents = random.sample(selectedParents, 2)
            global generationNum
            if len(producedChildren) < 2 and generationNum == 1:
                print("\nРавномерное скрещивание особей")
                print(f"Два случайно выбранных родителя:")
                print(f"\t1) {parents[0]}")
                print(f"\t2) {parents[1]}")
            if random.random() < self.algorithmParameters.crossingProbability:
                producedChildren += self.uniformCrossingForTwoParents(parents)
                if len(producedChildren) == 2 and generationNum == 1:
                    print(f"Полученные дети:")
                    print(f"\t1) {producedChildren[-1]}")
                    print(f"\t1) {producedChildren[-2]}")
            elif len(producedChildren) < 2 and generationNum == 1:
                if len(producedChildren) == 2 and generationNum == 1:
                    print("Скрещивание не проводится")
        return producedChildren


class Mutation(AlgorithmDataAndCommonMethods):
    def __init__(self, items: list[Item], algorithmParameters: AlgorithmParameters):
        super().__init__(items, algorithmParameters)
        self.mutationWays = {"Плотность мутации": self.densityMutation}

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
            if random.random() < self.algorithmParameters.mutationProbability:
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
        child.calculateFitness(self.algorithmParameters.maxBackpackWeight, self.items)
        if mutationNum == 1:
            print(f"Геном после мутации:")
            print(f"{child}")
        mutationNum = 2

    def densityMutation(self, children: list[Backpack]) -> None:
        for i in range(len(children)):
            if random.random() < self.algorithmParameters.mutationProbability:
                self.densityMutationOneChild(children[i])


class GeneticAlgorithm(Selection, Mutation, Crossing):
    def __init__(self, items: list[Item], algorithmParameters: AlgorithmParameters):
        super().__init__(items, algorithmParameters)
        self.parentsSelection = self.selectionWays[self.algorithmParameters.wayOfParentsSelection]
        self.crossing = self.crossingWays[self.algorithmParameters.wayOfCrossing]
        self.mutation = self.mutationWays[self.algorithmParameters.wayOfMutation]
        self.generationSelection = self.selectionWays[self.algorithmParameters.wayOfNewGenerationSelection]

    def generateRandomBackpack(self) -> Backpack:
        currentBackpackWeight = 0
        availableItems = self.items
        genome = [0] * len(self.items)
        while len(availableItems) != 0:
            item = random.choice(availableItems)

            if len(availableItems) == 1:
                amount = int((self.algorithmParameters.maxBackpackWeight - currentBackpackWeight) / item.weight)
            else:
                amount = random.randint(1, (
                        self.algorithmParameters.maxBackpackWeight - currentBackpackWeight) // item.weight)

            ind = self.items.index(item)
            genome[ind] += amount
            currentBackpackWeight += amount * item.weight

            availableItems = list(
                filter(lambda x: x.weight <= self.algorithmParameters.maxBackpackWeight - currentBackpackWeight,
                       availableItems))
        return Backpack(genome)

    def generateRandomGeneration(self) -> Generation:
        randomGeneration = Generation([])
        for _ in range(self.algorithmParameters.amountOfIndividsPerGeneration):
            randomGeneration.append(self.generateRandomBackpack())
            randomGeneration.calculateWeight(self.items)
            randomGeneration.calculateFitness(self.algorithmParameters.maxBackpackWeight, self.items)
        return randomGeneration

    def dynamicProgrammingSolution(self) -> Backpack:
        pass

    def getSolution(self) -> list[IterationInfo]:
        generation = self.generateRandomGeneration()
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
            maxFitness.append(generation.getMaxFitness())
            averageFitness.append(generation.getAverageFitness())
            allIterations.append(IterationInfo(generation.getBestBackpacks(), maxFitness[-1], averageFitness[-1]))

            print(f"\n------------------")
            print(f"Лучшие решения поколения №{generationNumber}")
            self.outputBackpacks(generation.getBestBackpacks())

            selectedParents = self.parentsSelection(generation)
            producedChildren = self.crossing(selectedParents)
            self.mutation(producedChildren)
            generation = self.generationSelection(generation.backpacks, producedChildren)

        self.drawPlot(maxFitness, averageFitness)
        return allIterations


if __name__ == '__main__':
    items = [Item(5, 2), Item(7, 3), Item(6, 4), Item(3, 2)]
    maxBackpackWeight = 22
    crossingProbability = 0.9
    mutationProbability = 0.2
    amountOfIndividsPerGeneration = 20
    maxAmountOfGenerations = 20
    wayOfParentsSelection = "Турнир"
    wayOfCrossing = "Равномерное скрещивание"
    wayOfMutation = "Плотность мутации"
    wayOfNewGenerationSelection = "Элитарный отбор"
    GA = GeneticAlgorithm(items, AlgorithmParameters(maxBackpackWeight, crossingProbability, mutationProbability,
                                                     amountOfIndividsPerGeneration, maxAmountOfGenerations,
                                                     wayOfParentsSelection, wayOfCrossing, wayOfMutation,
                                                     wayOfNewGenerationSelection))
    GA.getSolution()
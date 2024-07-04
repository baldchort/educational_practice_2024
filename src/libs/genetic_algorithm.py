import random

import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable

from src.libs.objects import *

generationNum = 1
mutationNum = 1
discreteRecomb = 1
log = 0


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


class Selection(AlgorithmDataAndCommonMethods):
    def __init__(self, items: list[Item], algorithmParameters: AlgorithmParameters):
        super().__init__(items, algorithmParameters)
        self.selectionWays = {"Турнир": self.tournamentSelection,
                              "Рулетка": self.rouletteSelection,
                              "Инбридинг": self.inbreedingSelection,
                              "Элитарный отбор": self.eliteSelection,
                              "Отбор вытеснением": self.displacementSelection,
                              "Отбор усечением": self.truncationSelection}

    def tournamentSelection(self, generation: Generation) -> list[Backpack]:
        selectedParents = []
        while len(selectedParents) != self.algorithmParameters.amountOfIndividsPerGeneration:
            indexes = [i for i in range(len(generation))]
            tournamentIndexes = random.sample(indexes, 2)
            selectedParents.append(max([generation[i] for i in tournamentIndexes]))

            global generationNum
            if log and len(selectedParents) < 2 and generationNum == 1:
                print("\nОТБОР ТУРНИРОМ")
                individ1 = generation[tournamentIndexes[0]]
                individ2 = generation[tournamentIndexes[1]]
                print(f"Две случайно выбранные особи:")
                print(f"\t1) {individ1}")
                print(f"\t2) {individ2}")
                print(f"\tВыбираем лучшую из них: {selectedParents[-1].genome}")

        return selectedParents

    def rouletteSelection(self, generation: Generation) -> list[Backpack]:
        selectedParents = []
        sumFitness = sum([individ.cost for individ in generation])
        probabilities = [individ.cost / sumFitness for individ in generation]

        table = PrettyTable(['№', 'Особь', 'Приспособленность', 'Вероятность выбора'])
        for i in range(len(generation)):
            table.add_row([i, generation[i].genome, generation[i].cost, round(probabilities[i], 4)])

        while len(selectedParents) != self.algorithmParameters.amountOfIndividsPerGeneration:
            selectedParents.append(random.choices(generation, weights=probabilities, k=1)[0])

            global generationNum
            if log and len(selectedParents) < 2 and generationNum == 1:
                print("\nОТБОР РУЛЕТКОЙ")
                print(table)
                print(f"Случайно выбранная особь:")
                print(f"\t{selectedParents[0]}")

        return selectedParents

    def inbreedingSelection(self, generation: Generation) -> list[Backpack]:
        selectedParents = []
        firstParentInd = random.choice([ind for ind in range(len(generation))])
        if firstParentInd == 0:
            secondParentInd = firstParentInd + 1
        elif (firstParentInd == len(generation) - 1 or
              (abs(generation.descendingSortedBackpacks[firstParentInd - 1].cost -
                   generation.descendingSortedBackpacks[firstParentInd].cost) <
               abs(generation.descendingSortedBackpacks[firstParentInd + 1].cost -
                   generation.descendingSortedBackpacks[firstParentInd].cost))):
            secondParentInd = firstParentInd - 1
        else:
            secondParentInd = firstParentInd + 1
        selectedParents.append(generation.descendingSortedBackpacks[firstParentInd])
        selectedParents.append(generation.descendingSortedBackpacks[secondParentInd])

        global generationNum
        if log and len(selectedParents) < 3 and generationNum == 1:
            print("\nИНБРИДИНГ")
            print(f"Случайно выбранная особь:")
            print(f"\t{generation.descendingSortedBackpacks[firstParentInd]}")
            print(f"\tЕе порядковый номер в популяции по убыванию ф-ии приспособленности: {firstParentInd}")
            print(f"Ближайшая особь:")
            print(f"\t{generation.descendingSortedBackpacks[secondParentInd]}")
            print(
                f"\tЕе порядковый номер в популяции по убыванию ф-ии приспособленности: {secondParentInd if secondParentInd >= 0 else len(generation) - secondParentInd}")
        return selectedParents

    def eliteSelection(self, oldGeneration: Generation, producedChildren: list[Backpack]) -> Generation:
        allCandidates = oldGeneration.backpacks + producedChildren
        generation = sorted(allCandidates, key=lambda x: x.cost, reverse=True)[
                     :int(0.1 * self.algorithmParameters.amountOfIndividsPerGeneration)]
        global generationNum
        if log and generationNum == 1:
            print(f"\nЭЛИТАРНЫЙ ОТБОР")
            print(f"Лучшие 10% родительских и детских особей:")
            self.outputBackpacks(generation)
        while len(generation) != self.algorithmParameters.amountOfIndividsPerGeneration:
            generation.append(random.choice(allCandidates))
        if log and generationNum == 1:
            print(f"Остальные 90% выбираются случайно")
            print(f"\nИтоговое новое поколение:")
            self.outputBackpacks(generation)
            print()
        return Generation(generation)

    def displacementSelection(self, oldGeneration: Generation, producedChildren: list[Backpack]) -> Generation:
        sortedOldGeneration = sorted(oldGeneration.backpacks + producedChildren, key=lambda x: x.cost, reverse=True)
        newGeneration = []
        addedToNewGenerationGenomes = []

        for individ in sortedOldGeneration:
            if len(newGeneration) == self.algorithmParameters.amountOfIndividsPerGeneration:
                break
            if individ.genome not in addedToNewGenerationGenomes:
                newGeneration.append(individ)
                addedToNewGenerationGenomes.append(individ.genome)

        if len(newGeneration) != self.algorithmParameters.amountOfIndividsPerGeneration:
            print("ПУПУПУ")
            exit(0)

        global generationNum
        if log and generationNum == 1:
            print(f"\nОТБОР ВЫТЕСНЕНИЕМ")
            print(f"Выбираем в новое поколение лучшие уникальные родительские и детские особи")
            print(f"\nИтоговое новое поколение:")
            self.outputBackpacks(newGeneration)
            print()

        return Generation(newGeneration)

    def truncationSelection(self, oldGeneration: Generation, producedChildren: list[Backpack]) -> Generation:
        sortedOldGeneration = sorted(oldGeneration.backpacks + producedChildren, key=lambda x: x.cost, reverse=True)[
                              :int(0.5 * self.algorithmParameters.amountOfIndividsPerGeneration)]
        newGeneration = []
        while len(newGeneration) != self.algorithmParameters.amountOfIndividsPerGeneration:
            newGeneration.append(random.choice(sortedOldGeneration))

        global generationNum
        if log and generationNum == 1:
            print(f"\nОТБОР УСЕЧЕНИЕМ")
            print(f"Выбираем среди 50% лучших родительских и детских особей:")
            self.outputBackpacks(sortedOldGeneration)
            print(f"\nИтоговое новое поколение:")
            self.outputBackpacks(newGeneration)
            print()

        return Generation(newGeneration)


class Crossing(AlgorithmDataAndCommonMethods):
    def __init__(self, items: list[Item], algorithmParameters: AlgorithmParameters):
        super().__init__(items, algorithmParameters)
        self.crossingWays = {"Равномерное скрещивание": self.uniformCrossing,
                             "Дискретная рекомбинация": self.discreteRecombination,
                             "Промежуточная рекомбинация": self.IntermediateRecombination}

    def uniformCrossingForTwoParents(self, parents: list[Backpack, Backpack]) -> list[Backpack]:
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
        while len(producedChildren) < self.algorithmParameters.amountOfIndividsPerGeneration:
            parents = random.sample(selectedParents, 2)
            global generationNum
            global discreteRecomb
            if log and len(producedChildren) < 2 and generationNum == 1 and discreteRecomb:
                if discreteRecomb:
                    print("\nДИСКРЕТНАЯ РЕКОМБИНАЦИЯ")
                else:
                    print("\nРАВНОМЕРНОЕ СКРЕЩИВАНИЕ")
                print(f"Два выбранных родителя:")
                print(f"\t1) {parents[0]}")
                print(f"\t2) {parents[1]}")
            if random.random() < self.algorithmParameters.crossingProbability:
                producedChildren += self.uniformCrossingForTwoParents(parents)
                if log and len(producedChildren) == 2 and generationNum == 1 and discreteRecomb:
                    if discreteRecomb:
                        print(f"Полученный ребенок:")
                        print(f"\t{producedChildren[-1]}")
                    else:
                        print(f"Полученные дети:")
                        print(f"\t1) {producedChildren[-1]}")
                        print(f"\t1) {producedChildren[-2]}")
            else:
                if log and not len(producedChildren) and generationNum == 1 and discreteRecomb:
                    print("Скрещивание не проводится")
        return producedChildren

    def discreteRecombination(self, selectedParents: list[Backpack]) -> list[Backpack]:
        producedChildren = []
        global discreteRecomb
        for i in range(2):
            children = self.uniformCrossing(selectedParents)
            producedChildren += [children[j] for j in range(0, len(children), 2)]
            discreteRecomb = 0
        return producedChildren

    def intermediateRecombinationForTwoParents(self, parents: list[Backpack, Backpack]) -> Backpack:
        child = []
        for i in range(len(parents[0].genome)):
            parameter = random.uniform(-0.25, 1.25)
            child.append(int(parents[0].genome[i] + parameter * (parents[1].genome[i] - parents[0].genome[i])))
            if child[i] < 0:
                child[i] = 0

        child = Backpack(child)
        child.calculateWeight(self.items)
        child.calculateFitness(self.algorithmParameters.maxBackpackWeight, self.items)
        return child

    def IntermediateRecombination(self, selectedParents: list[Backpack]) -> list[Backpack]:
        producedChildren = []
        while log and len(producedChildren) < self.algorithmParameters.amountOfIndividsPerGeneration:
            parents = random.sample(selectedParents, 2)
            global generationNum
            if len(producedChildren) < 1 and generationNum == 1:
                print("\nПРОМЕЖУТОЧНАЯ РЕКОМБИНАЦИЯ")
                print(f"Два выбранных родителя:")
                print(f"\t1) {parents[0]}")
                print(f"\t2) {parents[1]}")
            if random.random() < self.algorithmParameters.crossingProbability:
                producedChildren.append(self.intermediateRecombinationForTwoParents(parents))
                if len(producedChildren) == 1 and generationNum == 1:
                    print(f"Полученный ребенок:")
                    print(f"\t{producedChildren[-1]}")
            else:
                if not len(producedChildren) and generationNum == 1:
                    print("Скрещивание не проводится")
        return producedChildren


class Mutation(AlgorithmDataAndCommonMethods):
    def __init__(self, items: list[Item], algorithmParameters: AlgorithmParameters):
        super().__init__(items, algorithmParameters)
        self.mutationWays = {"Плотность мутации": self.densityMutation,
                             "Мутация перестановкой": self.recombinationMutation,
                             "Мутация случайной заменой": self.randomChange}

    def densityMutationOneChild(self, child: Backpack) -> None:
        global mutationNum
        if log and mutationNum == 1:
            print("\nПЛОТНОСТЬ МУТАЦИИ")
            print(f"Геном до мутации:")
            print(f"{child}")

        parameter = 20
        for i in range(len(child.genome)):
            if log and i == mutationNum == 1:
                print(f"\tПервый ген до мутации: {child.genome[i]}")
            if random.random() < self.algorithmParameters.mutationProbability * 1.25:
                delta = 0
                for j in range(parameter):
                    randVal = random.choices([1, 0], weights=[1 / parameter, 1 - 1 / parameter])[0]
                    delta += randVal * 2 ** (-i)
                sign = random.choice([-1, 1])
                child.genome[i] = int(child.genome[i] + sign * delta * 2)
                if child.genome[i] < 0:
                    child.genome[i] = 0
                if log and i == mutationNum == 1:
                    print(f"\tСлучайно полученное значение, на которое мутирует ген: {int(2 * delta)}")
                    print(f"\tЗнак мутации: {sign}")
                    print(f"\tПервый ген после мутации: {child.genome[i]}")
            else:
                if log and i == mutationNum == 1:
                    print(f"\tПервый ген не мутирует")
        child.calculateWeight(self.items)
        child.calculateFitness(self.algorithmParameters.maxBackpackWeight, self.items)
        if log and mutationNum == 1:
            print(f"Геном после мутации:")
            print(f"{child}")
        mutationNum = 2

    def densityMutation(self, children: list[Backpack]) -> None:
        for i in range(len(children)):
            if random.random() < self.algorithmParameters.mutationProbability:
                self.densityMutationOneChild(children[i])

    def recombinationMutation(self, children: list[Backpack]) -> None:
        global mutationNum
        for i in range(len(children)):
            if random.random() < self.algorithmParameters.mutationProbability:
                if log and mutationNum == 1:
                    print("\nМУТАЦИЯ ПЕРЕСТАНОВКОЙ")
                    print(f"Геном до мутации:")
                    print(f"{children[i]}")
                numOfRecomb = random.randint(1, int(len(self.items) * self.algorithmParameters.mutationProbability + 1))
                if log and mutationNum == 1:
                    print(f"Количество перестановок: {numOfRecomb}")
                for j in range(numOfRecomb):
                    ind1, ind2 = random.sample(range(len(self.items)), 2)
                    children[i].genome[ind1], children[i].genome[ind2] = (
                        children[i].genome[ind2], children[i].genome[ind1])
                    if log and mutationNum == 1 and j == 0:
                        print(f"\tСлучайно выбранные индексы генов для первой перестановки: {ind1}, {ind2}")
                        print(f"\tГеном после первой перестановки: {children[i]}")
                if log and mutationNum == 1:
                    print(f"Геном после мутации:")
                    print(f"{children[i]}")
                mutationNum = 2

    def randomChange(self, children: list[Backpack]) -> None:
        global mutationNum
        for i in range(len(children)):
            if random.random() < self.algorithmParameters.mutationProbability:
                if log and mutationNum == 1:
                    print("\nМУТАЦИЯ СЛУЧАЙНОЙ ЗАМЕНОЙ")
                    print(f"Геном до мутации:")
                    print(f"{children[i]}")
                numOfChanges = random.randint(1,
                                              int(len(self.items) * self.algorithmParameters.mutationProbability + 1))
                if log and mutationNum == 1:
                    print(f"Количество замен: {numOfChanges}")
                for j in range(numOfChanges):
                    ind = random.choice(range(len(self.items)))
                    value = random.randint(0, self.algorithmParameters.maxBackpackWeight // self.items[ind].cost)
                    children[i].genome[ind] = value
                    if log and mutationNum == 1 and j == 0:
                        print(f"\tСлучайно выбранный индекс гена для первой замены: {ind}")
                        print(f"\tНовое значение гена для первой замены: {value}")
                        print(f"\tГеном после первой замены: {children[i]}")
                if log and mutationNum == 1:
                    print(f"Геном после мутации:")
                    print(f"{children[i]}")
                mutationNum = 2


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

    # def dynamicProgrammingSolution(self) -> Backpack:
    #     pass

    def getSolution(self) -> list[IterationInfo]:
        generation = self.generateRandomGeneration()
        # print(f"Начальное случайно сгенерированное поколение:")
        # self.outputBackpacks(generation.backpacks)
        # print()

        maxFitness = []
        averageFitness = []
        selectedParents = []
        producedChildren = []
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

            if self.algorithmParameters.wayOfParentsSelection == "Индбридинг":
                while len(producedChildren) != self.algorithmParameters.amountOfIndividsPerGeneration:
                    twoParents = self.parentsSelection(generation)
                    selectedParents += twoParents
                    producedChildren += self.crossing(twoParents)
            else:
                selectedParents = self.parentsSelection(generation)
                producedChildren = self.crossing(selectedParents)
            self.mutation(producedChildren)
            generation = self.generationSelection(generation, producedChildren)
        if log:
            self.drawPlot(maxFitness, averageFitness)
        return allIterations


if __name__ == '__main__':
    items = [Item(5, 2), Item(7, 3), Item(6, 4), Item(3, 2)]
    maxBackpackWeight = 22
    crossingProbability = 0.9
    mutationProbability = 0.9
    amountOfIndividsPerGeneration = 20
    maxAmountOfGenerations = 20

    parentsSelectionWays = ["Турнир", "Рулетка", "Инбридинг"]
    crossingWays = ["Равномерное скрещивание", "Дискретная рекомбинация", "Промежуточная рекомбинация"]
    mutationWays = ["Плотность мутации", "Мутация перестановкой", "Мутация случайной заменой"]
    NewGenerationSelectionWays = ["Элитарный отбор", "Отбор вытеснением", "Отбор усечением"]

    wayOfParentsSelection = parentsSelectionWays[0]
    wayOfCrossing = crossingWays[0]
    wayOfMutation = mutationWays[0]
    wayOfNewGenerationSelection = NewGenerationSelectionWays[0]

    GA = GeneticAlgorithm(items, AlgorithmParameters(maxBackpackWeight, crossingProbability, mutationProbability,
                                                     amountOfIndividsPerGeneration, maxAmountOfGenerations,
                                                     wayOfParentsSelection, wayOfCrossing, wayOfMutation,
                                                     wayOfNewGenerationSelection))
    GA.getSolution()

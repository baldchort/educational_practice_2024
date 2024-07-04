import random
from abc import ABC, abstractmethod

from src.libs.algorithm_parameters import *


class ParentSelectionStrategy(ABC):
    @abstractmethod
    def selectParent(self, generation: Generation, algorithmParameters: AlgorithmParameters) -> list[Backpack]:
        pass


class TournamentSelection(ParentSelectionStrategy):
    def selectParent(self, generation: Generation, algorithmParameters: AlgorithmParameters) -> list[Backpack]:
        selectedParents = []
        while len(selectedParents) != algorithmParameters.amountOfIndividsPerGeneration:
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


class RouletteSelection(ParentSelectionStrategy):
    def selectParent(self, generation: Generation, algorithmParameters: AlgorithmParameters) -> list[Backpack]:
        selectedParents = []
        sumFitness = sum([individ.cost for individ in generation])
        probabilities = [individ.cost / sumFitness for individ in generation]

        table = PrettyTable(['№', 'Особь', 'Приспособленность', 'Вероятность выбора'])
        for i in range(len(generation)):
            table.add_row([i, generation[i].genome, generation[i].cost, round(probabilities[i], 4)])

        while len(selectedParents) != algorithmParameters.amountOfIndividsPerGeneration:
            selectedParents.append(random.choices(generation, weights=probabilities, k=1)[0])

            global generationNum
            if log and len(selectedParents) < 2 and generationNum == 1:
                print("\nОТБОР РУЛЕТКОЙ")
                print(table)
                print(f"Случайно выбранная особь:")
                print(f"\t{selectedParents[0]}")

        return selectedParents


class InbreedingSelection(ParentSelectionStrategy):
    def selectTwoParents(self, generation: Generation) -> list[Backpack]:
        firstParentInd = random.choice([i for i in range(len(generation))])
        selectedParents = [generation.descendingSortedBackpacks[firstParentInd]]
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

    def selectParent(self, generation: Generation, algorithmParameters: AlgorithmParameters) -> list[Backpack]:
        selectedParents = []
        while len(selectedParents) < algorithmParameters.amountOfIndividsPerGeneration:
            selectedParents += self.selectTwoParents(generation)
        return selectedParents

import random
from abc import ABC, abstractmethod

from src.libs.algorithm_parameters import *


class GenerationSelectionStrategy(ABC):
    @abstractmethod
    def select(self, oldGeneration: Generation, producedChildren: list[Backpack],
               algorithmParameters: AlgorithmParameters) -> Generation:
        pass

    def outputBackpacks(self, backpacks: list[Backpack], algorithmParameters: AlgorithmParameters) -> None:
        for i, backpack in enumerate(backpacks):
            print(f"{i + 1}) {backpack.genome}")
            print(f"\tСуммарная стоимость вещей: {backpack.cost}")
            print(
                f"\tСуммарный вес вещей: {backpack.weight}, дельта = {algorithmParameters.maxBackpackWeight - backpack.weight}")


class EliteSelection(GenerationSelectionStrategy):
    def select(self, oldGeneration: Generation, producedChildren: list[Backpack],
               algorithmParameters: AlgorithmParameters) -> Generation:
        allCandidates = oldGeneration.backpacks + producedChildren
        generation = sorted(allCandidates, key=lambda x: x.cost, reverse=True)[
                     :int(0.1 * algorithmParameters.amountOfIndividsPerGeneration)]
        global generationNum
        if log and generationNum == 1:
            print(f"\nЭЛИТАРНЫЙ ОТБОР")
            print(f"Лучшие 10% родительских и детских особей:")
            self.outputBackpacks(generation, algorithmParameters)
        while len(generation) != algorithmParameters.amountOfIndividsPerGeneration:
            generation.append(random.choice(allCandidates))
        if log and generationNum == 1:
            print(f"Остальные 90% выбираются случайно")
            print(f"\nИтоговое новое поколение:")
            self.outputBackpacks(generation, algorithmParameters)
            print()
        return Generation(generation)


class TruncationSelection(GenerationSelectionStrategy):
    def select(self, oldGeneration: Generation, producedChildren: list[Backpack],
               algorithmParameters: AlgorithmParameters) -> Generation:
        sortedOldGeneration = sorted(oldGeneration.backpacks + producedChildren, key=lambda x: x.cost, reverse=True)[
                              :int(0.5 * algorithmParameters.amountOfIndividsPerGeneration)]
        newGeneration = []
        while len(newGeneration) != algorithmParameters.amountOfIndividsPerGeneration:
            newGeneration.append(random.choice(sortedOldGeneration))

        global generationNum
        if log and generationNum == 1:
            print(f"\nОТБОР УСЕЧЕНИЕМ")
            print(f"Выбираем среди 50% лучших родительских и детских особей:")
            self.outputBackpacks(sortedOldGeneration, algorithmParameters)
            print(f"\nИтоговое новое поколение:")
            self.outputBackpacks(newGeneration, algorithmParameters)
            print()

        return Generation(newGeneration)


class ExclusionSelection(GenerationSelectionStrategy):
    def select(self, oldGeneration: Generation, producedChildren: list[Backpack],
               algorithmParameters: AlgorithmParameters) -> Generation:
        allCandidates = oldGeneration.backpacks + producedChildren
        sortedOldGeneration = sorted(allCandidates, key=lambda x: x.cost, reverse=True)[
                              :int(0.5 * algorithmParameters.amountOfIndividsPerGeneration)]
        newGeneration = []
        addedToNewGenerationGenomes = []

        for individ in sortedOldGeneration:
            if len(newGeneration) == algorithmParameters.amountOfIndividsPerGeneration:
                break
            if individ.genome not in addedToNewGenerationGenomes:
                newGeneration.append(individ)
                addedToNewGenerationGenomes.append(individ.genome)

        while len(newGeneration) != algorithmParameters.amountOfIndividsPerGeneration:
            newGeneration.append(random.choice(allCandidates))

        global generationNum
        if log and generationNum == 1:
            print(f"\nОТБОР ВЫТЕСНЕНИЕМ")
            print(f"Выбираем в новое поколение лучшие уникальные родительские и детские особи")
            print(f"\nИтоговое новое поколение:")
            self.outputBackpacks(newGeneration, algorithmParameters)
            print()

        return Generation(newGeneration)

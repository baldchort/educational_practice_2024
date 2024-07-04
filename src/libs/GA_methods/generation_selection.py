import random
from abc import ABC, abstractmethod

from src.libs.algorithm_parameters import *


class GenerationSelectionStrategy(ABC):
    @abstractmethod
    def select(self, selectedParents: list[Backpack], producedChildren: list[Backpack],
               algorithmParameters: AlgorithmParameters, items: list[Item]) -> Generation:
        pass


class EliteSelection(GenerationSelectionStrategy):
    def select(self, selectedParents: list[Backpack], producedChildren: list[Backpack],
               algorithmParameters: AlgorithmParameters, items: list[Item]) -> Generation:
        allCandidates = selectedParents + producedChildren
        generation = sorted(allCandidates, key=lambda x: x.cost, reverse=True)[
                     :int(0.1 * algorithmParameters.amountOfIndividsPerGeneration)]
        print(f"\nЭлитарный отбор")
        print(f"Лучшие 10% родительских и детских особей:")
        for i, backpack in enumerate(generation):
            print(f"{i + 1}) {backpack.genome}")
            print(f"\tСуммарная стоимость вещей: {backpack.cost}")
            print(
                f"\tСуммарный вес вещей: {backpack.weight}, дельта = {algorithmParameters.maxBackpackWeight - backpack.weight}")

        while len(generation) != algorithmParameters.amountOfIndividsPerGeneration:
            generation.append(random.choice(allCandidates))
        print(f"Остальные 90% выбираются случайно")
        print(f"\nИтоговое новое поколение:")
        for i, backpack in enumerate(generation):
            print(f"{i + 1}) {backpack.genome}")
            print(f"\tСуммарная стоимость вещей: {backpack.cost}")
            print(
                f"\tСуммарный вес вещей: {backpack.weight}, дельта = {algorithmParameters.maxBackpackWeight - backpack.weight}")

        return Generation(generation)

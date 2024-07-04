import random
from abc import ABC, abstractmethod

from src.libs.algorithm_parameters import *


class CrossingStrategy(ABC):
    @abstractmethod
    def crossing(self, selectedParents: list[Backpack], algorithmParameters: AlgorithmParameters,
                 items: list[Item]) -> list[Backpack]:
        pass


class UniformCrossing(CrossingStrategy):
    def crossingForTwoParents(self, parents: tuple[Backpack, Backpack], items: list[Item],
                              algorithmParameters: AlgorithmParameters) -> list[Backpack]:
        children = [[], []]
        for j in range(len(parents[0].genome)):
            i = random.choice([0, 1])
            children[0].append(parents[i].genome[j])
            children[1].append(parents[1 - i].genome[j])

        for i in range(len(children)):
            children[i] = Backpack(children[i])
            children[i].calculateWeight(items)
            children[i].calculateFitness(algorithmParameters.maxBackpackWeight, items)
        return children

    def crossing(self, selectedParents: list[Backpack], algorithmParameters: AlgorithmParameters,
                 items: list[Item]) -> list[Backpack]:
        producedChildren = []
        while len(producedChildren) <= algorithmParameters.amountOfIndividsPerGeneration:
            parents = random.sample(selectedParents, 2)
            if len(producedChildren) < 2:
                print("\nРавномерное скрещивание особей")
                print(f"Два случайно выбранных родителя:")
                print(f"\t1) {parents[0]}")
                print(f"\t2) {parents[1]}")
            if random.random() < algorithmParameters.crossingProbability:
                producedChildren += self.crossingForTwoParents(parents, items, algorithmParameters)
                if len(producedChildren) == 2:
                    print(f"Полученные дети:")
                    print(f"\t1) {producedChildren[-1]}")
                    print(f"\t2) {producedChildren[-2]}")
            elif len(producedChildren) < 2:
                print("Скрещивание не проводится")
        return producedChildren

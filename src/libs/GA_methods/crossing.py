import random
from abc import ABC, abstractmethod

from src.libs.algorithm_parameters import *


class CrossingStrategy(ABC):
    @abstractmethod
    def crossing(self, selectedParents: list[Backpack], algorithmParameters: AlgorithmParameters) -> list[Backpack]:
        pass


class UniformCrossing(CrossingStrategy):
    def crossingForTwoParents(self, parents: list[Backpack, Backpack]) -> list[Backpack]:
        children = [[], []]
        for j in range(len(parents[0].genome)):
            i = random.choice([0, 1])
            children[0].append(parents[i].genome[j])
            children[1].append(parents[1 - i].genome[j])
        return list(map(Backpack, children))

    def crossing(self, selectedParents: list[Backpack], algorithmParameters: AlgorithmParameters) -> list[Backpack]:
        producedChildren = []
        while len(producedChildren) < algorithmParameters.amountOfIndividsPerGeneration:
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
            if random.random() < algorithmParameters.crossingProbability:
                producedChildren += self.crossingForTwoParents(parents)
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


class DiscreteRecombination(CrossingStrategy):
    def crossing(self, selectedParents: list[Backpack], algorithmParameters: AlgorithmParameters) -> list[Backpack]:
        producedChildren = []
        global discreteRecomb
        for i in range(2):
            children = UniformCrossing().crossing(selectedParents, algorithmParameters)
            producedChildren += [children[j] for j in range(0, len(children), 2)]
            discreteRecomb = 0
        return producedChildren


class IntermediateRecombination(CrossingStrategy):
    def crossingForTwoParents(self, parents: list[Backpack, Backpack]) -> Backpack:
        child = []
        for i in range(len(parents[0].genome)):
            parameter = random.uniform(-0.25, 1.25)
            child.append(int(parents[0].genome[i] + parameter * (parents[1].genome[i] - parents[0].genome[i])))
            if child[i] < 0:
                child[i] = 0

        child = Backpack(child)
        return child

    def crossing(self, selectedParents: list[Backpack], algorithmParameters: AlgorithmParameters) -> list[Backpack]:
        producedChildren = []
        while len(producedChildren) < algorithmParameters.amountOfIndividsPerGeneration:
            parents = random.sample(selectedParents, 2)
            global generationNum
            if log and len(producedChildren) < 1 and generationNum == 1:
                print("\nПРОМЕЖУТОЧНАЯ РЕКОМБИНАЦИЯ")
                print(f"Два выбранных родителя:")
                print(f"\t1) {parents[0]}")
                print(f"\t2) {parents[1]}")
            if random.random() < algorithmParameters.crossingProbability:
                producedChildren.append(self.crossingForTwoParents(parents))
                if log and len(producedChildren) == 1 and generationNum == 1:
                    print(f"Полученный ребенок:")
                    print(f"\t{producedChildren[-1]}")
            else:
                if log and not len(producedChildren) and generationNum == 1:
                    print("Скрещивание не проводится")
        return producedChildren

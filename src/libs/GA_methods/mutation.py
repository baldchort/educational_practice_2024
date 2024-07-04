from abc import ABC, abstractmethod
import random

from src.libs.algorithm_parameters import *


class MutationStrategy(ABC):
    @abstractmethod
    def mutation(self, children: list[Backpack], algorithmParameters: AlgorithmParameters, items: list[Item]) -> None:
        pass


class DensityMutation(MutationStrategy):
    def mutationOneChild(self, child: Backpack, algorithmParameters: AlgorithmParameters,
                         items: list[Item]) -> None:
        print("\nПлотность мутации")
        print(f"Геном до мутации:")
        print(f"{child}")

        parameter = 20
        for i in range(len(child.genome)):
            if i == 0:
                print(f"\tПервый ген до мутации: {child.genome[i]}")
            if random.random() < algorithmParameters.mutationProbability:
                delta = 0
                for j in range(parameter):
                    randVal = random.choices([1, 0], weights=[1 / parameter, 1 - 1 / parameter])[0]
                    delta += randVal * 2 ** (-i)
                sign = random.choice([-1, 1])
                child.genome[i] = int(child.genome[i] + sign * delta * 2)
                if child.genome[i] < 0:
                    child.genome[i] = 0
                if i == 0:
                    print(f"\tСлучайно полученное значение, на которое мутирует ген: {int(2 * delta)}")
                    print(f"\tЗнак мутации: {sign}")
                    print(f"\tПервый ген после мутации: {child.genome[i]}")
            else:
                if i == 0:
                    print(f"\tПервый ген не мутирует")
        child.calculateWeight(items)
        child.calculateFitness(algorithmParameters.maxBackpackWeight, items)
        print(f"Геном после мутации:")
        print(f"{child}")

    def mutation(self, children: list[Backpack], algorithmParameters: AlgorithmParameters, items: list[Item]) -> None:
        for i in range(len(children)):
            if random.random() < algorithmParameters.mutationProbability:
                self.mutationOneChild(children[i], algorithmParameters, items)


class PermutationMutation(MutationStrategy):
    def mutation(self, children: list[Backpack], algorithmParameters: AlgorithmParameters, items: list[Item]) -> None:
        # impl
        pass


class ExchangeMutation(MutationStrategy):
    def mutation(self, children: list[Backpack], algorithmParameters: AlgorithmParameters, items: list[Item]) -> None:
        # impl
        pass

import random
from abc import ABC, abstractmethod

from src.libs.algorithm_parameters import *


class MutationStrategy(ABC):
    @abstractmethod
    def mutation(self, children: list[Backpack], algorithmParameters: AlgorithmParameters, items: list[Item]) -> None:
        pass


class DensityMutation(MutationStrategy):
    def mutationOneChild(self, child: Backpack, algorithmParameters: AlgorithmParameters) -> None:
        global mutationNum
        if log and mutationNum == 1:
            print("\nПЛОТНОСТЬ МУТАЦИИ")
            print(f"Геном до мутации:")
            print(f"{child}")

        parameter = 20
        for i in range(len(child.genome)):
            if log and i == mutationNum == 1:
                print(f"\tПервый ген до мутации: {child.genome[i]}")
            if random.random() < algorithmParameters.mutationProbability * 1.25:
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
        if log and mutationNum == 1:
            print(f"Геном после мутации:")
            print(f"{child}")
        mutationNum = 2

    def mutation(self, children: list[Backpack], algorithmParameters: AlgorithmParameters, items: list[Item]) -> None:
        for i in range(len(children)):
            if random.random() < algorithmParameters.mutationProbability:
                self.mutationOneChild(children[i], algorithmParameters)


class PermutationMutation(MutationStrategy):
    def mutation(self, children: list[Backpack], algorithmParameters: AlgorithmParameters, items: list[Item]) -> None:
        global mutationNum
        for i in range(len(children)):
            if random.random() < algorithmParameters.mutationProbability:
                if log and mutationNum == 1:
                    print("\nМУТАЦИЯ ПЕРЕСТАНОВКОЙ")
                    print(f"Геном до мутации:")
                    print(f"{children[i]}")
                num_of_recomb = random.randint(1, int(len(items) * algorithmParameters.mutationProbability + 1))
                if log and mutationNum == 1:
                    print(f"Количество перестановок: {num_of_recomb}")
                for j in range(num_of_recomb):
                    ind1, ind2 = random.sample(range(len(items)), 2)
                    children[i].genome[ind1], children[i].genome[ind2] = (
                        children[i].genome[ind2], children[i].genome[ind1])
                    if log and mutationNum == 1 and j == 0:
                        print(f"\tСлучайно выбранные индексы генов для первой перестановки: {ind1}, {ind2}")
                        print(f"\tГеном после первой перестановки: {children[i]}")
                if log and mutationNum == 1:
                    print(f"Геном после мутации:")
                    print(f"{children[i]}")
                mutationNum = 2


class ExchangeMutation(MutationStrategy):
    def mutation(self, children: list[Backpack], algorithmParameters: AlgorithmParameters, items: list[Item]) -> None:
        global mutationNum
        for i in range(len(children)):
            if random.random() < algorithmParameters.mutationProbability:
                if log and mutationNum == 1:
                    print("\nМУТАЦИЯ СЛУЧАЙНОЙ ЗАМЕНОЙ")
                    print(f"Геном до мутации:")
                    print(f"{children[i]}")
                numOfChanges = random.randint(1,
                                              int(len(children[i]) * algorithmParameters.mutationProbability + 1))
                if log and mutationNum == 1:
                    print(f"Количество замен: {numOfChanges}")
                for j in range(numOfChanges):
                    i = random.choice(range(len(children[i])))
                    value = random.randint(0, algorithmParameters.maxBackpackWeight // items[i].cost)
                    children[i].genome[i] = value
                    if log and mutationNum == 1 and j == 0:
                        print(f"\tСлучайно выбранный индекс гена для первой замены: {i}")
                        print(f"\tНовое значение гена для первой замены: {value}")
                        print(f"\tГеном после первой замены: {children[i]}")
                if log and mutationNum == 1:
                    print(f"Геном после мутации:")
                    print(f"{children[i]}")
                mutationNum = 2

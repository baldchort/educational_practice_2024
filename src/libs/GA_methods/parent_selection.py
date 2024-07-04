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

            if len(selectedParents) < 2:
                print("\nОтбор родителей турниром")
                individ1 = generation[tournamentIndexes[0]]
                individ2 = generation[tournamentIndexes[1]]
                print(f"Две случайно выбранные особи:")
                print(f"\t1) {individ1}")
                print(f"\t2) {individ2}")
                print(f"\tВыбираем лучшую из них: {selectedParents[-1].genome}")

        return selectedParents

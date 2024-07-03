from typing import Iterator


class Item:
    def __init__(self, cost: int, weight: int):
        self.cost = cost
        self.weight = weight

    def __str__(self) -> str:
        return f"Вещь стоит {self.cost} и весит {self.weight}"

    def __lt__(self, other: 'Item') -> bool:
        return self.weight < other.weight

    def __le__(self, other: 'Item') -> bool:
        return self.weight <= other.weight

    def __gt__(self, other: 'Item') -> bool:
        return self.weight > other.weight

    def __ge__(self, other: 'Item') -> bool:
        return self.weight >= other.weight

class Backpack:
    def __init__(self, amountOfEachItems: list[int]):
        self.genome = amountOfEachItems
        self.cost = 0
        self.weight = 0

    def __str__(self):
        return f"{self.genome}, стоимость = {self.cost}, вес = {self.weight}"

    def __iter__(self) -> Iterator:
        return iter(self.genome)

    def __le__(self, other: 'Backpack') -> bool:
        return self.cost <= other.cost

    def __lt__(self, other: 'Backpack') -> bool:
        return self.cost < other.cost

    def __ge__(self, other: 'Backpack') -> bool:
        return self.cost >= other.cost

    def __gt__(self, other: 'Backpack') -> bool:
        return self.cost > other.cost

    def calculateWeight(self, items: list[Item]) -> None:
        self.weight = sum(items[i].weight * self.genome[i] for i in range(len(items)))

    def calculateFitness(self, limitWeight: int, items: list[Item]) -> None:
        sumCost = sum(items[i].cost * self.genome[i] for i in range(len(items)))
        overload = self.weight - limitWeight
        if overload <= 0:
            self.cost = sumCost
        else:
            penalty = (self.weight - limitWeight) / limitWeight
            self.cost = int(sumCost * (1 - penalty ** 2)) if overload <= max(item.weight for item in items) else 0


class Generation:
    def __init__(self, backpacks: list[Backpack]):
        self.backpacks = backpacks
        self.maxFitness = 0
        self.averageFitness = 0

    def __iter__(self) -> Iterator:
        return iter(self.backpacks)

    def __len__(self) -> int:
        return len(self.backpacks)

    def __getitem__(self, key: int) -> Backpack:
        return self.backpacks[key]

    def __str__(self):
        return "\n".join(map(str, self.backpacks))

    def append(self, item: Backpack) -> None:
        self.backpacks.append(item)

    def expend(self, other: 'Generation') -> None:
        self.backpacks.extend(other)

    def remove(self, item: Backpack) -> None:
        self.backpacks.remove(item)

    def getBestBackpacks(self) -> list[Backpack]:
        sorted_backpacks = sorted(self.backpacks, key=lambda x: x.cost, reverse=True)
        return sorted_backpacks[:3]

    def getAverageFitness(self) -> float:
        return sum(backpack.cost for backpack in self.backpacks) / len(self.backpacks)

    def getMaxFitness(self) -> int:
        return self.getBestBackpacks()[0].cost

    def calculateWeight(self, items: list[Item]) -> None:
        for backpack in self.backpacks:
            backpack.calculateWeight(items)

    def calculateFitness(self, limitWeight: int, items: list[Item]) -> None:
        for backpack in self.backpacks:
            backpack.calculateFitness(limitWeight, items)


class AlgorithmParameters:
    def __init__(self,
                 maxBackpackWeight: int,
                 crossingProbability: float,
                 mutationProbability: float,
                 amountOfIndividsPerGeneration: int,
                 maxAmountOfGenerations: int):
        self.maxBackpackWeight = maxBackpackWeight
        self.crossingProbability = crossingProbability
        self.mutationProbability = mutationProbability
        self.amountOfIndividsPerGeneration = amountOfIndividsPerGeneration
        self.maxAmountOfGenerations = maxAmountOfGenerations



class IterationInfo:
    def __init__(self, bestBackpacks: list[Backpack], currentMaxFitness: int, currentAverageFitness: float):
        self.bestBackpacks = bestBackpacks
        self.currentMaxFitness = currentMaxFitness
        self.currentAverageFitness = currentAverageFitness


# class AllInfo:
#     def __init__(self, maxBackpackWeight: int, items: list[Item]):
#         self.maxBackpackWeight = maxBackpackWeight
#         self.items = items
#         self.maxFitness = []
#         self.averageFitness = []
#
#     def appendMaxFitness(self, iteration: IterationInfo) -> None:
#         self.maxFitness.append(iteration.currentMaxFitness)
#
#     def appendAverageFitness(self, iteration: IterationInfo) -> None:
#         self.averageFitness.append(iteration.currentAverageFitness)
#
#     def drawPlot(self) -> None:
#         pass


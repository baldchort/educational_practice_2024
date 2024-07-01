from typing import Iterator


class Item:
    def __init__(self, cost: int, weight: int):
        self.cost = cost
        self.weight = weight

    def __str__(self):
        return f"Вещь стоит {self.cost} и весит {self.weight}"


class Backpack:
    def __init__(self, amountOfEachItems: list[int]):
        self.genome = amountOfEachItems
        self.cost = 0
        self.weight = 0

    def calculationWeight(self, items: list[Item]) -> None:
        self.weight = sum(items[i].weight * self.genome[i] for i in range(len(items)))

    # нужно исправить перерасчёт целевой функции:
    # пусть жёсткий штраф будет начинаться от перевеса на вес самой тяжёлой вещи
    # а мягкий штраф нужно ещё придумать :/
    def calculationFitness(self, limitWeight: int, items: list[Item]) -> None:
        self.cost = 0 if self.weight > limitWeight else sum(items[i].cost * self.genome[i] for i in range(len(items)))

    def __str__(self):
        return ", ".join(map(str, self.genome))

    def __iter__(self) -> Iterator:
        return iter(self.genome)

    def __le__(self, other: 'Backpack'):
        return self.cost <= other.cost

    def __lt__(self, other: 'Backpack'):
        return self.cost < other.cost


class Generation:
    def __init__(self, backpacks: list[Backpack]):
        self.backpacks = backpacks

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


class CurrentIterationInfo:
    def __init__(self, bestBackpacks: list[Backpack], currentMaxFitness: float, currentAverageFitness: float):
        self.bestBackpacks = bestBackpacks
        self.currentMaxFitness = currentMaxFitness
        self.currentAverageFitness = currentAverageFitness
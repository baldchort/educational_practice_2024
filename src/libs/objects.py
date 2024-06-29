from typing import Iterator


class Item:
    def __init__(self, weight: int, cost: int):
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return f"Вещь стоит {self.cost} и весит {self.weight}"


class Backpack:
    def __init__(self, amountOfEachItems: list[int]):
        self.genome = amountOfEachItems
        self.cost = 0
        self.weight = 0

    def calculationWeight(self, items: list[Item]) -> None:
        self.weight = sum(items[i].weight * self.genome for i in range(len(items)))

    def calculationFitness(self, limitWeight: int) -> None:
        self.cost = 0 if self.weight > limitWeight else sum(item.cost for item in self.items)

    def __str__(self):
        return f"Рюкзак содержит: \n{'\n'.join(str(item) for item in self.items)}"

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

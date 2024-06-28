class Item:
    def __init__(self, weight: int, cost: int):
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return f"Вещь стоит {self.cost} и весит {self.weight}"


class Backpack:
    def __init__(self, items: list[Item]):
        self.items = items
        self.cost = 0
        self.weight = 0

    def calculationWeight(self) -> None:
        self.weight = sum(item.weight for item in self.items)

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

    def __iter__(self):
        return iter(self.backpacks)

    def __len__(self):
        return len(self.backpacks)

    def __getitem__(self, key):
        return self.backpacks[key]


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

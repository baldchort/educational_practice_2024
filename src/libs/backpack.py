class Item:
    def __init__(self, weight: int, cost: int):
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return f"Вещь стоит {self.cost} и весит {self.weight}"


class Backpack:
    def __init__(self, itemAmount: int):
        self.items = [Item(0, 0) for _ in range(itemAmount)]
        self.cost = 0
        self.weight = 0
        self.amount = 0

    def generateGeneration(self):
        for item in self.items:
            pass

    def calculationWeight(self) -> None:
        self.weight = sum(x.weight for x in self.items)

    def calculationFitness(self, limitWeight: int) -> None:
        self.cost = 0 if self.weight > limitWeight else sum(x.cost for x in self.items)


class BackpackBuilder:
    def __init__(self, items: list, limitWeight: int):
        self.items = items
        self.limitWeight = limitWeight


class Generation:
    def __init__(self, limitAmount: int, limitWeight: int):
        self.generation = []
        self.limitAmount = limitAmount
        self.limitWeight = limitWeight

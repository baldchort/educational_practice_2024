class Item:
    def __init__(self, cost: int, weight: int):
        self.cost = cost
        self.weight = weight

    def __str__(self):
        return f"Вещь стоит {self.cost} и весит {self.weight}"
